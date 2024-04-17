import pandas as pd
# ----------------------------
from ClassEvent import xevents

class Table():
    def __make_events() -> None:
        pass

    def __init__(self, dataframe=None) -> None:
        if(dataframe):
            self.dataframe = dataframe
            self.ncols = self.dataframe.shape[0]
            self.nrows = self.dataframe.shape[1]
            self.column_names = self.dataframe.columns
        print(self.ncols, self.nrows)

    def add_row(self, index, value) -> None:
        pass

    def add_col(self, index, datatype, header="Новая колонка") -> None:
        pass
    
    def sort_by(self, col_indexes, sort_request) -> None:
        pass

    def mark_cell(self, col_index, row_index, format) -> None:
        pass

    def unmark_cell(self, col_index, row_index) -> None:
        pass

    def move(self, who, index_from, index_to) -> None:
        pass
