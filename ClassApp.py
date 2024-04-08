from ClassEvent import xevents
from ClassMainWindow import MainWindow


class Application:

    main_win = 0

    def __init__(self):
        self.__make_events()
        self.main_win = MainWindow()

    def __make_events(self):
        xevents.add_event("Application run", self.exec, 0)
        xevents.add_event("Application quit", self.on_quit, 0)

    def exec(self):
        self.main_win.run()

    def on_quit(self):
        self.main_win.destroy()
