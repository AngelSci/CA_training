from bokeh.io import output_file, show
from bokeh.plotting import figure

from bokeh_geo.sources import GPXDataSource

# create figure
fig = figure(title="Bokeh GPX Example",
             tools='pan, wheel_zoom',
             x_range=(-77.018, -77.0015),
             y_range=(38.89, 38.91))

# add kml points
with open('../data/BokehGeo/osm.gpx') as p:
    line_gpx = p.read()

gpx_line_source = GPXDataSource(features=line_gpx)
fig.multi_line(xs='xs',
               ys='ys',
               color="red",
               alpha=0.9,
               line_width=2,
               source=gpx_line_source)

output_file("gpx.html")
show(fig)
