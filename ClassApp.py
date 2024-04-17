from ClassData import FileConnector, DBConnector, DataTransfer
from ClassEvent import xevents
from ClassGraph import Graph
from ClassMainWindow import MainWindow
from ClassMenu import MainMenu
from ClassTable import Table
from ClassTabs import Tabs

class Application:
    
    def __init__(self):
        self.file_connector = FileConnector()
        self.graph = Graph()
        self.main_win = MainWindow()
        self.menu = MainMenu(self.main_win)
        self.table = Table()
        self.tabs = Tabs()
        
        self.__make_events()

    def __make_events(self):
        xevents.add_event("Application run", self.exec)
        xevents.add_event("Application quit", self.on_quit)

    def exec(self):
        self.main_win.run()

    def on_quit(self):
        self.main_win.destroy()
