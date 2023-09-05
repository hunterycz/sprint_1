import pytest
import bloomdata.helper_functions as hf
import numpy as np


adjectives = ['blue', 'large', 'grainy',
              'substantial', 'potent', 'thermonuclear']
nouns = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

list1 = [1, 2, 3]
list2 = [4, 5, 6]


def test_random_phrase():
    assert type(hf.random_phrase(adjectives, nouns)) == str
    assert type(hf.random_phrase(list1, list2)) == str
    assert hf.random_phrase(['Ryan'], ['Allred']) == 'Ryan Allred'
    assert hf.random_phrase([3], [4]) == '3 4'

# 3 new pytest functions for module 4 guide project

# check if output is a float


def test_random_float():
    assert isinstance(hf.random_float(0, np.random.randint(1, 101)), float)


def test_random_float_all_0():
    assert isinstance(hf.random_float(0, 0), float)


def test_silly_tuple_is_tuple():
    assert isinstance(hf.silly_tuple(), tuple)
