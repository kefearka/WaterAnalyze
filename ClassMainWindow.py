import tkinter as tk
import tkinter.ttk as ttk
# ----------------------------
from ClassMenu import MainMenu
from ClassTabs import Tabs
from ClassData import FileConnector
from ClassEvent import xevents

class MainWindow(tk.Tk):

    def __init__(self):
        self.root_handle = None

        self.root_handle = super()
        self.root_handle.__init__()

        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.set_params()

        self.mmenu = MainMenu(self)

        self.tabs = Tabs(self)
        self.tabs.add("Таблица")
        self.tabs.add("График")

    def set_params(self, _title="Анализ воды", _window_params="650x650+450+250") -> None:
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.title(_title)
        self.geometry(_window_params)
        self.protocol('WM_DELETE_WINDOW', self.exit)

    def exit(self):
        self.destroy()

    def run(self):
        self.mainloop()

