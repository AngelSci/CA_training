# BokehGeo Lesson Plan

## Overview

What is BokehGeo?
    * GPX  
    * KML
    * WMS
    * Transfer Functions used with maps

Another way to describe it:

* Bokeh Bindings for popular Geo formats
   * GPX
   * KML
   * WMS
   * Transfer Functions used with maps

## Examples demonstrating BokehGeo map plots

* gpx example
    * source activate iqt
    * python gpx_example.py
    * GPX file format
    * https://en.wikipedia.org/wiki/GPS_Exchange_
    Format
    * GPX, or GPS Exchange Format, is an XML schema designed as a common GPS data format for software applications. It can be used to describe waypoints, tracks, and routes. 
    * Lons and lats

* kml example
    * source activate iqt
    * python kml_example.py
    * KML is file format used for Google Earth

* WMS Example
    * source activate iqt
    * python wms_geographic_projection.py
    * WMS is an HTTP spec for how to retreave an image file from a web server
    * as opposed to requesting tiles, you are requesting full images... that's what WMS is!

* Simple WMS Example
    * source activate iqt
    * python simple_wms.py
    * Another WMS example, colored states done by 
    * During the demo, be sure to zoom in!
    * As you zoom, it's pulling new tiles from the WMS site



