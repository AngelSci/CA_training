#!/usr/bin/env python
import sys
import json
import re
import os


NO_CHECK = ['/Notes/', '/coursebuild/']

def check_toc(nb, mod):
    clean_notebook = True
    found_toc = False

    # Some directories exempt from needing TOC
    for pat in NO_CHECK:
        if pat in mod:
            return True

    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            header = re.compile('^[#]+\s*Table of Contents')
            match = bool(header.match(cell['source'][0])) and len(
                cell['source']) == 1
            if match:
                print(mod)
                print("  TOC ERROR: use calico document-tools")
            clean_notebook = clean_notebook and not bool(match)

            found_toc = found_toc or bool(header.match(cell['source'][0]))
    if not found_toc:
        print(mod)
        print("  TOC MISSING: use calico document-tools")
    elif clean_notebook and os.environ.get('GIT_VERBOSE'):
        print(mod)
        print("  OK - No TOC errors found")

    return clean_notebook and found_toc


if __name__ == '__main__':
    clean_list = True

    if len(sys.argv) > 1:
        notebooks = sys.argv[1:]
    else:
        sys.exit(0)

    for mod in notebooks:
        nb = json.load(open(mod))
        clean_notebook = check_toc(nb, mod)
        clean_list = clean_list and clean_notebook

    # In Unix 0 means no errors
    return_code = int(not clean_list)
    sys.exit(return_code)
