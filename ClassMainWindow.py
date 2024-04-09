import tkinter as tk
from tkinter import ttk
from ClassMenu import MainMenu
from ClassEvent import xevents


class MainWindow(tk.Tk):

    def __init__(self):
        self.root_handle = 0

        self.root_handle = super()
        self.root_handle.__init__()

        self.configure()

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

        self.notebook.pack(fill='both', expand=True)

    def configure(self, _title="Анализ воды", _window_params="650x650+450+250") -> None:
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.title(_title)
        self.geometry(_window_params)
        self.protocol('WM_DELETE_WINDOW', self.exit)

    def exit(self):
        self.destroy()

    def run(self):
        self.mainloop()
