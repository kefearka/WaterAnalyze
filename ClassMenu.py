import tkinter as tk
# ----------------------------
from ClassEvent import xevents

class MainMenu(tk.Menu):
    def __init__(self, _parent):
        
        super().__init__()
        self.parent = _parent
        self.mainmenu = None

        self.set_default()

    def set_default(self):
        self.mainmenu = tk.Menu(self)
        self.parent.config(menu=self.mainmenu)

        filemenu = tk.Menu(self.mainmenu, tearoff=False, border=1)
        filemenu.add_command(label="Открыть файл с данными")
        filemenu.add_command(label="Подключиться к базе")
        filemenu.add_command(label="Выход", command=lambda: xevents.call_event("Application quit"))

        helpmenu = tk.Menu(self.mainmenu, tearoff=False, border=1)
        helpmenu.add_command(label="Помощь")
        helpmenu.add_command(label="О программе")

        self.mainmenu.add_cascade(label="Файл", menu=filemenu)
        self.mainmenu.add_cascade(label="Справка", menu=helpmenu)
        