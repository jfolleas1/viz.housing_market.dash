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

    @lru_cache(maxsize=10)
    def get_selection(self, filtering_dict):
        filtering_dict
        return self.get()

    @lru_cache(maxsize=10)
    def get_unique_values(self, column_name):
        return list(self.get()[column_name].unique())
    
    @lru_cache(maxsize=10)
    def get_aggregate(self, column_name, agg_function):
        return agg_function(self.get()[column_name])