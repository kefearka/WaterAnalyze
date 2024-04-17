import tkinter as tk
from ClassMenu import MainMenu
from ClassTabs import Tabs
from ClassEvent import xevents

class MainWindow(tk.Tk):

    def __init__(self):
        self.root_handle = 0

        self.root_handle = super()
        self.root_handle.__init__()

        self.set_params()

        self.mmenu = MainMenu(self)
        self.mmenu.set_default()

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
