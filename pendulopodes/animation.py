from collections import deque

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

from .dynamics import polar_to_inertial


def animate(*pendulums):
    """Plot an arbitrary number of pendulum elements over time.

    Each theta_array should be an array of angles (in radians) of a particular element over time.
    Currently this function assumes these angles have been spaced about 50ms apart by sampling.

    Returns the FunctionAnimation.
    """
    total_len = 0
    for pendulum in pendulums:
        total_len += pendulum[0]

    fig = plt.figure()
    ax = plt.axes(xlim=(-total_len, total_len), ylim=(-total_len, total_len))

    ax.set_aspect('equal', adjustable='box')

    element_count = len(pendulums)
    frame_count = len(pendulums[0][1])

    x_arrays = []
    y_arrays = []
    lines = []
    endpoints = deque(maxlen=10)

    for pendulum in pendulums:
        l, theta_array = pendulum
        lines += ax.plot([], [], lw=1)

        _x, _y = polar_to_inertial(l, theta_array)
        x_arrays.append(_x)
        y_arrays.append(_y)

    def init():  # setup function I think?
        for _line in lines:
            _line.set_data([], [])
        return lines

    def func(frame):  # function called to render each frame
        last = 0, 0
        trail = []

        for elem in range(element_count):
            y = [last[0], last[0] + y_arrays[elem][frame]]
            x = [last[1], last[1] + -x_arrays[elem][frame]]
            lines[elem].set_data(y, x)
            last = y[1], x[1]
            
            # last element = endpoint
            if elem == element_count - 1:
                endpoints.append(last)
                
                trail = []
                for p in range(len(endpoints) - 1):
                    line, = ax.plot([], [], "r", lw=1)
                    line.set_data([endpoints[p][0], endpoints[p+1][0]], [endpoints[p][1], endpoints[p+1][1]])
                    trail.append(line)
                    
        return lines + trail

    anim = FuncAnimation(fig, func, init_func=init, frames=frame_count, interval=50, blit=True)

    # return anim
    plt.show()
