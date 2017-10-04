from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future import standard_library
standard_library.install_aliases()
from future.builtins import (
                 bytes, dict, int, list, object, range, str,
                 ascii, chr, hex, input, next, oct, open,
                 pow, round, super, filter, map, zip)

import sys
sys.path.append("/Path/to/QEA/modules/")
#import QEA_custom_stuff

if sys.version_info[0] < 3:
    print("I'm importing arcGIS")
else:
    print("Please run this under Py2.7")


# ^^^^^^^^^ Boilerplate ^^^^^^^^^^^^^^^

# Real code below

def hello(name):
        """This function says hello to the caller

        The argument 'name' should be a persons firstname
        """
        print("Hello", name)

if __name__ == '__main__':
    hello("Raghav")

