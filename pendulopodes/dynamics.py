import numpy as np

from .constants import *


"""
Assumptions:
    (constant) unit length
    unit mass
    rotate about origin
    2-dimensional (for now)
    theta = 0 at (x, y) = (1, 0)

Coordinate system:
    (shoutout to Derek Paley)

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

Angular kinematics:
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


def eqm_single_simple_pendulum(theta, omega):
    """Single-part simple pendulum equation of motion.

    tension = m*g*cos(theta)+m*l*theta
    alpha = -g/l*sin(theta
    """
    alpha = -g*np.sin(theta)

    return omega, alpha


def system_single_simple_pendulum(t, y):
    """Single-part simple pendulum system of differential equations, in vector form.

    y = [theta, omega]
    y_dot = [omega, alpha]
    """
    theta, omega = y

    omega, alpha = eqm_single_simple_pendulum(theta, omega)
    y_dot = [omega, alpha]

    return y_dot


def eqm_double_simple_pendulum(theta1, omega1, theta2, omega2):
    """Double-part simple pendulum equation of motion"""

    alpha1_n = -g*(2*m1 + m2)*np.sin(theta1) - m2*g*np.sin(theta1 - 2*theta2) - 2*np.sin(theta1 - theta2)*m2*(omega2**2 * l2 + omega1**2 * l1 * np.cos(theta1 - theta2))
    alpha1_d = l1 * (2*m1 + m2 - m2*np.cos(2*theta1 - 2*theta2))
    alpha1 = alpha1_n / alpha1_d

    alpha2_n = 2*np.sin(theta1 - theta2) * (omega1**2 * l1 * (m1 + m2) + g*(m1 + m2) * np.cos(theta1) + omega2**2 * l2 * m2 * np.cos(theta1 - theta2))
    alpha2_d = l2 * (2*m1 + m2 - m2*np.cos(2*theta1 - 2*theta2))
    alpha2 = alpha2_n / alpha2_d

    return omega1, alpha1, omega2, alpha2


def system_double_simple_pendlum(t, y):
    theta1, omega1, theta2, omega2 = y

    omega1, alpha1, omega2, alpha2 = eqm_double_simple_pendulum(theta1, omega1, theta2, omega2)
    y_dot = [omega1, alpha1, omega2, alpha2]

    return y_dot
