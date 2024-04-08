from ClassEvent import xevents
from ClassMainWindow import MainWindow


class Application:

    main_win = 0

    def __init__(self):
        xevents.add_event("Application run", self.exec, 0)
        xevents.add_event("Application quit", self.on_quit, 0)
        print()
        self.main_win = MainWindow()

    def exec(self):
        self.main_win.run()

    def on_quit(self):
        self.main_win.destroy()
