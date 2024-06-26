from tkinter import ttk
# ----------------------------
from ClassEvent import xevents

class Tabs():
    
    def __init__(self, _parent) -> None:
        self.main_window_handle = None
        self.ntabs = 0
        self.tabs = []

        self.main_window_handle = _parent
        self.notebook = ttk.Notebook(self.main_window_handle)

    def __make_events(self) -> None:
        xevents.add_event("Tab add", self.add)
        xevents.add_event("Tab del", self.delete)
        
    def add(self, tab_name):
        _frame = ttk.Frame(self.notebook)
        _frame.rowconfigure(0, weight=1)
        _frame.columnconfigure(0, weight=1)
        _frame.pack(fill='both', expand=True)
        
        self.notebook.add(_frame, text=tab_name)
        self.notebook.pack(fill='both', expand=True)

        self.ntabs += 1
        self.tabs.append({self.ntabs, tab_name, _frame})

        return 'Вкладка ' + tab_name + ' добавлена'
    
    def place(self, index, source, object):
        pass

    def delete(self, target):
        pass
