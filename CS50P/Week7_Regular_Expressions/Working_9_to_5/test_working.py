import pytest
from working import convert

def test_default():
    assert convert('03:00 AM to 4:00 PM') == '03:00 to 16:00'
    assert convert('11:56 AM to 8:59 AM') == '11:56 to 08:59'


def test_input_format():
    with pytest.raises(ValueError):
         convert('this test so hard')
    with pytest.raises(ValueError):
         convert('08:00 AM - 9:00 PM')
    with pytest.raises(ValueError):
         convert('9:00AM to 7:00PM')

def test_hourMinute_range():
    with pytest.raises(ValueError):
         convert('09:00 AM to 17:00 PM')
    with pytest.raises(ValueError):
         convert('09:60 AM to 07:00 PM')

