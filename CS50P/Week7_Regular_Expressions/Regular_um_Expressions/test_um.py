from um import count


def test_default():
    assert count("um") == 1
    assert count("um,") == 1
    assert count("um?") == 1


def test_inword():
    assert count("jump") == 0
    assert count("album") == 0

def test_sentence():
    assert count("um, c'est hamid de fes") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2



