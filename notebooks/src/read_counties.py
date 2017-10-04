from collections import OrderedDict, namedtuple
from warnings import warn
import csv
from enum import IntEnum

Coord = namedtuple('Coord', 'lon lat')

# Create an enum for fields, keep names as close to header fields as possible
Field = IntEnum('Field',
                '''County_Name
                   State_County
                   state_abbr
                   State_Abbr
                   geometry
                   value
                   GEO_ID
                   GEO_ID2
                   Geographic_Name
                   STATE_num
                   COUNTY_num
                   FIPS_formula
                   Has_error''')


def read_county_data(file):
    """Read polygon information for a filename or file-like object

    Return an OrderedDict of geometries, removing redundant field information.

    For the key, use the 'State-County' field, which is required to be unique
    in the underlying data.
    """
    Counties = OrderedDict()
    key_lines = {}   # For warning messages of duplicates

    # Is it a file-like object?
    if hasattr(file, 'read'):
        pass               # We'll read it below
    # It's a filename (hopefully), so open it
    elif isinstance(file, str):
        file = open(file)
    # We don't know how to handle this argument
    else:
        raise TypeError("Must pass a file-like object or filename")

    lines = csv.reader(file)
    header = next(lines)
    # Quick sanity check for having the right header
    if header[:4] != ['County Name', 'State-County',
                      'state abbr', 'State Abbr.']:
        raise ValuError("File indicated does not contain appropriate "
                        "header:\n  Found %s" % header)
    # Now loop through the actual data lines
    for n, line in enumerate(lines):
        # Unfortunately, IntEnum's start at 1 in their default definition
        line = [None] + line

        # Check for inconsistent data
        if line[Field.state_abbr].upper() != line[Field.State_Abbr]:
            warn("Inconsistent upper and lowercase state abbreviation "
                 "on line %d (%s/%s)" % (
                    n+1, line[Field.state_abbr], line[Field.State_Abbr]))
        if line[Field.State_County] != "%s-%s" % (
                        line[Field.State_Abbr], line[Field.County_Name]):
            warn("Inconsistent State-County field versus its components "
                 "on line %d (%s/%s/%s)" % (
                    n+1, line[Field.State_County],
                    line[Field.County_Name], line[Field.State_Abbr]))

        key = line[Field.State_Abbr], line[Field.County_Name]
        if key in Counties:
            # For no well-motivated reason, use "first line wins" rule
            prior = key_lines[key]
            warn("Duplicate county information found on line %d(%d): %s" % (
                    n, prior, key))
        else:
            Counties[key] = process_geometry(line[Field.geometry])
            key_lines[key] = n

    return Counties


def process_geometry(geometry):
    """Process raw geometry field into a list of (lon, lat) pairs

    Note that although the field is technically an XML snippet, the actual
    data is surrounded by the same tags in every case.  Stripping this extra
    wrapper can be done with basic string replacement.

    A geometry consists of one or more polygons.  In the case where there
    are multiple, the several <Polygon> elements are wrapped in
    <MultiGeometry>.  Otherwise the top level tag is <Polygon>.

    """

    polygons = set()  # The set of all the polygons

    # Cleanup extra tags that aren't strictly required for parse
    tags = ["MultiGeometry", "innerBoundaryIs", "outerBoundaryIs",
            "LinearRing", "coordinates"]
    for tag in tags:
        geometry = geometry.replace("<%s>" % tag, " ")
        geometry = geometry.replace("</%s>" % tag, " ")
    geometry = geometry.replace("</Polygon>", " ")

    # We now have just: '<Polygon>... [<Polygon>...]'
    for polygon in geometry.split('<Polygon>'):
        if not polygon.strip():
            # Ignore extra empty results of the split
            continue
        points = polygon.split()
        polygon = []
        for point in points:
            lon, lat = map(float, point.split(','))
            polygon.append(Coord(lon, lat))

        # Add the current polygon to polygons
        polygons.add(tuple(polygon))
    return polygons
