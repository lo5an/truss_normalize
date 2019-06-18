import pytest
from truss_normalize import *

def test_normalize_timestamp():
    # Check a Daylight Time converstion
    assert normalize_timestamp("4/1/11 11:00:00 AM") == "2011-04-01T14:00:00-04:00"
    # Check a Standard Time conversion
    assert normalize_timestamp("1/1/11 12:00:01 AM") == "2011-01-01T03:00:01-05:00"

def test_normalize_postal():
    # Check padding
    assert normalize_postal("1") == "00001"
    # Check nonconformant zipcode
    with pytest.raises(Exception):
        assert normalize_postal("123456")

def test_normalize_fullname():
    # Check a lowercase with diacritics
    assert normalize_fullname("EXáMPLE name") == "EXÁMPLE NAME"
    # Check non-alphabetic
    assert normalize_fullname("株式会社スタジオジブリ") == "株式会社スタジオジブリ"

def test_normalize_duration():
    # Check seconds
    assert normalize_duration("0:0:6.0") == 6
    # Check minutes
    assert normalize_duration("0:1:6.0") == 66
    # Check hours
    assert normalize_duration("10:1:6.0") == 36066
