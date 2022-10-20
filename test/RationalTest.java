import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import static org.junit.jupiter.api.Assertions.*;

class RationalTest {
    @Test
    @DisplayName("Test rational12 equals another Rational(1,2)")
    void testEquals() {
        Rational rational12 = new Rational(1, 2);
        assertTrue(rational12.equals(new Rational(1, 2)));
    }

    @Test
    @DisplayName("Test rational12 not equals new Rational(1,3)")
    void testNotEquals() {
        Rational rational12 = new Rational(1, 2);
        assertFalse(rational12.equals(new Rational(1, 3)));
    }

    @Test
    @DisplayName("Rational(2,3) is approx. equal to 0.666667")
    void doubleValue() {
        Rational rational23 = new Rational(2, 3);
        assertEquals(0.666667, rational23.doubleValue(), 0.0001);
    }

    @Test
    @DisplayName("Test if zero is an illegal denominator")
    void zeroDenominatorIsIllegal() {
        assertThrows(IllegalArgumentException.class, () -> new Rational(1, 0));
    }
}