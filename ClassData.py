import pandas as pd
import os
# ----------------------------
from ClassEvent import xevents

class DataTransfer():
    def __init__(self) -> None:
        pass

class FileConnector():

    def __make_events(self) -> None:
        xevents.add_event("get data from file", self.read)
        xevents.add_event("save data to file", self.write)

    def __init__(self) -> None:
        self.file_path = None
        self.dataframe = None

        self.__make_events()

    def read(self, path, delimeter='/t') -> object:
        filename, fileext = os.path.splitext(path)
        match fileext:
            case '.txt':
                self.dataframe = pd.read_fwf(self.file_path, delimeter=delimeter)
            case '.csv':
                self.dataframe = pd.read_csv(self.file_path)
            case '.xlsx':
                self.dataframe = pd.read_excel(self.file_path)
            case '.xls':
                self.dataframe = pd.read_excel(self.file_path)
            case _:
                print('U R masta! U`r keep wrong file')
        self.file_path = path
        return self.dataframe

    def write(self, path) -> bool:
        return True
        
class DBConnector():
    def __init__(self) -> None:
        pass