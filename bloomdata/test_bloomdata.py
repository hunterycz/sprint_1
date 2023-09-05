import pytest
import bloomdata.bloomdata as bd


def test_increment_int():
    assert bd.increment(3) == 4
    assert bd.increment(-2) == -1


def test_increment_float():
    assert bd.increment(1.5) == 2.5


def test_increment_int_return_type_int():
    assert isinstance(bd.increment(3), int)


def test_increment_int_return_type_float():
    assert isinstance(bd.increment(1.5), float)
