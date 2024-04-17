import pandas as pd
from ClassEvent import xevents


class Table():
    def __make_events():
        pass
    
    def __init__(self, dataframe=None) -> None:
        if(dataframe):
            self.dataframe = dataframe
            self.ncols = 0
            self.nrows = 0
            self.column_names = None

    def add_row(self, index, value):
        pass

    def add_col(self, index, datatype, header="Новая колонка"):
        pass
    
    def sort_by(self, col_indexes, sort_request):
        pass

    def mark_cell(self, col_index, row_index, format):
        pass

    def unmark_cell(self, col_index, row_index):
        pass

    def move(self, who, index_from, index_to):
        pass
