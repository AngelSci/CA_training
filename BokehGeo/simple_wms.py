from bokeh.models import Range1d
from bokeh.plotting import figure, output_file, show
from bokeh.tile_providers import STAMEN_TONER

from bokeh_geo.sources import WMSImageSource

title = 'WMS Map: US States'
p = figure(tools='wheel_zoom,pan', title=title, plot_height=500, plot_width=800)
p.x_range = Range1d(start=-15473429, end=2108550, bounds=None)
p.y_range = Range1d(start=-6315661, end=7264686, bounds=None)
p.background_fill_color = "black"
p.axis.visible = False

# National Land Cover Dataset (http://www.mrlc.gov/nlcd2011.php)
service_url = (
    "http://demo.boundlessgeo.com/geoserver/wms"
)
layers = 'topp:states'
styles = ''
crs = 'EPSG:3857'
image_source = WMSImageSource(url=service_url,
                              layers=layers,
                              styles=styles,
                              f='image/png',
                              transparent=True,
                              crs=crs)
image_source.validate()

p.add_tile(STAMEN_TONER)
p.add_dynamic_image(image_source)

output_file('simple_wms_example.html', title="wms_map.py example")
show(p)
