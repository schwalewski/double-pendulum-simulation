import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from simulation import x1, y1, x2, y2, th


fig, ax = plt.subplots()


ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-2.5, 0.5)

line, = ax.plot([], [], 'o-', lw=2)

def update(i):
    line.set_data([0, x1[i], x2[i]], [0, y1[i], y2[i]])
    return line,

anim = FuncAnimation(fig, update, frames=len(th), interval=20)

plt.show()
