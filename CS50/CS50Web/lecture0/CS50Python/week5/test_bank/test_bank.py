from bank import value

def test_hello():

    assert value("hello") == 0
    assert value("hello bady") == 0
    assert value("Hello") == 0
    assert value("HELLO THERE") == 0

def test_h():
    assert value("Hi")  == 20
    assert value("holla")  == 20
    assert value("Hip Hop")  == 20
    assert value("hillary clinton")  == 20

def test_rest():
    assert value("Good Morning")  == 100
    assert value("Whatsup")  == 100
    assert value("Dobryi den")  == 100
    assert value("chest")  == 100
    assert value("Pruvit")  == 100

