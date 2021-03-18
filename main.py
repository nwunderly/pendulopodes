import argparse

import numpy as np
from matplotlib import pyplot as plt

from pendulopodes.dynamics import system_single_simple_pendulum, polar_to_inertial
from pendulopodes.diffeq import ode45_single_pendulum


T_SPAN = [0, 100]


def vector(s):
    """NOTE: NOT YET BEING USED"""
    return [float(n) for n in s.split(',')]


def parse():
    parser = argparse.ArgumentParser()

    # theta and theta_dot
    parser.add_argument('--theta0', type=float, default=np.pi/2)
    parser.add_argument('--thetadot0', type=float, default=0)

    return parser.parse_args()


def plot(theta):
    fig = plt.figure()
    ax = fig.add_subplot(111, title="Pendulum path")

    x, y = polar_to_inertial(1, theta)

    ax.plot(y, -x)
    ax.plot(0, 0, 'ro')

    plt.show()


def main():
    args = parse()

    theta0 = args.theta0
    theta_dot0 = args.thetadot0

    t, theta, theta_dot = ode45_single_pendulum(
        system_single_simple_pendulum,
        T_SPAN,
        theta0,
        theta_dot0
    )

    plot(theta)


if __name__ == '__main__':
    main()
