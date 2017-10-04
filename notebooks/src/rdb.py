import csv
from collections import namedtuple, OrderedDict


def read_rdb(filename):
    """Read all the information in an RDB file

    Subject area experts will find the format familiar, I am sure.  The
    *rdb* format is described at
    http://help.waterdata.usgs.gov/faq/about-tab-delimited-output as well.
    But I am a non-expert in the subject area, so I will just visually
    examine it, and figure out in a relatively ad hoc way how to read and
    utilize it.

    Here are some things I notice:

    * The file starts with a commented header, with each line beginning with
      a hash mark (`# `) and space.
    * The next line after the header is a list of field names.
    * Some field names start with numbers, and are not valid Python
      identifiers.
    * The next line after the field names is the data types of the
      columns; but I'm not sure exactly what those descriptions mean.
    * The bulk of the file is tab-separated values.

     Let's write a small custom function to parse what we see in this data
     format.  Note that I actually *did* a quick search, and it appears the
     modules `Asciitable` and the package `Astropy` both seem to support
     this format (other existing libraries might also); but suppose it was
     something novel.
    """
    fh = open(filename)
    # First collect the comments, stopping at the field names
    comment_lines = []
    for line in fh:
        # We've gotten to the header
        if not line.startswith('#'):
            fields = line.rstrip().split('\t')
            break
        comment_lines.append(line[2:])
    # Make the individual lines into one string
    comment = ''.join(comment_lines)
    # Read the next line with the data formats
    formats = next(fh).rstrip().split('\t')
    # Make sure field names are valid Python identifiers
    field_names = [f if f[0].isalpha() else 'N_'+f for f in fields]
    # Define header as ordered mapping of field name to data type
    header = OrderedDict(zip(field_names, formats))
    row = namedtuple('Row', field_names)
    records = []
    for values in csv.reader(fh, delimiter='\t'):
        records.append(row(*values))
    # Close the file before we leave
    fh.close()
    return comment, header, records
