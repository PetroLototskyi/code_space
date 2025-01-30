from twttr import shorten

def test_vowels():
    assert shorten("Hermione") == "Hrmn"
    assert shorten("ananas") == "nns"
    assert shorten("STAPLE APPLE") == "STPL PPL"

def test_numeric():
    assert shorten("12345")  == "12345"
    assert shorten("12.75")  == "12.75"
