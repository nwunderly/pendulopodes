from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from .dynamics import polar_to_inertial


def animate(*theta_arrays):
    """Plot an arbitrary number of pendulum elements over time.

    Each theta_array should be an array of angles (in radians) of a particular element over time.
    Currently this function assumes these angles have been spaced about 50ms apart by sampling.

    Returns the FunctionAnimation.
    """
    fig = plt.figure()
    ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))

    ax.set_aspect('equal', adjustable='box')

    element_count = len(theta_arrays)
    frame_count = len(theta_arrays[0])

    x_arrays = []
    y_arrays = []
    lines = []

    for theta_array in theta_arrays:
        lines += ax.plot([], [], lw=1)

        _x, _y = polar_to_inertial(1, theta_array)
        x_arrays.append(_x)
        y_arrays.append(_y)

    def init():  # setup function I think?
        for _line in lines:
            _line.set_data([], [])
        return lines

    def func(frame):  # function called to render each frame
        last = 0, 0

        for elem in range(element_count):
            y = [last[0], last[0] + y_arrays[elem][frame]]
            x = [last[1], last[1] + -x_arrays[elem][frame]]
            lines[elem].set_data(y, x)
            last = y[1], x[1]

        return lines

    anim = FuncAnimation(fig, func, init_func=init, frames=frame_count, interval=50, blit=True)

    # return anim
    plt.show()
