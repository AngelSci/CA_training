import pandas as pd
from urllib.request import urlopen
from bokeh.plotting import Figure
from bokeh.models import ColumnDataSource, VBox
from bokeh.models.widgets import TextInput
from bokeh.io import curdoc
from bokeh.driving import count


# 1. Initialize ColumnDataSource and plot for price and date

def update(attrname, old, new):
# 2. update plot title with new ticker value
# 3. re-initialize ColumnDataSource object

ticker_input = TextInput(title='Ticker name (Google)', value='AAPL')
ticker_input.on_change('value', update)


URL = 'http://finance.google.com/finance/info?client=ig'

def update_price():
# 4. Get ticker value
# 5. Retrieve new date and price from the URL
#    into a dictionary
# 6. Call source.stream() with the new dictionary




curdoc().add_root(VBox(ticker_input, p))
update(None, None, None)
curdoc().add_periodic_callback(update_price, 5000)
