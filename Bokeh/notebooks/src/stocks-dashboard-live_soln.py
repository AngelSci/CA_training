import pandas as pd
from urllib.request import urlopen
from bokeh.plotting import Figure
from bokeh.models import ColumnDataSource, VBox
from bokeh.models.widgets import TextInput
from bokeh.io import curdoc
from bokeh.driving import count



source = ColumnDataSource(data=dict(date=[], price=[]))

p = Figure(plot_height=600, plot_width=800, title="", x_axis_type='datetime')
p.line(x='date', y='price', alpha=0.3, color='Black', line_width=2, source=source)
p.yaxis.axis_label='Price'
p.title.text = 'AAPL'

def update(attrname, old, new):
    p.title.text = ticker_input.value

    source.data = dict(date=[], price=[])


ticker_input = TextInput(title='Ticker name (Google)', value='AAPL')
ticker_input.on_change('value', update)


URL = 'http://finance.google.com/finance/info?client=ig'

def update_price():
    ticker = ticker_input.value

    data = urlopen(URL+'&q='+ticker).read().decode('utf-8')
    df = pd.read_json(data[3:])
    df['lt_dts'] = pd.to_datetime(df['lt_dts'])

    new_source = dict(
            date = df['lt_dts'].tolist(),
            price = df['l'].tolist()
    )

    source.stream(new_source)




curdoc().add_root(VBox(ticker_input, p))
update(None, None, None)
curdoc().add_periodic_callback(update_price, 5000)
