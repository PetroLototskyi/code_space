from fuel import convert, gauge
import pytest

def test_positive():
    assert convert("3 / 4") == 75
    assert convert("1 / 4") == 25
    assert convert("4 / 4") == 100
    assert convert("0 / 4") == 0
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"

def test_negative():
    assert convert("-5 / 6") == -83
    assert convert("-2 / -2") == 100
    assert gauge(-83) == "E"
    assert gauge(-75) == "E"
'''
def test_gas_greater_than_100(monkeypatch):
    # predefined inputs
    monkeypatch.setattr('builtins.input', lambda _: "150/50")
    result = convert("150/50")
    assert result > 100
'''

def test_errors_handaling():
    with pytest.raises(ZeroDivisionError):
        convert("5 / 0")

    with pytest.raises(ValueError):
        convert("sony / pony")





