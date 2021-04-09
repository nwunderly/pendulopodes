from scipy.integrate import solve_ivp

from .dynamics import NElementPendulum


TOLERANCE = 10**-13
FIRST_STEP = 0.01


def integrate(system, t_span, y0):
    soln = solve_ivp(system, t_span, y0, atol=TOLERANCE, rtol=TOLERANCE, first_step=FIRST_STEP)
    return soln.t, soln.y


# def solve_single_pendulum(t_span, theta0, omega0):
#     """Integrate the equation of motion for a single simple pendulum."""
#     y0 = [theta0, omega0]
#     t, y = integrate(system_single_simple_pendulum, t_span, y0)
#     theta, omega = y
#
#     return t, theta, omega
#
#
# def solve_double_pendulum(t_span, theta10, omega10, theta20, omega20):
#     """Integrate the equations of motion for a two-element simple pendulum system."""
#     y0 = [theta10, omega10, theta20, omega20]
#     t, y = integrate(system_double_simple_pendlum, t_span, y0)
#     theta1, omega1, theta2, omega2 = y
#
#     return t, theta1, omega1, theta2, omega2


def solve_single_pendulum_v2(t_span, l, m, theta0, omega0):
    """Integrate the equation of motion for a single simple pendulum."""
    y0 = [theta0, omega0]
    pendulum = NElementPendulum(1, length=[l], mass=[m], theta0=[theta0], omega0=[omega0])
    t, y = integrate(pendulum.system_single_simple_pendulum, t_span, y0)
    theta, omega = y

    return t, theta, omega


def solve_double_pendulum_v2(t_span, l1, m1, theta10, omega10, l2, m2, theta20, omega20):
    """Integrate the equations of motion for a two-element simple pendulum system."""
    y0 = [theta10, omega10, theta20, omega20]
    pendulum = NElementPendulum(2, length=[l1, l2], mass=[m1, m2], theta0=[theta10, theta20], omega0=[omega10, omega20])
    t, y = integrate(pendulum.system_double_simple_pendlum, t_span, y0)
    theta1, omega1, theta2, omega2 = y

    return t, theta1, omega1, theta2, omega2


def solve_n_element_pendulum(n, t_span, *initial_conditions):
    """Integrate the equations of motion for an n-element simple pendulum system."""
    pass
