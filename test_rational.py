from rational import Rational
from math import isclose
import pytest


def test_equals():
    rational12 = Rational(1, 2)
    assert rational12.equals(Rational(1, 2))


def test_not_equals():
    rational12 = Rational(1, 2)
    assert not rational12.equals(Rational(2, 3))


def test_as_float():
    rational23 = Rational(2, 3)
    assert isclose(0.66667, rational23.as_float(), abs_tol=0.0001)


def test_zero_denominator_is_error():
    with pytest.raises(ValueError):
        Rational(1, 0)


