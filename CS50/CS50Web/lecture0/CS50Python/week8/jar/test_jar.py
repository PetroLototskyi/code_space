from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar_one = Jar (15)
    assert jar_one.capacity == 15
    jar_two = Jar (2)
    assert jar_two.capacity == 2


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.cookies == 1
    jar.deposit(4)
    assert jar.cookies == 5


def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(2)
    assert jar.cookies == 5
    jar.withdraw(4)
    assert jar.cookies == 1

