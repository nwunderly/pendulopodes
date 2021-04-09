import numpy as np

from .constants import g


"""
Assumptions:
    (constant) unit length
    unit mass
    rotate about origin
    2-dimensional (for now)
    theta = 0 at (x, y) = (1, 0)

Coordinate system:

            |
            |
------------|------------> Y
            |
            |
            |
            |
            |
            V
            X

Angular kinematics: (RADIANS)
    theta: angle
    omega: angular velocity
    alpha: angular acceleration
"""


def inertial_to_polar(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan(y/x)
    return r, theta


def polar_to_inertial(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y


# def eqm_single_simple_pendulum(theta, omega):
#     """Single-element simple pendulum equation of motion.
#     (Shoutout to Derek Paley)
#
#     tension = m*g*cos(theta)+m*l*theta
#     alpha = -g/l*sin(theta
#     """
#     alpha = -g*np.sin(theta)
#
#     return omega, alpha
#
#
# def system_single_simple_pendulum(t, y):
#     """System of differential equations for a single-element simple pendulum.
#
#     y = [theta, omega]
#     y_dot = [omega, alpha]
#     """
#     theta, omega = y
#
#     omega, alpha = eqm_single_simple_pendulum(theta, omega)
#     y_dot = [omega, alpha]
#
#     return y_dot
#
#
# def eqm_double_simple_pendulum(theta1, omega1, theta2, omega2):
#     """Two-element simple pendulum equation of motion.
#
#     Equations found at https://www.myphysicslab.com/pendulum/double-pendulum-en.html
#     """
#     alpha1_n = -g*(2*m1 + m2)*np.sin(theta1) - m2*g*np.sin(theta1 - 2*theta2) - 2*np.sin(theta1 - theta2)*m2*(omega2**2 * l2 + omega1**2 * l1 * np.cos(theta1 - theta2))
#     alpha1_d = l1 * (2*m1 + m2 - m2*np.cos(2*theta1 - 2*theta2))
#     alpha1 = alpha1_n / alpha1_d
#
#     alpha2_n = 2*np.sin(theta1 - theta2) * (omega1**2 * l1 * (m1 + m2) + g*(m1 + m2) * np.cos(theta1) + omega2**2 * l2 * m2 * np.cos(theta1 - theta2))
#     alpha2_d = l2 * (2*m1 + m2 - m2*np.cos(2*theta1 - 2*theta2))
#     alpha2 = alpha2_n / alpha2_d
#
#     return omega1, alpha1, omega2, alpha2
#
#
# def system_double_simple_pendlum(t, y):
#     """System of differential equations for a two-element simple pendulum.
#
#     y = [theta1, omega1, theta2, omega2]
#     y_dot = [omega1, alpha1, omega2, alpha2]
#     """
#     theta1, omega1, theta2, omega2 = y
#
#     omega1, alpha1, omega2, alpha2 = eqm_double_simple_pendulum(theta1, omega1, theta2, omega2)
#     y_dot = [omega1, alpha1, omega2, alpha2]
#
#     return y_dot


class NElementPendulum:
    def __init__(self, element_count, *, length=(1,), mass=(1,), theta0=(np.pi/2,), omega0=(0,)):
        if element_count > 1:
            assert element_count % len(length) == 0
            assert element_count % len(mass) == 0
            assert element_count % len(theta0) == 0
            assert element_count % len(omega0) == 0

        self.element_count = element_count
        self.length = length*(element_count//len(length))
        self.mass = mass*(element_count//len(mass))
        self.theta0 = theta0*(element_count//len(theta0))
        self.omega0 = omega0*(element_count//len(omega0))

    def eqm_single_simple_pendulum(self, theta, omega):
        """Single-element simple pendulum equation of motion.
        (Shoutout to Derek Paley)

        tension = m*g*cos(theta)+m*l*theta
        alpha = -g/l*sin(theta
        """
        alpha = -g / self.length[0] * np.sin(theta)

        return omega, alpha

    def system_single_simple_pendulum(self, t, y):
        """System of differential equations for a single-element simple pendulum.

        y = [theta, omega]
        y_dot = [omega, alpha]
        """
        theta, omega = y

        omega, alpha = self.eqm_single_simple_pendulum(theta, omega)
        y_dot = [omega, alpha]

        return y_dot

    def eqm_double_simple_pendulum(self, theta1, omega1, theta2, omega2):
        """Two-element simple pendulum equation of motion.

        Equations found at https://www.myphysicslab.com/pendulum/double-pendulum-en.html
        """
        m1 = self.mass[0]
        m2 = self.mass[1]
        l1 = self.length[0]
        l2 = self.length[1]

        alpha1_n = -g * (2 * m1 + m2) * np.sin(theta1) - m2 * g * np.sin(theta1 - 2 * theta2) - 2 * np.sin(theta1 - theta2) * m2 * (
                    omega2 ** 2 * l2 + omega1 ** 2 * l1 * np.cos(theta1 - theta2))
        alpha1_d = l1 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2))
        alpha1 = alpha1_n / alpha1_d

        alpha2_n = 2 * np.sin(theta1 - theta2) * (
                    omega1 ** 2 * l1 * (m1 + m2) + g * (m1 + m2) * np.cos(theta1) + omega2 ** 2 * l2 * m2 * np.cos(theta1 - theta2))
        alpha2_d = l2 * (2 * m1 + m2 - m2 * np.cos(2 * theta1 - 2 * theta2))
        alpha2 = alpha2_n / alpha2_d

        return omega1, alpha1, omega2, alpha2

    def system_double_simple_pendlum(self, t, y):
        """System of differential equations for a two-element simple pendulum.

        y = [theta1, omega1, theta2, omega2]
        y_dot = [omega1, alpha1, omega2, alpha2]
        """
        theta1, omega1, theta2, omega2 = y

        omega1, alpha1, omega2, alpha2 = self.eqm_double_simple_pendulum(theta1, omega1, theta2, omega2)
        y_dot = [omega1, alpha1, omega2, alpha2]

        return y_dot
