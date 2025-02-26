from plates import is_valid

def test_two_letter():
    assert is_valid("ggjkl") == True
    assert is_valid("a11") == False
    assert is_valid("1ajki") == False
    assert is_valid("11a") == False

def test_max_min():
    assert is_valid("aaaaaa") == True
    assert is_valid("aa") == True
    assert is_valid("gggaaal") == False
    assert is_valid("a") == False

def test_periodes():
    assert is_valid("@zbi") == False
    assert is_valid("as,d5!") == False
    assert is_valid("ayoub?") == False
    assert is_valid("as1 23") == False

def test_numbers():
    assert is_valid("asd123") == True
    assert is_valid("asd1f5") == False
    assert is_valid("as0123") == False
    assert is_valid("as123l") == False



