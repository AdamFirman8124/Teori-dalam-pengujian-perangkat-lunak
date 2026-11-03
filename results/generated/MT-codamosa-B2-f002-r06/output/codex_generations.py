

# Generated at 2026-11-02 16:55:08.608929
# Unit test for function truncate_number
def test_truncate_number():
    # nonce:d81650e7
    # Truncates the fractional part of a positive float
    assert math.isclose(module_0.truncate_number(3.5), 0.5, abs_tol=1e-9)
    # Another typical case
    assert math.isclose(module_0.truncate_number(2.75), 0.75, abs_tol=1e-9)
    # Whole number has no fractional part
    assert module_0.truncate_number(10.0) == 0.0
    # Number smaller than one returns itself
    assert math.isclose(module_0.truncate_number(0.25), 0.25, abs_tol=1e-9)
    # Large number with fractional part
    assert math.isclose(module_0.truncate_number(1234.5678), 0.5678, abs_tol=1e-9)
    # Negative number: Python's % returns a positive remainder
    assert math.isclose(module_0.truncate_number(-1.5), 0.5, abs_tol=1e-9)
    # Zero has no fractional part
    assert module_0.truncate_number(0.0) == 0.0

# Generated at 2026-11-02 16:56:26.945901
# Unit test for function truncate_number
def test_truncate_number():
    # Basic positive number with fractional part
    assert module_0.truncate_number(3.5) == 0.5
    assert module_0.truncate_number(123.456) == 0.456
    assert module_0.truncate_number(0.25) == 0.25

    # Whole numbers should return 0.0
    assert module_0.truncate_number(4.0) == 0.0
    assert module_0.truncate_number(100.0) == 0.0

    # Numbers less than 1
    assert module_0.truncate_number(0.5) == 0.5
    assert module_0.truncate_number(0.999) == 0.999

    # Negative numbers: Python modulo follows sign of divisor
    assert module_0.truncate_number(-3.5) == 0.5
    assert module_0.truncate_number(-1.25) == 0.75

    # Very large number
    assert module_0.truncate_number(1e10 + 0.5) == 0.5

    # Return type check
    assert isinstance(module_0.truncate_number(2.7), float)
    assert isinstance(module_0.truncate_number(5), float)

    # Verify result is in valid range [0, 1)
    for value in [10.75, -7.3, 0.001, 999.999]:
        result = module_0.truncate_number(value)
        assert 0.0 <= result < 1.0

# Generated at 2026-11-02 16:57:34.253280
# Unit test for function truncate_number
def test_truncate_number():
    # Test with a positive float having a fractional part
    assert module_0.truncate_number(3.5) == 0.5
    # Test with a number just above an integer
    assert module_0.truncate_number(1.33) == 0.33
    # Test with a whole number (no fractional part)
    assert module_0.truncate_number(4.0) == 0.0
    # Test with zero
    assert module_0.truncate_number(0.0) == 0.0
    # Test with a small fractional part
    assert abs(module_0.truncate_number(2.123) - 0.123) < 1e-9
    # Test with a large number
    assert module_0.truncate_number(123.456) == 123.456 % 1.0
    # Test with negative number (Python modulo returns positive fractional part)
    assert module_0.truncate_number(-1.5) == 0.5
    # Test with negative whole number
    assert module_0.truncate_number(-3.0) == 0.0
    # Result should always be in [0.0, 1.0)
    result = module_0.truncate_number(7.75)
    assert 0.0 <= result < 1.0

# Generated at 2026-11-02 16:59:05.639350
# Unit test for function truncate_number
def test_truncate_number():
    assert module_0.truncate_number(3.5) == 0.5
    assert module_0.truncate_number(1.25) == 0.25
    assert module_0.truncate_number(2.0) == 0.0
    assert module_0.truncate_number(0.0) == 0.0
    assert module_0.truncate_number(100.75) == 0.75
    assert module_0.truncate_number(-1.5) == 0.5
    assert module_0.truncate_number(0.999) == 0.999
    assert module_0.truncate_number(7.123456) == pytest.approx(0.123456)
    assert module_0.truncate_number(1e10 + 0.5) == 0.5

# Generated at 2026-11-02 17:00:16.400252
# Unit test for function truncate_number
def test_truncate_number():import unittest


def module_0.truncate_number(number: float) -> float:
    return number % 1.0


# Unit test for function truncate_number
class TestTruncateNumber(unittest.TestCase):

    def test_positive_float(self):
        self.assertAlmostEqual(module_0.truncate_number(3.5), 0.5)

    def test_whole_number(self):
        self.assertEqual(module_0.truncate_number(5.0), 0.0)

    def test_zero(self):
        self.assertEqual(module_0.truncate_number(0.0), 0.0)

    def test_negative_float(self):
        self.assertAlmostEqual(module_0.truncate_number(-1.5), 0.5)

    def test_small_fraction(self):
        self.assertAlmostEqual(module_0.truncate_number(1.001), 0.001, places=5)

    def test_large_number(self):
        self.assertAlmostEqual(module_0.truncate_number(123456.789), 0.789, places=5)

    def test_just_below_next_integer(self):
        self.assertAlmostEqual(module_0.truncate_number(9.999999), 0.999999, places=5)


if __name__ == "__main__":
    unittest.main()
# nonce:9822b5f8