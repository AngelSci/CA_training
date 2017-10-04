'''
To run the bokeh server - spark streaming example:

hdfs dfs -mkdir /taxidata
rm temp*
hdfs dfs -rm /taxidata/*
bokeh serve dashboard.py --port 8081 --host 52.207.239.46:8081
./bin/spark-submit taxi_stream.py /taxidata

'''
from multiprocessing.connection import Listener
from threading import Thread

from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.models import HBox, VBox, Paragraph
from bokeh.plotting import Figure
from bokeh.tile_providers import STAMEN_TONER

pickup_source = ColumnDataSource(data=dict(x=[], y=[], fare=[], date=[]))
dropoff_source = ColumnDataSource(data=dict(x=[], y=[], fare=[], date=[]))
new_data = data_dirty = None

password = b'secret password'

def listen():
    global new_data, data_dirty
    listener = Listener(('localhost', 6000), authkey=password)
    conn = listener.accept()
    while True:
        new_data = conn.recv()
        data_dirty = True

revenue = 0
pickup_count = 0
dropoff_count = 0
def update_data():
    global data_dirty, revenue, pickup_count, dropoff_count
    if data_dirty and new_data:

        if new_data['pickups']:
            pickup_count += len(new_data['pickups']['x'])
            pickup_source.stream(new_data['pickups'], 150)

        if new_data['dropoffs']:
            dropoff_count += len(new_data['dropoffs']['x'])
            revenue += sum([f for f in new_data['dropoffs']['fare'] if f])
            dropoff_source.stream(new_data['dropoffs'], 150)

        data_dirty = False
        update_info()

def update_info():
    global revenue, pickup_count, dropoff_count
    global revenue_text, pickup_text, dropoff_text

    revenue_text.text = 'Revenue: ${:,}'.format(revenue)
    pickup_text.text = 'Pickups: {:,}'.format(pickup_count)
    dropoff_text.text = 'Dropoffs: {:,}'.format(dropoff_count)

# listen from messages from Spark
t = Thread(target=listen)
t.daemon = True
t.start()

# Create plot -------------------------------
xmin = -8240227.037
ymin = 4974203.152
xmax = -8231283.905
ymax = 4979238.441

fig = Figure(x_range=(xmin, xmax),
             y_range=(ymin, ymax),
             plot_height=600,
             plot_width=900,
             tools='pan,wheel_zoom')


fig.add_tile(STAMEN_TONER, alpha=.3)
fig.axis.visible = False
fig.grid.grid_line_alpha = 0
fig.min_border_left = 0
fig.min_border_right = 0
fig.min_border_top = 0
fig.min_border_bottom = 0

fig.background_fill_color = 'black'
fig.legend.location = 'bottom_left'
fig.legend.label_text_color = 'white'
fig.legend.background_fill_alpha = 0

fig.circle(source=pickup_source,
           x='x', y='y',
           color='#F3F315',
           line_color='lightyellow',
           line_width=1,
           legend='Pickup Location',
           alpha=.85)

fig.circle(source=dropoff_source,
           x='x',
           y='y',
           color='#05E9FF',
           line_color='lightblue',
           line_width=1,
           legend='Dropoff Location',
           alpha=.5)

revenue_text = Paragraph(text='Revenue: ')
pickup_text = Paragraph(text='Pickups: ')
dropoff_text = Paragraph(text='Dropoffs: ')

info = VBox(children=[revenue_text, pickup_text, dropoff_text], width=200)

layout = HBox(children=[fig, info])

# setup bokeh server document
curdoc().add_root(layout)
curdoc().add_periodic_callback(update_data, 100)
