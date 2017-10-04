import pandas as pd
import numpy as np
from pandas_datareader import data
import datetime

from bokeh.plotting import Figure
from bokeh.models import ColumnDataSource, HBox, VBoxForm
from bokeh.models import # your favorite tools
from bokeh.models.widgets import # your favorite controls
from bokeh.io import curdoc


def get_stock_data(ticker, start='1990-1-1', end=datetime.date.today()):
    return data.DataReader(ticker, 'yahoo', start, end)


def compute_moving_averages(df, short, long):
    df['mav_short'] = df['Close'].rolling(window=short).mean()
    df['mav_long'] = df['Close'].rolling(window=long).mean()


def compute_signals(df):
    if 'mav_short' not in df:
        raise ValueError('moving average columns missing')

    def cross(x):
        short = x['mav_short']
        long = x['mav_long']
        if short > long:
            return 1
        else:
            return 0

    df['position'] = 0
    df['position'] = df.apply(cross, axis=1).diff()




# Step 1: input controls
## add TextInput and Sliders
## we want to modify:
##   ticker
##   start year
##   end year
##   long average window
##   short average window


# initialize the sources
source = ColumnDataSource(data=dict(date=[], price=[], mav_short=[], mav_long=[]))
buy  = ColumnDataSource(data=dict(x=[], y=[], price=[]))
sell = ColumnDataSource(data=dict(x=[], y=[], price=[]))


# Step 3: Plotting
## create plot object and plot lines and triangles
### plot price, mav_short and mav_long
### green triangle for buy
### red inverted_triangle for sell
### setup any tools you like

def get_data():
    # Step 4: re-compute
    # grab values from the control widgets
    # return the new data as a DataFrame
    pass

def update(attrname, old, new):
    df = get_data()

    source.data = dict(
            date = df.index,
            price = df['Close'],
            mav_short = df['mav_short'],
            mav_long = df['mav_long'],
    )

    buy_idx  = df['position'] ==  1
    sell_idx = df['position'] == -1

    buy.data = dict(
            x = df.loc[buy_idx].index,
            y = df.loc[buy_idx, 'mav_short'],
            price = df.loc[buy_idx, 'Close']
    )
    sell.data = dict(
            x = df.loc[sell_idx].index,
            y = df.loc[sell_idx, 'mav_short'],
            price = df.loc[sell_idx, 'Close']
    )


# Setp 5: register the controls
controls = # [your controls list]
for control in controls:
    control.on_change('value', update)

inputs = HBox(VBoxForm(*controls), width=300)

update(None, None, None)

curdoc().add_root(HBox(inputs, p, width=1100))
