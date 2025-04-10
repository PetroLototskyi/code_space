from working import convert
import pytest


def test_corect_input():
    assert convert("9 AM to 5 PM") == ("09:00 to 17:00")
    assert convert("9:00 AM to 5:00 PM") == ("09:00 to 17:00")
    assert convert("10 PM to 8 AM") == ("22:00 to 08:00")
    assert convert("10:30 PM to 8:50 AM") == ("22:30 to 08:50")


def test_incorect_input():
    with pytest.raises(ValueError):
        convert("7 AM 3 PM")
    with pytest.raises(ValueError):
        convert("7 AM : 3 PM")


def test_incorect_hour():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")


def test_incorect_min():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
