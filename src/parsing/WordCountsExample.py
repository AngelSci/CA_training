
from collections import defaultdict
from collections import Counter
import json
import string

from nltk.stem.porter import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer

class WordCountsExample(object):
    """Word counts on a file's contents as example of single file processor

    Write other processors using a similar class with the following methods:

            __init__: takes self and args from cli() as initialization
            on_each_file: processes each file, see below
            final_json: called at the end, see below
    """

    def __init__(self, args):
        self.args = args
        self.word_counts = defaultdict(lambda: 0)
        self.character_counts = defaultdict(lambda: 0)
        self.files_processed_ok = 0
        if not self.args.stem_method in globals():
            raise ValueError('Must use a --stem-method that is in globals() '
                             'here, e.g. LancasterStemmer or PorterStemmer')
        self.stemmer = globals()[self.args.stem_method]()

    def preprocess_for_word_counts(self, content):
        '''Replace all punctuation with spaces, then split, then stem.

        Inputs:
            content: raw string content of one file
        Returns:
            tuple of stemmed words
        '''
        translator = content.maketrans(string.punctuation,
                          "".join([' ' for _ in string.punctuation]))
        no_symbols = content.translate(translator)
        words = no_symbols.split()
        stemmed = tuple(map(self.stemmer.stem, words))
        return stemmed

    def prune_uncommon(self, keep_top_n=2000000):
        '''prune_uncommon limits the size of the running word_counts dict to keep_top_n items.

        Inputs:
            keep_top_n: integer number of items to keep in self.word_counts
        '''
        if len(self.word_counts) > keep_top_n:
            sorted_items = sorted(self.word_counts.items(), key=lambda x: -x[1])
            for excluded_key, _  in sorted_items[keep_top_n:]:
                self.word_counts.pop(excluded_key)

    def update_totals(self, word_counts, character_counts):
        '''Add a file's word and character counts to the
        dictionaries that track word and character counts
        across all files processed.

        Inputs:
            word_counts: word_counts for a file
            character_counts: character_counts for a file
        '''
        for key, value in word_counts.items():
            self.word_counts[key] += value
        for key, value in character_counts.items():
            self.character_counts[key] += value
        self.prune_uncommon(self.args.top_n_words)

    def on_each_file(self, file_hash, f, contents,  args, output_file_handle=None):
        """
        on_each_file is called on each file. It updates word and character counts.
        Inputs:
            file_hash: hash of the filename
            f: the file name
            contents: the contents of the file
            args: all arguments of the cli() typically (Namespace)
        Returns:
            summary dictionary of word counts, character counts, file length,
            file name hash, and contents hash

        Writes a json in a single line to output_file_handle followed by newline
        if output_file_handle is not None.
        """
        character_counts = Counter(contents)
        stemmed_words = self.preprocess_for_word_counts(contents)
        word_counts = Counter(stemmed_words)
        lenn = len(contents)
        contents_hash = hash(contents)
        summary = {'characters': character_counts,
                   'words': word_counts,
                   'len': lenn,
                   'file_hash': file_hash,
                   'contents_hash': contents_hash,
                   }
        self.update_totals(word_counts, character_counts)
        if output_file_handle is not None:
            j = json.dumps(summary)
            output_file_handle.write(j + '\n')
        self.files_processed_ok += 1
        return summary

    def final_json(self):
        '''Called at the end, final_json writes the state to json files. '''
        if '.' in self.args.output_file:
            *left, right = self.args.output_file.split('.')
            totals_file = '.'.join(left) + '__totals.' + right
        else:
            totals_file = self.args.output_file + '__totals'
        with open(totals_file, 'w') as f:
            summary = {'total_word_counts': self.word_counts,
                       'total_character_counts': self.character_counts,
                       'files_processed_ok': self.files_processed_ok}
            f.write(json.dumps(summary))
