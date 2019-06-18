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

def test_normalize_fullname():
    assert normalize_fullname("EXáMPLE name") == "EXÁMPLE NAME"
    assert normalize_fullname("株式会社スタジオジブリ") == "株式会社スタジオジブリ"

def test_normalize_duration():
    assert normalize_duration("0:0:6.0") == 6
    assert normalize_duration("0:1:6.0") == 66
    assert normalize_duration("0:1:6.0") == 66
    assert normalize_duration("10:1:6.0") == 36066
