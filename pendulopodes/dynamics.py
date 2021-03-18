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
"""


def inertial_to_polar(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.atan(y/x)

    return r, theta


def polar_to_inertial(r, theta):
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    return x, y


def eqm_single_simple_pendulum(theta, theta_dot):
    """Single-part simple pendulum equation of motion.

    tension = m*g*cos(theta)+m*l*theta
    theta_dot_dot = -g/l*sin(theta
    """
    theta_dot_dot = -g*np.sin(theta)

    return theta_dot, theta_dot_dot


def system_single_simple_pendulum(t, y):
    """Single-part simple pendulum system of differential equations, in vector form.

    y = [theta, theta_dot]
    y_dot = [theta_dot, theta_dot_dot]
    """
    theta, theta_dot = y

    theta_dot, theta_dot_dot = eqm_single_simple_pendulum(theta, theta_dot)
    y_dot = [theta_dot, theta_dot_dot]

    return y_dot


def single_compound_pendulum_eqm(theta, theta_dot):
    """Single-part compound pendulum equation of motion."""
    pass



