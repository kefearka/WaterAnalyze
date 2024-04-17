from tkinter import ttk
from ClassEvent import xevents

class Tabs():
    
    def __init__(self, _parent_window) -> None:
        self.main_window_handle = _parent_window

        self.init_tab()

        xevents.add_event("Tab add", self.add, 1)
        xevents.add_event("Tab del", self.delete, 0)
    
    def init_tab(self):
        self.notebook = ttk.Notebook(self.main_window_handle)
    
    def add(self, tab_name):
        self._frame = ttk.Frame(self.notebook)
        self._frame.rowconfigure(0, weight=1)
        self._frame.columnconfigure(0, weight=1)
        self._frame.pack(fill='both', expand=True)
        self.notebook.add(self._frame, text=tab_name)
        self.notebook.pack(fill='both', expand=True)

    def delete(self):
        self.notebook.forget(self.notebook.select())
    
    def place():
        pass