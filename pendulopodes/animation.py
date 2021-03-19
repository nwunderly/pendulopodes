import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


from .dynamics import polar_to_inertial


def animate(theta):
    """Plot the path of a point over time."""

    fig = plt.figure()
    ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
    line, = ax.plot([], [], lw=1)
    ax.set_aspect('equal', adjustable='box')

    frame_count = len(theta)
    x, y = polar_to_inertial(1, theta)

    def init():
        line.set_data([], [])
        return line,

    def callback(i):
        line.set_data([0, y[i]], [0, -x[i]])
        return line,

    anim = FuncAnimation(fig, callback, init_func=init, frames=frame_count, interval=0.050, blit=True)
    plt.show()
