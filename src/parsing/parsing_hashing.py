"""
Two Python files in this directory that work together:

    1) WordCountsExample.py: a module that does word counts on each
    file in a group of files and maintains word and character counts
    among all files read.
    2) parsing_hashing.py: a script that imports WordCountsExamples.py
    and has a command line interface for selecting data files to put
    into the word counter.  It also has a system of hashing file
    names to track files already processed.

There is also a directory of text files taken from the Brown corpus (see below).

This example was motivated by the general question:

     "I have a directory with a lot of files and new files show up there
     each time interval.  I want a cron job to launch periodically with
     some logic about processing new files, like wildcard matching patterns,
     and I also want to make sure that I don't process any files already processed.
     How should I keep track of files?"

This Python code provides some examples of:
   1) input/output to json
   2) NLTK stemming of words
   3) other standardization of text for processing (punctuation stripping)
   4) flexible logic to iterate over a group of files
   5) design of Python classes for stateful processes,
     like keeping a running counts dictionary
   6) try/finally blocks to ensure some code is always run before exiting
   7) usage of argparse for making command line interfaces
"""
import argparse
import codecs
import glob
import hashlib
from itertools import count
import json
import os

from WordCountsExample import WordCountsExample

DEFAULTS = {
    'data_dir': '../../data/looping_files_example/',
    'processing_class': 'WordCountsExample',
    'file_glob': '*',
    'hash_cache': './hashes.js',
    'output_file': './counts_json_lines.txt',
    'top_n_words': 2000000,
    'stem_method': "LancasterStemmer"
}

hashes = []

def load_hashes(hash_cache):
    """load a json from hash_cache location or return empty list if not there"""
    if os.path.exists(hash_cache):
        with open(hash_cache, 'r') as f:
            hashes = json.load(f)
    else:
        hashes = []
    return hashes


def file_gen(file_glob, data_dir, hashes):
    """Generate file hash, name, contents for a file_glob within data_dir,
    skipping hashes seen already.

    Input:
        file_glob: matching glob pattern within data_dir
        data_dir: where to look for data
        hashes: hashes of file names already processed
    Yields:
        (file_hash, file_name, file_contents) for all matching files
    """
    print('Begin file_gen with {} hashes observed'.format(len(hashes)))
    for f in glob.glob(os.path.join(data_dir, file_glob)):
        if os.path.isdir(f):
            continue
        # without the encode utf-8 part I was getting:
            # TypeError: Unicode-objects must be encoded before hashing
        # without .hexdigest() on the md5 functions I was getting:
            # TypeError: <md5 HASH object @ 0x10186f080> is not JSON serializable
        file_hash = hashlib.md5(f.encode('utf-8')).hexdigest()
        if file_hash in hashes:
            # uncomment this out if you want to be sure the skipping logic workds:
            # print('continue')
            continue
        try:
            with codecs.open(f, 'r', 'utf-8') as fhandle:
                contents = fhandle.read()
                yield (file_hash, f, contents)
        except Exception as e:
            print('ERROR:, the file being processed was', f,'failed with', repr(e))
            # TODO consider raising exception here

def dump_hashes(hashes, hash_cache):

    """Dump hashes to hash_cache location"""
    with open(hash_cache, 'w') as f:
        f.write(json.dumps(hashes))


def process_files(args):
    '''Iterate and apply callable to unprocessed files with hashes for tracking.

    Input:
        args: Namespace from cli() or a namespace with the same attributes as
              from cli()

            args.processing_class: processing class to instantiate.
                                   Must have an on_each_file method and a
                                   final_json method.
                                   (see WordCountsExample above)
            args.file_glob: the file glob to match in data_dir
            args.data_dir: where to look for data_dir
            args.hash_cache: where to look for and save hash list
            args.output_file: where to save newline delimited jsons from output
    '''
    if not args.processing_class in globals():
        raise ValueError('Argument "processing_class" must be a callable here in globals()')
    hashes = load_hashes(args.hash_cache)
    processing_class = globals()[args.processing_class]
    processing = processing_class(args)
    file_generator = file_gen(args.file_glob,
                              args.data_dir,
                              hashes)
    with open(args.output_file, 'w') as output_file_handle:
        try:
            for counter, output in enumerate(file_generator):
                (file_hash, f, contents) = output
                summary = processing.on_each_file(file_hash, f, contents,
                                                  args, output_file_handle)
                if summary:
                    hashes.append(file_hash)
                else: # allow the on_each_file method to return Falsy if unsuccessful
                    print('Processing failed on ', f, 'hash not appended.')
        except Exception as e:
            print('Failed with ', repr(e), '\n and args of', args)
            raise
        finally:
            print('Finalizing the hashes array with those processed so far')
            processing.final_json()
            dump_hashes(hashes, args.hash_cache)

def cli(parse_this_str=None):
    '''Makes the command line interface options for the file
    processing script.

    Inputs:
        parse_this_str: pass a string to parse in place of sys.argv
                        or None (default) to parse sys.argv
    Returns:
        Namespace from parsed string or sys.argv
    '''
    parser = argparse.ArgumentParser(description='Example word counts script '
                                                 'with file name or contents hashing')
    # These two statements make a requirement of 2 positional arguments
    parser.add_argument('file_glob',
                        help="Which filename matching glob.glob should be applied.  Defaults to entire directory")
    parser.add_argument('output_file',
                        help='Output file name for newline separated json output')
    # The remaining arguments are optional with defaults in DEFAULTS dictionary above
    parser.add_argument('-d',
                        '--data-dir',
                        help="In which directory to read files (top level)",
                        required=False,
                        default=DEFAULTS['data_dir'])
    parser.add_argument('-p',
                        '--processing-class',
                        help='Which class (imported or defined here) is instantiated ' +\
                             'for processing files.  See WordCountsExample for example class',
                        default=DEFAULTS['processing_class'],
                        required=False)
    parser.add_argument('-hc',
                        '--hash-cache',
                        help="Where to read and save the hashes already processed",
                        required=False,
                        default=DEFAULTS['hash_cache'])
    parser.add_argument('-t',
                        '--top-n-words',
                        help="When accumulating word counts keep the top-n-words, 2,000,000 by default.",
                        required=False,
                        default=DEFAULTS['top_n_words'],
                        type=int)
    parser.add_argument('-s',
                        '--stem-method',
                        help="Which NLTK method for word stemming.  Must be here in globals()",
                        required=False,
                        default=DEFAULTS['stem_method'])

    if parse_this_str is not None:
        # For testing sometimes it is helpful to have it parse
        # a string rather than sys.argv
        return parser.parse_args(parse_this_str)
    return parser.parse_args()

def main(parse_this_str=None):
    args = cli(parse_this_str=parse_this_str)
    print('Running with args of ', args)
    return process_files(args)

if __name__ == "__main__":
    main()
