from scipy.integrate import solve_ivp

from .dynamics import system_single_simple_pendulum, system_double_simple_pendlum


TOLERANCE = 10**-13
FIRST_STEP = 0.0001


def integrate(system, t_span, y0):
    soln = solve_ivp(system, t_span, y0, atol=TOLERANCE, rtol=TOLERANCE, first_step=FIRST_STEP)
    return soln.t, soln.y


def solve_single_pendulum(t_span, theta0, omega0):
    """Integrate the equation of motion for a single simple pendulum."""
    y0 = [theta0, omega0]
    t, y = integrate(system_single_simple_pendulum, t_span, y0)
    theta, omega = y

    return t, theta, omega


def solve_double_pendulum(t_span, theta10, omega10, theta20, omega20):
    """Integrate the equations of motion for a two-element simple pendulum system."""
    y0 = [theta10, omega10, theta20, omega20]
    t, y = integrate(system_double_simple_pendlum, t_span, y0)
    theta1, omega1, theta2, omega2 = y

    return t, theta1, omega1, theta2, omega2


def solve_n_element_pendulum(n, t_span, *initial_conditions):
    """Integrate the equations of motion for an n-element simple pendulum system."""
    pass
