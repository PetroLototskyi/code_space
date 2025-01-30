from seasons import obtain_DOB
import pytest

def test_DOB():
    assert obtain_DOB("1983-01-27") == (1983, 1, 27)

    with pytest.raises(SystemExit):
        obtain_DOB("1999-1-1")

    with pytest.raises(SystemExit, match="Invalid date"):
        obtain_DOB("invalid_date_format")


