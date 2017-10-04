from bokeh.io import output_file, show
from bokeh.plotting import figure

from bokeh_geo.sources import KMLDataSource

# create figure
fig = figure(title="Bokeh KML Example",
             tools='pan, wheel_zoom',
             x_range=(-122.372, -122.362),
             y_range=(37.818, 37.826))

# add kml points
with open('../data/BokehGeo/point.kml') as p:
    point_kml = p.read()

kml_point_source = KMLDataSource(features=point_kml)
fig.circle(x='x',
           y='y',
           color="blue",
           size=20,
           alpha=0.9,
           source=kml_point_source)

# add kml lines
with open('../data/BokehGeo/linestring.kml') as l:
    line_kml = l.read()

kml_line_source = KMLDataSource(features=line_kml)
fig.multi_line(xs='xs',
               ys='ys',
               color="red",
               alpha=0.9,
               line_width=2,
               source=kml_line_source)

# add kml polygons
with open('../data/BokehGeo/polygon.kml') as k:
    polygon_kml = k.read()

kml_polygon_source = KMLDataSource(features=polygon_kml)
fig.patches(xs='xs',
            ys='ys',
            alpha=0.9,
            source=kml_polygon_source)

# finish up...
output_file("geojson.html")
show(fig)
