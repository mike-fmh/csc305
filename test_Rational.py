from rational import Rational


def test_equals():
    rational12 = Rational(1, 2)
    assert rational12.equals(Rational(1, 2))


def test_as_float():
    assert False
