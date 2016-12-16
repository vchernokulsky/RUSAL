# !/usr/bin/python
#  -*- coding: utf-8 -*

import Tkinter

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import rc


class Temperature:
    def __init__(self, param):
        self.__name = param[0]
        self.__root = param[1]
        # prepare matplotlib objects
        font = {'family': 'Verdana', 'weight': 'normal'}
        rc('font', **font)
        self.__figure = None
        self.__plot = None
        self.__prepare_figures()

    def __prepare_figures(self):
        self.__figure = Figure(figsize=(3, 2), dpi=100)
        self.__figure.suptitle(self.__name)
        self.__figure.subplots_adjust(top=0.85, bottom=0.3)
        # subplot customize
        self.__plot = self.__figure.add_subplot(111)
        self.__plot.set_xlabel(u'время')
        self.__plot.set_ylabel(u'температура')

    def show(self):
        canvas = FigureCanvasTkAgg(self.__figure, master=self.__root)
        canvas.get_tk_widget().pack(fill=Tkinter.X)
        canvas.show()

    def update_data(self, step):
        #self.__figure.clear()
        #self.__prepare_figures()
        #canvas = FigureCanvasTkAgg(self.__figure, master=self.__root)
        #canvas.get_tk_widget().destroy()
        #canvas.get_tk_widget().delete("all")
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t + step)
        self.__plot.plot(t, s)
