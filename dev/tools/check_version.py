#!/usr/bin/env python
import sys
import codecs
import nbformat
import os


def read_notebook(notebook_filename):
    with codecs.open(notebook_filename, 'rb', 'utf-8') as f:
        try:
            return nbformat.read(f, nbformat.NO_CONVERT)
        except:
            print("Malformed notebook %s" % notebook_filename)
            sys.exit(-1)


if __name__ == '__main__':
    clean_list = True

    if len(sys.argv) > 1:
        notebooks = sys.argv[1:]
    else:
        sys.exit(0)

    for mod in notebooks:
        nb = read_notebook(mod)
        vers = nbformat.reader.get_version(nb)[0]
        clean_notebook = (vers == 4)
        if clean_notebook and os.environ.get('GIT_VERBOSE'):
            print(mod)
            print("  OK - correct version")
        elif not clean_notebook:
            print(mod)
            print("  VERSION ERROR: %s" % vers)
        clean_list = clean_list and clean_notebook

    # In Unix 0 means no errors
    return_code = int(not clean_list)
    sys.exit(return_code)
