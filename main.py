import argparse

import numpy as np
from matplotlib import pyplot as plt

from pendulopodes.dynamics import polar_to_inertial
from pendulopodes.diffeq import solve_single_pendulum_v2, solve_double_pendulum_v2
from pendulopodes.animation import animate


T_SPAN = [0, 30]


def vector(s):
    """NOTE: NOT YET BEING USED"""
    return [float(n) for n in s.split(',')]


def parse():
    parser = argparse.ArgumentParser()

    # theta and omega
    parser.add_argument('--theta10', type=float, default=np.pi/2)
    parser.add_argument('--omega10', type=float, default=0)
    parser.add_argument('--theta20', type=float, default=np.pi/2)
    parser.add_argument('--omega20', type=float, default=0)

    parser.add_argument('--l1', type=float, default=1)
    parser.add_argument('--l2', type=float, default=1)
    parser.add_argument('--m1', type=float, default=1)
    parser.add_argument('--m2', type=float, default=1)

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


def sample(t, theta):
    path = []

    desired_time = 0
    step = 0.050

    for i, time in enumerate(t):
        if time >= desired_time:
            path.append(theta[i])
            desired_time += step

    return path


def main():
    args = parse()

    theta10 = args.theta10
    omega10 = args.omega10
    l1 = args.l1
    m1 = args.m1
    theta20 = args.theta20
    omega20 = args.omega20
    l2 = args.l2
    m2 = args.m2

    ###################
    # SINGLE PENDULUM #
    ###################
    # t, theta, omega = solve_single_pendulum(
    #     T_SPAN,
    #     theta0,
    #     omega0
    # )
    #
    # path = sample(t, theta)
    # # plot(theta)
    # animate(path)

    ###################
    # DOUBLE PENDULUM #
    ###################
    # t, theta1, omega1, theta2, omega2 = solve_double_pendulum(
    #     T_SPAN,
    #     theta10, omega10,  # l1, m1,
    #     theta20, omega20,  # l2, m2,
    # )
    #
    # path1 = sample(t, theta1)
    # path2 = sample(t, theta2)
    #
    # animate(path1, path2)

    ########################################
    # SINGLE PENDULUM CLASS IMPLEMENTATION #
    ########################################
    t, theta, omega = solve_single_pendulum_v2(
        T_SPAN,
        l1, m1,
        theta10,
        omega10
    )

    path = sample(t, theta)
    # plot(theta)
    animate((l1, path))

    ########################################
    # DOUBLE PENDULUM CLASS IMPLEMENTATION #
    ########################################
    t, theta1, omega1, theta2, omega2 = solve_double_pendulum_v2(
        T_SPAN,
        l1, m1, theta10, omega10,
        l2, m2, theta20, omega20,
    )

    path1 = (l1, sample(t, theta1))
    path2 = (l2, sample(t, theta2))

    animate(path1, path2)


if __name__ == '__main__':
    main()
