from typing import Callable


class Rational:
    _gcd_helper: Callable[[int, int], int] = None
    """Stores rational numbers in fraction format."""
    def __init__(self, numerator: int, denominator: int):
        """:param numerator: the top number of the rational when expressed as a fraction.
           :param denominator: the bottom number of the fraction.

           :returns: None"""
        if denominator == 0:
            raise ValueError
        self._numerator = numerator
        """The top number of the fraction"""
        self._denominator = denominator
        """The bottom number of the fraction"""

    def equals(self, other: 'Rational') -> bool:
        """Checks for equality between two Rational objects.

            :param other: the Rational object to compare to.
            :returns: bool - True if both Rationals are EXACTLY equal, False otherwise."""
        return self._numerator == other._numerator and self._denominator == other._denominator

    def as_float(self) -> float:
        """Gives the floating-point equivalent of the rational number.

        :returns: float"""
        if self._denominator == 0:
            # to prevent division by zero
            return 0
        else:
            return self._numerator / self._denominator

    def standard_form(self) -> 'Rational':
        """ Returns an equivalent Rational in standard form.
        The standard, or canonical, form of a Rational has a
        positive denominator and the numerator and denominator
        are coprime -- their greatest common factor is 1.
        (Thinking of the rational as a fraction, the fraction
        cannot be reduced/simplified.)
        :return: a new, equivalent Rational in standard form
        """
        # start by getting the original rational's values
        std_numerator, std_denominator = self._numerator, self._denominator
        if self._denominator < 0:
            # if the denominator is negative, move the negative
            # sign to the numerator by multiplying both by -1
            std_numerator, std_denominator = -std_numerator, -std_denominator
        # set the std numerators & denominators to the rational's reduced form
        divisor = Rational._gcd_helper(std_numerator, std_denominator)
        std_numerator = std_numerator // divisor  # // is integer division
        std_denominator = std_denominator // divisor
        return Rational(std_numerator, std_denominator)
