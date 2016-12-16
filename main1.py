import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import time


"""

fig, ax = plt.subplots()
ax.grid()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i/10.0))  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init, interval=25, blit=False)
plt.show()
"""


def generate_y(t):
    rand = random.uniform(1, 10)
    rand_deg = random.uniform(5, 10)
    y = np.sin(2 * np.pi * t) * np.exp(- (rand_deg/10)/ rand)
    return y

def main():
    MESSAGE = b'\x02\x30\x33\x30\x30\x30\x30\x31\x30\x31\x43\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x31\x03\x42'
    print MESSAGE[1]
"""
    f = [0 for i in range(6)]
    values = [0 for i in range(6)]
    t = 0
    cnt = 0
    for i in range(6):
        filename = "y" + str(i + 1) + ".rtf"
        try:
            f[i] = open(filename, 'w')
            f[i].close()
        except IOError:
            print ("No file")

    while cnt < 5000:
        cnt += 1
        t += 0.05
        for i in range(6):
            filename = "y"+str(i+1)+".rtf"
            try:
                f[i] = open(filename, 'a')
                int_to_write = generate_y(t)
                str_to_wtite = str(int_to_write)
                values[i] = int_to_write
                f[i].write(str(str_to_wtite)+"\n")
                f[i].close()
            except IOError:
                print ("No file")
        print t, ": ", values
        time.sleep(1)
"""

if __name__ == '__main__':
    main()