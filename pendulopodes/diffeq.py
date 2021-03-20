from scipy.integrate import solve_ivp

from .dynamics import system_single_simple_pendulum, system_double_simple_pendlum


TOLERANCE = 10**-13


def ode45_single_pendulum(t_span, theta0, omega0):
    y0 = [theta0, omega0]
    soln = solve_ivp(system_single_simple_pendulum, t_span, y0, atol=TOLERANCE, rtol=TOLERANCE, first_step=0.0001)

    y = soln.y
    t = soln.t

    theta = y[0]
    omega = y[1]

    return t, theta, omega


def ode45_double_pendulum(t_span, theta10, omega10, theta20, omega20):
    y0 = [theta10, omega10, theta20, omega20]

    soln = solve_ivp(system_double_simple_pendlum, t_span, y0, atol=TOLERANCE, rtol=TOLERANCE, first_step=0.0001)

    y = soln.y
    t = soln.t

    theta10 = y[0]
    omega10 = y[1]
    theta20 = y[2]
    omega20 = y[3]

    return t, theta10, omega10, theta20, omega20
