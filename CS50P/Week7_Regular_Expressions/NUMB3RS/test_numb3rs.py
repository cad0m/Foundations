from numb3rs import validate

def test_valid_input():
    assert validate("1.1.1.1") == True
    assert validate("127.0.0.1") == True
    assert validate("140.247.235.144") == True
    assert validate("255.255.255.255") == True

def test_invalid_input():
    assert validate("256.255.255.255") == False
    assert validate("64.128.256.512") == False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False

def test_nonints_input():
    assert validate("hamid") == False
    assert validate("cs50") == False

def test_bit_numbers():
    assert validate("1.1.1") == False
    assert validate("1.1.1.1.0") == False





