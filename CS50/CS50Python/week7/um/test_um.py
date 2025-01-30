from um import count

def test_ignorecase():
    assert count (r"Um, thanks, um...") == 2
    assert count (r"Um, thanks for the album.") == 1

def test_punctuation():
    assert count (r"um?") == 1
    assert count (r"um.. um?") == 2

def test_inside_word():
    assert count (r"yummy") == 0

def test_tricky():
    assert count (r"Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") ==2
    assert count (r"um") == 1
