import pytest
from fuel import convert, gauge


def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")
        assert convert("0/0")

def test_ValueError():
    with pytest.raises(ValueError):
        assert convert("2/1")

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("1/3") == 33
    assert convert("1/5") == 20

def test_EorF():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_guage():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"




