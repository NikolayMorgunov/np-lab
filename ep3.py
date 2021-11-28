import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def init():
    line.set_data([], [])
    return line,


def animate(i):
    global x, all_U
    y = all_U[i][0]
    line.set_data(x, y)
    return line,


u = np.array([np.genfromtxt('func_u_start.txt',  delimiter="\n")])

x = np.arange(u[0].size)

fig = plt.figure()
ax = plt.axes(xlim=(min(x), max(x)), ylim=(min(u[0]), max(u[0])))
line, = ax.plot([], [], lw=3)

A = np.eye(u[0].size)
B = -np.roll(A, -1, axis=1)
A = A + B

all_U = []
for _ in range(256):
    all_U.append(u)
    u = u - 0.5 * np.dot(A, u.transpose()).transpose()

anim = FuncAnimation(fig, animate, init_func=init,
                     frames=200, interval=50, blit=True)
ax.minorticks_on()
ax.grid(which='major',
        color='k',
        linewidth=1)
ax.grid(which='minor',
        color='grey',
        linestyle=':')

# anim.save('func_animation.gif', writer='imagemagick', fps=30)

plt.show()
