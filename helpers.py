import pandas as pd


def make_sure_pd_index_timestamp(tseries):
    if not (type(tseries.first_valid_index()) == pd._libs.tslibs.timestamps.Timestamp):
        tseries.index = pd.to_datetime(tseries.index)
    return tseries
