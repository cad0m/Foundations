from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12
    with pytest.raises(ValueError):
        jar = Jar(5, -3)
        jar = Jar(-5, 3)
        jar = Jar("l", 5)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5, 1)
    assert jar.size == 1
    jar.deposit(1)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.deposit(-3)
        jar.deposit(8)


def test_withdraw():
    jar = Jar(5, 5)
    assert jar.size == 5
    jar.withdraw(2)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(-3)
        jar.withdraw(6)
