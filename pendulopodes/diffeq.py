from scipy.integrate import solve_ivp


TOLERANCE = 10**-13


def ode45_single_pendulum(system, t_span, theta0, theta_dot0):
    y0 = [theta0, theta_dot0]
    soln = solve_ivp(system, t_span, y0, atol=TOLERANCE, rtol=TOLERANCE, first_step=0.0001)

    y = soln.y
    t = soln.t

    theta = y[0]
    theta_dot = y[1]

    return t, theta, theta_dot
