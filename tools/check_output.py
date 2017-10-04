#!/usr/bin/env python
import sys
import json
import os


def check_output(nb, mod):
    clean_notebook = True

    #for pat in NO_CHECK:
    #    if pat in mod:
    #        return True

    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            if cell['execution_count'] is not None:
                print(mod)
                print("  OUTPUT FOUND %d: %s" %
                      (cell['execution_count'], cell['source'][0].strip()))
                clean_notebook = clean_notebook and False
    if clean_notebook and os.environ.get('GIT_VERBOSE'):
        print(mod)
        print("  OK - No output found")

    return clean_notebook


if __name__ == '__main__':
    clean_list = True

    if len(sys.argv) > 1:
        notebooks = sys.argv[1:]
    else:
        sys.exit(0)

    for mod in notebooks:
        nb = json.load(open(mod))
        clean_notebook = check_output(nb, mod)
        clean_list = clean_list and clean_notebook

    # In Unix 0 means no errors
    return_code = int(not clean_list)
    sys.exit(return_code)
