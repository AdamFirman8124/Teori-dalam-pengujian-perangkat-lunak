

# Generated at 2026-11-02 09:21:06.413337
# Unit test for function truncate_number
def test_truncate_number():
    # Typical positive float: fractional part
    assert module_0.truncate_number(3.5) == 0.5
    assert module_0.truncate_number(1.25) == 0.25

    # Whole number: fractional part is zero
    assert module_0.truncate_number(4.0) == 0.0
    assert module_0.truncate_number(100) == 0.0

    # Number less than 1
    assert module_0.truncate_number(0.75) == 0.75
    assert module_0.truncate_number(0.0) == 0.0

    # Negative numbers: modulo yields positive fractional part
    assert module_0.truncate_number(-1.5) == 0.5
    assert module_0.truncate_number(-3.0) == 0.0

    # Large values
    assert module_0.truncate_number(123456.789) == 0.789

    # Floating point precision tolerance
    assert abs(module_0.truncate_number(2.7) - 0.7) < 1e-9
    assert abs(module_0.truncate_number(10.333) - 0.333) < 1e-9

    # Result is always in [0, 1)
    for value in [-10.7, -1.0, 0.0, 0.999, 5.5, 999.123]:
        result = module_0.truncate_number(value)
        assert 0.0 <= result < 1.0, f"Result {result} out of range for input {value}"

    print("All tests passed!")


class TestTruncateNumber(unittest.TestCase):

    def test_positive_fractional(self):
        self.assertEqual(module_0.truncate_number(3.5), 0.5)

    def test_whole_number(self):
        self.assertEqual(module_0.truncate_number(4.0), 0.0)

    def test_less_than_one(self):
        self.assertEqual(module_0.truncate_number(0.75), 0.75)

    def test_zero(self):
        self.assertEqual(module_0.truncate_number(0.0), 0.0)

    def test_negative_number(self):
        self.assertEqual(module_0.truncate_number(-1.5), 0.5)

    def test_negative_whole(self):
        self.assertEqual(module_0.truncate_number(-3.0), 0.0)

    def test_precision(self):
        self.assertAlmostEqual(module_0.truncate_number(2.7), 0.7)

    def test_result_range(self):
        for value in [-10.7, 0.0, 5.5, 999.123]:
            with self.subTest(value=value):
                result = module_0.truncate_number(value)
                self.assertTrue(0.0 <= result < 1.0)


if __name__ == "__main__":
    test_truncate_number()
    unittest.main()

# Generated at 2026-11-02 09:23:34.650654
# Unit test for function truncate_number
def test_truncate_number():
    assert module_0.truncate_number(3.5) == 0.5
    assert module_0.truncate_number(1.0) == 0.0
    assert module_0.truncate_number(2.75) == 0.75
    assert module_0.truncate_number(0.5) == 0.5
    assert module_0.truncate_number(100.25) == 0.25
    assert module_0.truncate_number(7.0) == 0.0
    assert abs(module_0.truncate_number(3.14159) - 0.14159) < 1e-6

# Generated at 2026-11-02 09:26:15.105054
# Unit test for function truncate_number
def test_truncate_number():
    # Basic case: integer part with decimal fraction
    assert module_0.truncate_number(3.5) == 0.5
    assert module_0.truncate_number(1.25) == 0.25

    # Whole numbers have no decimal part
    assert module_0.truncate_number(2.0) == 0.0
    assert module_0.truncate_number(0.0) == 0.0
    assert module_0.truncate_number(100.0) == 0.0

    # Larger numbers with fractional parts (use tolerance for float precision)
    assert abs(module_0.truncate_number(123.456) - 0.456) < 1e-9
    assert abs(module_0.truncate_number(100.1) - 0.1) < 1e-6

    # Negative numbers: Python's % returns result with sign of divisor (positive)
    assert module_0.truncate_number(-1.5) == 0.5
    assert module_0.truncate_number(-3.25) == 0.75

    # Fraction less than 1 stays unchanged
    assert module_0.truncate_number(0.75) == 0.75

# Generated at 2026-11-02 09:28:29.903326
# Unit test for function truncate_number
def test_truncate_number():
    # Typical positive floats with fractional parts
    assert module_0.truncate_number(3.5) == pytest.approx(0.5)
    assert module_0.truncate_number(2.25) == pytest.approx(0.25)
    assert module_0.truncate_number(123.456) == pytest.approx(123.456 % 1.0)

    # Whole numbers have no fractional part
    assert module_0.truncate_number(4.0) == pytest.approx(0.0)
    assert module_0.truncate_number(100.0) == pytest.approx(0.0)

    # Zero
    assert module_0.truncate_number(0.0) == pytest.approx(0.0)

    # Negative numbers: Python's % yields a non-negative fractional part
    assert module_0.truncate_number(-1.5) == pytest.approx(0.5)
    assert module_0.truncate_number(-2.75) == pytest.approx(0.25)

    # Number just below the next integer
    assert module_0.truncate_number(0.9999999) == pytest.approx(0.9999999)

    # Result must always lie in [0.0, 1.0)
    result = module_0.truncate_number(7.123456)
    assert 0.0 <= result < 1.0
    assert result == pytest.approx(0.123456)


@pytest.mark.parametrize(
    "number, expected",
    [
        (3.5, 0.5),
        (1.33, 0.33),
        (2.0, 0.0),
        (0.0, 0.0),
        (-0.5, 0.5),
        (1e10 + 0.5, 0.5),
    ],
)
def test_truncate_number_parametrized(number, expected):
    assert module_0.truncate_number(number) == pytest.approx(expected)