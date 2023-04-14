import pandas as pd
import json

def make_sure_pd_index_timestamp(tseries):
    if not (type(tseries.first_valid_index()) == pd._libs.tslibs.timestamps.Timestamp):
        tseries.index = pd.to_datetime(tseries.index)
    return tseries

def load_dict_from_json(filename):
    data = json.load(open(filename,'r'))
    return data
