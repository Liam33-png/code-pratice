from fuel import convert,gauge
import pytest

def test_guage_default():
    assert gauge(50) == "50%"
def test_guage_full():
    assert gauge(100) == "F"
def test_guage_empty():
    assert gauge(0) == "E"

def test_convert_valerror():
    with pytest.raises(ValueError):
         convert("a/b")
    with pytest.raises(ValueError):
         convert("2/1")
def test_convert_norm():
    assert convert("1/2") == "50"
    assert convert("1/4") == "25"
    
    
