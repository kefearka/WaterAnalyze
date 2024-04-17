import pandas as pd

class DataTransfer():
    
    pass

class FileConnector():
    def __init__(self, path) -> None:
        self.file_path = path

    def get(self) -> object:
        self.dataframe = pd.read_excel(self.file_path)

class DBConnector():
    pass