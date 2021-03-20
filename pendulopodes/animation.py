from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from .dynamics import polar_to_inertial


# def animate(theta):
#     """Plot the path of a point over time."""
#
#     fig = plt.figure()
#     ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
#     line, = ax.plot([], [], lw=1)
#     ax.set_aspect('equal', adjustable='box')
#
#     frame_count = len(theta)
#     x, y = polar_to_inertial(1, theta)
#
#     def init():
#         line.set_data([], [])
#         return line,
#
#     def callback(i):
#         line.set_data([0, y[i]], [0, -x[i]])
#         return line,
#
#     anim = FuncAnimation(fig, callback, init_func=init, frames=frame_count, interval=50, blit=True)
#     plt.show()


def animate(*theta_arrays):
    """Plot an arbitrary number of pendulum components over time."""

    fig = plt.figure()
    ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))

    ax.set_aspect('equal', adjustable='box')

    component_count = len(theta_arrays)
    frame_count = len(theta_arrays[0])

    x_arrays = []
    y_arrays = []
    lines = []

    for theta_array in theta_arrays:
        lines += ax.plot([], [], lw=1)

        _x, _y = polar_to_inertial(1, theta_array)
        x_arrays.append(_x)
        y_arrays.append(_y)

    def init():
        for _line in lines:
            _line.set_data([], [])
        return lines

    def callback(t):
        last = 0, 0

        for i in range(component_count):
            y = [last[0], last[0] + y_arrays[i][t]]
            x = [last[1], last[1] + -x_arrays[i][t]]
            lines[i].set_data(y, x)
            last = y[1], x[1]

        return lines

    anim = FuncAnimation(fig, callback, init_func=init, frames=frame_count, interval=50, blit=True)
    plt.show()
