/**
 * Stores rational numbers as fractions.
 */
public class Rational {
    /**
     * The top number of the fraction
     */
    private int _numerator;
    /**
     * The bottom number of the fraction
     */
    private int _denominator;

    public int GetNumerator() {
        return this._numerator;
    }

    public int GetDenominator() {
        return this._denominator;
    }

    /**
     * @param numerator   the top number of the rational when expressed as a fraction.
     * @param denominator the bottom number of the fraction.
     */
    public Rational(int numerator, int denominator) {
        if (denominator == 0) {
            throw new IllegalArgumentException("Denominator cannot be zero");
        }
        this._numerator = numerator;
        this._denominator = denominator;
    }

    /**
     * @param other a Rational object to compare the calling class to.
     * @return boolean - true if both Rationals are EXACTLY equal, false otherwise.
     **/
    public boolean equals(Rational other) {
        return (float) this.GetNumerator() == (float) other.GetNumerator() && (float) this.GetDenominator() == (float) other.GetDenominator();
    }

    /**
     * Gives the double equivalent of the rational number.
     *
     * @return double
     */
    public double doubleValue() {
        if (this.GetDenominator() == 0) {
            // so we don't divide by 0
            return 0;
        } else {
            return (double) this.GetNumerator() / (double) this.GetDenominator();
        }
    }
}