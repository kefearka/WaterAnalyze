from tkinter import ttk

class ClassTabs():
    
    def __init__(self, _parent_window) -> None:
        self.main_window_handle = _parent_window
    
    def init_tab(self):
        self.notebook = ttk.Notebook(self.main_window_handle)
    
    def add_tab(self, tab_name):
        pass