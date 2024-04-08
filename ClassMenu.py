import tkinter as tk
from ClassEvent import xevents

class MainMenu(tk.Menu):
    def __init__(self, _parent):
        super().__init__()
        self.parent = _parent
        self.mainmenu = 0

    def set_default(self):
        self.mainmenu = tk.Menu(self, tearoff=0, borderwidth=1)
        self.parent.config(menu=self.mainmenu)

        filemenu = tk.Menu(self.mainmenu, tearoff=0, borderwidth=1)
        filemenu.add_command(label="Открыть...")
        filemenu.add_command(label="Сохранить...")
        filemenu.add_command(label="Выход", command=lambda: xevents.call_event("Application quit"))
        # filemenu.add_command(label="Выход", command=self.parent.exit)

        helpmenu = tk.Menu(self.mainmenu, tearoff=0, borderwidth=1)
        helpmenu.add_command(label="Помощь")
        helpmenu.add_command(label="О программе")

        self.mainmenu.add_cascade(label="Файл", menu=filemenu)
        self.mainmenu.add_cascade(label="Справка", menu=helpmenu)
