import argparse

import numpy as np
from matplotlib import pyplot as plt

from pendulopodes.dynamics import system_single_simple_pendulum, polar_to_inertial
from pendulopodes.diffeq import ode45_single_pendulum


T_SPAN = [0, 1]


def vector(s):
    """NOTE: NOT YET BEING USED"""
    return [float(n) for n in s.split(',')]


def parse():
    parser = argparse.ArgumentParser()

    # theta and theta_dot
    parser.add_argument('--theta0', type=float, default=np.pi/2)
    parser.add_argument('--thetadot0', type=float, default=0)

    return parser.parse_args()


def gradient_for(count):
    cmap = plt.get_cmap('rainbow')
    step = 1.0/count

    # invert the color list so it's red -> purple, might change later
    return [cmap(0 + i*step) for i in range(count)][::-1]


def plot(theta):
    # use every other point to show spacing more clearly
    theta = theta[::2]

    fig = plt.figure()
    ax = fig.add_subplot(111, title="Pendulum path")
    ax.axis('equal')

    x, y = polar_to_inertial(1, theta)

    # origin
    ax.plot(0, 0, 'ro')

    n_points = len(theta)
    grad = gradient_for(n_points)

    # plot path
    for i in range(n_points):
        ax.plot(y[i], -x[i], color=grad[i], marker='+')


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
