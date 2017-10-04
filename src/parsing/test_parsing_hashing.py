import pytest
from parsing_hashing import load_hashes, cli


def test_load_hashes():
    hashes = load_hashes('./hashes.js')
    assert isinstance(hashes, list)

def test_cli():
    args = cli(["*.ipynb",'output.txt'])
    assert args.file_glob == '*.ipynb'
    assert args.output_file == 'output.txt'
    assert args.data_dir is not None

def test_bad_cli_args():
    try:
        args = cli([])
        ran_it = True
    except:
        ran_it = False
    assert not ran_it

def test_file_gen():
    file_glob = '*'
    where_i_am = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(where_i_am, "../../data/looping_files_example")
    hashes = []
    should_have_found = len(os.listdir(data_dir))
    file_list = list(file_gen(file_glob, data_dir, hashes))
    self.assertEqual(len(file_list), should_have_found)
