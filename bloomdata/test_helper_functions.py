import pytest
import bloomdata.helper_functions as hf

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
