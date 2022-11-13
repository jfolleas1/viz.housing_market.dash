import config as cfg
from functools import lru_cache
import pandas as pd


class Dataset(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Dataset, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.__data = pd.read_csv(cfg.DATA_LOCATION)

    def get(self):
        return self.__data

    @staticmethod
    def apply_filters(initial_data, filters):
        filtered_data = initial_data.copy()
        for col, op, val in filters:
            if op == '<=':
                filtered_data = filtered_data[filtered_data[col] <= val]
            elif op == '>=':
                filtered_data = filtered_data[filtered_data[col] >= val]
            elif op == 'in':
                filtered_data = filtered_data[filtered_data[col].isin(val)]
        return filtered_data

    def get_selection(self, filters_list):
        selection  = self.apply_filters(self.get(), filters_list)
        return selection

    @lru_cache(maxsize=10)
    def get_unique_values(self, column_name):
        return list(self.get()[column_name].unique())
    
    @lru_cache(maxsize=10)
    def get_aggregate(self, column_name, agg_function):
        return agg_function(self.get()[column_name])