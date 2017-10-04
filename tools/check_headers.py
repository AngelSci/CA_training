#!/usr/bin/env python
from collections import Iterable
import sys
import nbformat
import codecs
import re
import os


def read_notebook(notebook_filename):
    with codecs.open(notebook_filename, 'rb', 'utf-8') as f:
        return nbformat.read(f, nbformat.NO_CONVERT)

def check_headers(nb, mod,debug=True):
    clean_notebook = True
    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            # check for malformed header cell (must have space)
            header = re.compile('^[#]+[a-zA-Z0-9]')
            match = header.match(cell['source'])
            if match:
                if(debug):
                    print(mod)
                    print("  HEADER ERROR: %s" % cell['source'])
            clean_notebook = clean_notebook and not bool(match)

            # header cells must be one line long except TOC
            header = re.compile('^[#]+ [a-zA-Z0-9]')
            match = header.match(cell['source'])
            error = (match
                    and cell['source'].splitlines()[0] != '# Table of Contents'
                    and (len(cell['source'].splitlines()) > 1))
            if error:
                if(debug):
                    print(mod)
                    print("  TOC ERROR: %s" % cell['source'])
            clean_notebook = clean_notebook and not bool(error)


    if clean_notebook and os.environ.get("GIT_VERBOSE"):
        print(mod)
        print("  OK - No header errors found")

    return clean_notebook


if __name__ == '__main__':
    clean_list = True

    if len(sys.argv) > 1:
        notebooks = sys.argv[1:]
    else:
        sys.exit(0)

    for mod in notebooks:
        nb = read_notebook(mod)
        clean_notebook = check_headers(nb, mod)
        clean_list = clean_list and clean_notebook

    # In Unix 0 means no errors
    return_code = int(not clean_list)
    sys.exit(return_code)
