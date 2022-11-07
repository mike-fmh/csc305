from rational import Rational
from math import isclose
import pytest


def setup_function():
    Rational._gcd_helper = lambda a, b: 1


def teardown_function():
    Rational._gcd_helper = None


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


def test_1_2_standard_form():
    original = Rational(1, 2)
    standard = Rational(1, 2)
    assert standard.equals(original.standard_form())


def test_0_1_standard_form():
    original = Rational(0, 1)
    standard = Rational(0, 1)
    assert standard.equals(original.standard_form())


def test_1_n1_standard_form():
    original = Rational(-1, 1)
    standard = Rational(-1, 1)
    assert standard.equals(original.standard_form())


def test_n1_1_standard_form():
    original = Rational(1, -1)
    standard = Rational(-1, 1)
    assert standard.equals(original.standard_form())


def test_0_n1_standard_form():
    original = Rational(0, -1)
    standard = Rational(0, 1)
    assert standard.equals(original.standard_form())


def test_n1_n1_standard_form():
    original = Rational(-1, -1)
    standard = Rational(1, 1)
    assert standard.equals(original.standard_form())


def test_n30_n5_standard_form():
    Rational._gcd_helper = lambda a, b: 5
    original = Rational(-30, -5)
    standard = Rational(6, 1)
    assert standard.equals(original.standard_form())


def test_12_8_standard_form():
    Rational._gcd_helper = lambda a, b: 4
    original = Rational(12, 8)
    standard = Rational(3, 2)
    assert standard.equals(original.standard_form())


def test_350_n70_standard_form():
    Rational._gcd_helper = lambda a, b: 70
    original = Rational(350, -70)
    standard = Rational(-5, 1)
    assert standard.equals(original.standard_form())


def test_21_n49_standard_form():
    Rational._gcd_helper = lambda a, b: 7
    original = Rational(21, -49)
    standard = Rational(-3, 7)
    assert standard.equals(original.standard_form())
