import pytest
from truss_normalize import *


def test_normalize_timestamp():

    assert normalize_timestamp("4/1/11 11:00:00 AM") == "2011-04-01T14:00:00-04:00"
    assert normalize_timestamp("1/1/11 12:00:01 AM") == "2011-01-01T03:00:01-05:00"
    assert normalize_timestamp("1/1/11 12:00:01 AM") == "2011-01-01T03:00:01-05:00"

def test_normalize_postal():
    assert normalize_postal("1") == "00001"

    with pytest.raises(Exception):
        assert normalize_postal("123456")
