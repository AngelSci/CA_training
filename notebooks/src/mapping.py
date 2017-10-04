import collections.abc
import sys


class ShoutMap():
    "An odd mapping that returns an upper case version of its key"
    def __getitem__(self, key):
        return str(key).upper() + "!"

    def __iter__(self):
        return iter([])

    def __len__(self):
        return sys.maxsize

# I want ShoutMap to be a subclass of Mapping
collections.abc.Mapping.register(ShoutMap)
