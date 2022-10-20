class Rational:
    """Stores rational numbers in fraction format."""
    def __init__(self, numerator: int, denominator: int):
        """:param numerator: the top number of the rational when expressed as a fraction.
           :param denominator: the bottom number of the fraction.

           :returns: None"""
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


if __name__ == '__main__':
    rational12 = Rational(1, 2)
    rational23 = Rational(2, 3)
    print("Test rational12 equals another Rational(1,2):", "passed" if rational12.equals(Rational(1, 2)) else "failed")
    print("Test rational12 not equals rational23:", "passed" if not rational12.equals(rational23) else "failed")
    print("Test rational12 < rational23 as floats:", "passed" if rational12.as_float() < rational23.as_float() else "failed")
