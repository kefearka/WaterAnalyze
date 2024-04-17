import pandas as pd

class DataTransfer():
    def __init__(self) -> None:
        pass

class FileConnector():

    def __init__(self) -> None:
        self.file_path = None
        self.dataframe = None

    def get(self, path) -> object:
        self.file_path = path
        self.dataframe = pd.read_excel(self.file_path)
        return self.dataframe

class DBConnector():
    def __init__(self) -> None:
        pass