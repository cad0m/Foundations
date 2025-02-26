from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("hello,") == 0
    assert value("HELLO") == 0
    assert value("Hello5fam98") == 0

def test_h():
    assert value("hahaha") == 20
    assert value("hey123hello") == 20
    assert value("helliow") == 20

def test_noh():
    assert value("123456789") == 100
    assert value("qwertyuiopasdfghjkzxcvbnm") == 100
    assert value(",/.'lo[]") == 100
