# !/usr/bin/python
#  -*- coding: utf-8 -*
from threading import Thread

import matplotlib
import random
import threading

import time

from Views.Temperature import Temperature

matplotlib.use('TkAgg')

import sys

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk


def destroy(e):
    sys.exit()


views = []
root = Tk.Tk()


def print_plot():
    step = random.uniform(0, 1)
    print step
    for view in views:
        view.update_data(step)


def task():
    print_plot()
    root.update()
    root.after(2000, task)


def main():
    #root = Tk.Tk()
    root.wm_attributes("-fullscreen", True)
    root.wm_title(u'Параметры процесса')

    view_params = [(u'Агитатор', root), (u'Декомпозер #1', root), (u'Декомпозер #2', root),
                   (u'Бак оборотного расствора', root)]
    for param in view_params:
        view = Temperature(param)
        views.append(view)

    for view in views:
        view.update_data(0)
        view.show()

    #t1 = threading.Thread(target=print_plot)
    #t1.start()

    root.after(2000, task)
    root.mainloop()


if __name__ == '__main__':
    main()