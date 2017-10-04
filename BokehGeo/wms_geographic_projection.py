import pdb
import requests
import json

from bokeh.io import show, output_file
from bokeh.models import Range1d, HBox, VBox
from bokeh.plotting import Figure

from bokeh.models import GeoJSONDataSource, VBox, Select
from bokeh.models import TapTool, CustomJS, WheelZoomTool, PanTool

from bokeh_geo.sources import WMSImageSource

# create figure
p = Figure(tools='wheel_zoom,pan,tap',
           plot_width=800, 
           plot_height=450, 
           title='WMS Geographic Projection')

# style figure
p.x_range = Range1d(start=-180, end=180, bounds=(-180, 180))
p.y_range = Range1d(start=-90, end=90, bounds=(-90, 90))
p.background_fill_color = "black"
p.grid.grid_line_alpha = 0
p.min_border_top = 30
p.min_border_right = 0
p.min_border_bottom = 0
p.min_border_left = -10

# add wms image layer
service_endpoint = 'http://demo.opengeo.org/geoserver/wms'
image_source = WMSImageSource(url=service_endpoint,
                              layers='ne:ne',
                              f='image/png',
                              crs='EPSG:4326')

p.add_dynamic_image(image_source)

# setup tap tool
output_file("wms_plate_carree.html")
show(p)
