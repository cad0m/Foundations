from twttr import shorten

def test_number_symboles():
    assert shorten("123456789") == "123456789"
    assert shorten("*-+= ><?|}") == "*-+= ><?|}"

def test_novoyels():
    assert shorten("qwrtypsdfghjklzxcvbnm") == "qwrtypsdfghjklzxcvbnm"
    assert shorten("qwrtypsdfghjklzxcvbnm123456789") == "qwrtypsdfghjklzxcvbnm123456789"

def test_onlyvoyels():
    assert shorten("AEIOU") == ""
    assert shorten("aeiou") == ""
    assert shorten("aeiouAEIOU") == ""

def test_notext():
    assert shorten("    ") == "    "

