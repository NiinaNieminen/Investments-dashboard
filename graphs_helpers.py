import panel as pn
import pandas as pd
from datetime import datetime

# Start from minimum date
def get_starting_point(timeseries1,timeseries2):
    return min(timeseries1.notna().idxmax().min(),timeseries2.notna().idxmax().min())   

def get_range(piirra_sarjat,piirra_flows,tic):
    '''Limit to time periods when there is data'''
    d0 = piirra_flows[[tic+ ' cumflows_eur']]
    d0 = d0.loc[d0[tic + ' cumflows_eur'] != 0]
    d1 = piirra_sarjat[[tic + ' value_eur']]
    d1 = d1.loc[d1[tic + ' value_eur'] != 0]
    
    # Find first date when either one has data
    start = get_starting_point(d0,d1)
    d0 = d0.loc[start:,:]
    d1 = d1.loc[start:,:]
    return d0,d1

def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    if type(val) in [float,int]:
        color = 'red' if val < 0 else 'black'
        return 'color: %s' % color
    else:
        pass

def highlight_max(s):
    '''
    Highlight the maximum in a Series twith selected color.
    '''
    # Leave non numbers out
    include = ['Market value', 'Return eur',
               '3m P/A %', '6m P/A %', '1y P/A %', '3y P/A %', '5y P/A %', '10y P/A %',
               'max P/A %', 'Costs % per year', 'Costs eur']
    if s.name in include:
        is_max = s == s.max()
        return ['background-color: #cccccc' if v else '' for v in is_max ]
    else:
        return ['' for x in range(len(s))]
    
