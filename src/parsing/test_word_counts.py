import json

from WordCountsExample import WordCountsExample
from parsing_hashing import cli

def test_init():
    args = cli(['*', 'output.txt'])
    wc = WordCountsExample(args)
    assert hasattr(wc, 'args')
    assert hasattr(wc, 'stemmer')
    assert hasattr(wc, 'word_counts')
    assert hasattr(wc, 'character_counts')
    assert wc.files_processed_ok == 0

def test_processing():
    args = cli(['*', 'output.txt'])
    wc = WordCountsExample(args)
    contents = 'I am running.'
    stemmed = wc.preprocess_for_word_counts(contents)
    assert stemmed == ('i', 'am','run',)
    with open(args.output_file, 'w') as f:
        summary = wc.on_each_file('hash', 'name', contents,
                                  f)
    assert summary.get('words', {}).get('run', 0) == 1
    assert summary.get('words', {}).get('i', 0) == 1
    assert summary.get('characters', {}).get('r', 0) == 1
    assert wc.word_counts.get('run', 0) == 1
    assert wc.character_counts.get('r', 0) == 1
    assert wc.word_bigrams_counts.get('i am', 0) == 1
    assert wc.word_bigrams_counts.get('am run', 0) == 1
    assert wc.character_bigrams_counts.get('ru', 0) == 1
    with open(args.output_file, 'r') as f:
        js = json.loads(f.readline())
        assert js == summary
    assert wc.files_processed_ok == 1
