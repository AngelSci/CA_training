"""In most uses, the doctests in this module would be 
placed inside the imported `parsing_hashing` module itself
"""

def tests():
    """Test suite adapted from other test framework versions
    
    >>> from parsing_hashing import load_hashes, cli
    >>> hashes = load_hashes('./hashes.js')
    >>> type(hashes)
    <class 'list'>

    >>> 2+2  # This better fail!
    5

    >>> 1/0  # Doctest knows how to look for expected exceptions
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero

    >>> # Test the cli function
    >>> args = cli(["*.ipynb",'output.txt'])
    >>> args.file_glob == '*.ipynb'
    True
    >>> args.output_file == 'output.txt'
    True
    >>> args.data_dir is not None
    True

    >>> # Test misuse of cli
    >>> import sys
    >>> sys.stderr = open('/dev/null','w')
    >>> try:
    ...     args = cli([])
    ...     ran_it = True
    ... except:
    ...     ran_it = False
    ...
    >>> ran_it
    False
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
