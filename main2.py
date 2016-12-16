import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time


def generate_y(t):
    rand = random.uniform(1, 10)
    rand_deg = random.uniform(5, 10)
    y = np.sin(2 * np.pi * t) * np.exp(- (rand_deg/10)/ rand)
    return y

def read_data_y(ind):
    filename = "y" + str(ind) + ".rtf"
    f = open(filename)
    last_line = f.readlines()[-1]
    f.close()
    y = float(last_line)
    return y


def data_gen():
    t = data_gen.t
    cnt = 0
    while cnt < 5000:
        cnt += 1
        t += 0.05
        #y1 = np.sin(2*np.pi*t) * np.exp(-t/random.uniform(1, 10))
        #y = [generate_y(t), generate_y(t), generate_y(t), generate_y(t), generate_y(t), generate_y(t)]
        y = [read_data_y(1), read_data_y(2), read_data_y(3), read_data_y(4), read_data_y(5), read_data_y(6)]
        print t, ": ", y
        # adapted the data generator to yield both sin and cos
        yield t, y
        time.sleep(1.0)
data_gen.t = 0


# the same axes initalizations as before (just now we do it for both of them)
def init():
    for ax in ax_array:
        #ax.set_ylim(-1.1, 1.1)
        ax.set_xlim(0, 5)
        ax.grid()
    del xdata[:]
    for y in y_data:
        del y[:]
    # init the data of both line objects
    n = min(len(line),len(y_data))
    for i in range(n):
        line[i].set_data(xdata, y_data[i])
    return line,


# create a figure with two subplots
#fig, ax_array = plt.subplots(3,2)
fig = plt.figure()
ax1 = fig.add_subplot(3, 2, 1)
ax1.title.set_text('Plot 1')
ax2 = fig.add_subplot(3, 2, 2)
ax2.title.set_text('Plot 2')
ax3 = fig.add_subplot(3, 2, 3)
ax3.title.set_text('Plot 3')
ax4 = fig.add_subplot(3, 2, 4)
ax4.title.set_text('Plot 4')
ax5 = fig.add_subplot(3, 2, 5)
ax5.title.set_text('Plot 5')
ax6 = fig.add_subplot(3, 2, 6)
ax6.title.set_text('Plot 6')
ax_array = [ax1, ax2, ax3, ax4, ax5, ax6]


# intialize ALL lines objects (one in each axes)
line = [0 for i in range(6)]
n = min(len(line),len(ax_array))
colors = [(0.3, 0.3, 0.3), (0.3, 0.7, 0.3), (0.6, 0.3, 0.6),
          (0.2, 0.9, 0.6), (0.8, 0.6, 0.3), (0.9, 0.2, 0.7)]
for i in range(n):
    line[i], = ax_array[i].plot([], [], lw=2, color=colors[i])

# initialize the data arrays
xdata, y1data, y2data, y3data, y4data, y5data, y6data = [], [], [], [], [], [], []

y_data = [y1data, y2data, y3data, y4data, y5data, y6data]


def run(data):
    # update the data
    t, y_array = data
    xdata.append(t)
    n = min(len(y_array), len(y_data))
    for i in range(n):
        y_data[i].append(y_array[i])


    # axis limits checking. Same as before, just for both axes
    for ax in ax_array:
        xmin, xmax = ax.get_xlim()
        if t >= xmax:
            ax.set_xlim(xmin+(xmax-xmin)/2, xmax+(xmax-xmin)/2)
            ax.figure.canvas.draw()

    # update the data of both line objects
    n = min(len(line), len(y_data))
    for i in range(n):
        line[i].set_data(xdata, y_data[i])
        ax_array[i].set_ylim(min(y_data[i]) - 0.1, max(y_data[i]) + 0.1)
    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,repeat=False, init_func=init)
plt.show()
