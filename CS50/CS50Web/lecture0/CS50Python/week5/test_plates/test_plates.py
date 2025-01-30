from plates import is_valid

def test_begining():
    assert is_valid("AA") == True
    assert is_valid("1A") == False
    assert is_valid("A1") == False
    assert is_valid("11") == False

def test_lenght():
    assert is_valid("AAA222") == True
    assert is_valid("A") == False
    assert is_valid("AAAA333") == False
    assert is_valid("AAABCD") == True
    # assert is_valid("AAABCDKS") == False

def test_punctuation():
    assert is_valid("CS.50") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS-50") == False
    assert is_valid("CS50!") == False

def test_numbers_zero():
    assert is_valid("AA50") == True
    assert is_valid("ABC123") == True
    assert is_valid("AB053") == False


def test_start_with():
    assert is_valid("AA50") == True
    assert is_valid("ABC123") == True
    assert is_valid("50A33") == False
    assert is_valid("123ABC") == False
    assert is_valid("AAA33A") == False
    assert is_valid("AF33A") == False


