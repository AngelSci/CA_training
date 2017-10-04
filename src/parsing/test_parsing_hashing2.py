import os
import unittest

from parsing_hashing import file_gen, mistakes

class MyTest(unittest.TestCase):

    def test_1(self):
        file_glob = '*'
        where_i_am = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(where_i_am, "../../data/looping_files_example")
        hashes = []
        file_list = list(file_gen(file_glob, data_dir, hashes))
        self.assertEqual(len(file_list), 499)

    def test_load_hashes(self):
        hashes = load_hashes('./hashes.js')
        assert isinstance(hashes, list)

    def test_cli(self):
        args = cli(["*.ipynb",'output.txt'])
        assert args.file_glob == '*.ipynb'
        assert args.output_file == 'output.txt'
        assert args.data_dir is not None

    def test_bad_cli_args(self):
        with self.assertRaises(ValueError):
            args = cli([])
