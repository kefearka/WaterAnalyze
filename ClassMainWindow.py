import tkinter as tk
from tkinter import ttk
from matplotlib.pyplot import figure, show

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# -------------------------------------
from ClassMenu import MainMenu
from ClassGraph import ClassGraph


class MainWindow(tk.Tk):
    root_handle = 0

    def __init__(self):
        self.root_handle = super()
        self.root_handle.__init__()

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.title('Анализ воды')
        self.geometry("650x650+450+250")

        self.mmenu = MainMenu(self)
        self.mmenu.set_default()

        self.notebook = ttk.Notebook(self)

        self.table_frame = ttk.Frame(self.notebook)
        self.table_frame.rowconfigure(0, weight=1)
        self.table_frame.columnconfigure(0, weight=1)
        self.table_frame.pack(fill='both', expand=True)

        self.graph_frame = ttk.Frame(self.notebook)
        self.graph_frame.rowconfigure(0, weight=1)
        self.graph_frame.columnconfigure(0, weight=1)
        self.graph_frame.pack(fill='both', expand=True)

        self.notebook.add(self.table_frame, text="Таблица")
        self.notebook.add(self.graph_frame, text="График")

        # rect = 0.1, 0.1, 0.8, 0.8
        # t = np.arange(0.01, 10.0, 0.01)
        # scale = 1.10

        # fig = plt.Figure()

        # canvas = FigureCanvasTkAgg(fig, self.graph_frame)

        # ax1 = fig.add_axes(rect)
        # ax1.plot(t, np.exp(t), 'b-')  # Put your speed/power plot here
        # ax1.set_xlabel('Speed (mph)', color='b')
        # ax1.set_ylabel('Power', color='b')

        # ax2 = fig.add_axes(rect, frameon=False)
        # ax2.yaxis.tick_right()
        # ax2.yaxis.set_label_position('right')
        # ax2.xaxis.tick_top()
        # ax2.xaxis.set_label_position('top')

        # ax2.plot(t, np.sin(2 * np.pi * t), 'r-')  # Put your speed/rotation plot here
        # ax2.set_xlabel('Speed (kmph)', color='r')
        # ax2.set_ylabel('Rotations', color='r')

        # zp = ClassGraph()
        # figZoom = zp.zoom_factory(ax1, base_scale=scale)
        # figPan = zp.pan_factory(ax1)
        # figZoom2 = zp.zoom_factory(ax2, base_scale=scale)
        # figPan2 = zp.pan_factory(ax2)
        # canvas._tkcanvas.pack(fill=tk.BOTH, expand=1)

        self.notebook.pack(fill='both', expand=True)

        self.title('анализ')
        self.protocol('WM_DELETE_WINDOW', self.exit)

    def exit(self):
        self.destroy()

    def run(self):
        self.mainloop()
