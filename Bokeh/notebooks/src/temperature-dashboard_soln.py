import pandas as pd
from bokeh.io import curdoc
from bokeh.charts import Histogram

df = pd.read_csv('../data/pittsburgh2013.csv')

plot = Histogram(df, values='Mean TemperatureF')

curdoc().add_root(plot)
