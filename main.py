# ----------------------------
from ClassApp import Application

""" Версия программы """
__version__ = "0.0.1"

if __name__ == '__main__':

    print("Program version: " + __version__)
    app = Application()
    app.exec()
