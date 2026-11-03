

# Generated at 2026-11-02 10:53:42.231200
# Unit test for function closest_integer
def test_closest_integer():
    # Basic integer strings
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Regular rounding (non-.5 fractions)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("2.4") == 2
    assert module_0.closest_integer("2.6") == 3
    assert module_0.closest_integer("-2.4") == -2
    assert module_0.closest_integer("-2.6") == -3

    # .5 cases: round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("1.5") == 2
    assert module_0.closest_integer("-1.5") == -2
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros removed before parsing
    assert module_0.closest_integer("14.500") == 15
    assert module_0.closest_integer("-14.500") == -15
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("100.000") == 100
    assert module_0.closest_integer("2.50") == 3
    assert module_0.closest_integer("-2.50") == -3

# Generated at 2026-11-02 10:55:27.753141
# Unit test for function closest_integer
def test_closest_integer():
    # Basic integers (no decimal point)
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("5") == 5

    # Regular rounding (not a .5 tie)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.7") == -16
    assert module_0.closest_integer("123.456") == 123

    # .5 ties round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer(".5") == 1
    assert module_0.closest_integer("-.5") == -1
    assert module_0.closest_integer("999.5") == 1000
    assert module_0.closest_integer("-999.5") == -1000
    assert module_0.closest_integer("123456789.5") == 123456790

    # Trailing zeros are stripped before the '.5' check
    assert module_0.closest_integer("10.50") == 11
    assert module_0.closest_integer("-10.50") == -11
    assert module_0.closest_integer("2.500") == 3
    assert module_0.closest_integer("-2.500") == -3
    assert module_0.closest_integer(".500") == 1
    assert module_0.closest_integer("10.00") == 10
    assert module_0.closest_integer("0.0") == 0

    # Values that reduce to whole numbers after stripping zeros
    assert module_0.closest_integer("1.0") == 1
    assert module_0.closest_integer("-1.0") == -1
    assert module_0.closest_integer("100.000") == 100
    assert module_0.closest_integer("-100.000") == -100

    # Empty string is not a valid float
    try:
        module_0.closest_integer("")
        assert False, "expected ValueError for empty string"
    except ValueError:
        pass

# Generated at 2026-11-02 10:57:13.658716
# Unit test for function closest_integer
def test_closest_integer():
    # Basic rounding (nearest integer)
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("1.234") == 1
    assert module_0.closest_integer("1.7") == 2
    assert module_0.closest_integer("-1.7") == -2
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    # Equidistant cases: must round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3      # Python's round would give 2
    assert module_0.closest_integer("-2.5") == -3    # Python's round would give -2
    assert module_0.closest_integer("10.5") == 11
    assert module_0.closest_integer("-10.5") == -11

    # Trailing zeros are stripped before parsing
    assert module_0.closest_integer("10.50") == 11
    assert module_0.closest_integer("-10.50") == -11
    assert module_0.closest_integer("2.50") == 3
    assert module_0.closest_integer("1.0") == 1
    assert module_0.closest_integer("-1.0") == -1
    assert module_0.closest_integer("0.0") == 0

    # Integer strings (including leading zeros)
    assert module_0.closest_integer("100") == 100
    assert module_0.closest_integer("-100") == -100
    assert module_0.closest_integer("007") == 7

    print("All tests passed.")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-11-02 11:00:35.436270
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Standard rounding (no tie)
    assert module_0.closest_integer("15.6") == 16
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("-15.6") == -16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("0.6") == 1
    assert module_0.closest_integer("-0.4") == 0
    assert module_0.closest_integer("-0.6") == -1

    # Ties round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("999.5") == 1000
    assert module_0.closest_integer("-999.5") == -1000

    # Trailing zeros are stripped before the tie check
    assert module_0.closest_integer("14.500") == 15
    assert module_0.closest_integer("-14.500") == -15
    assert module_0.closest_integer("2.50") == 3
    assert module_0.closest_integer("0.50") == 1
    assert module_0.closest_integer("-0.50") == -1
    assert module_0.closest_integer("10.0") == 10

    # Larger fractional values
    assert module_0.closest_integer("123.456") == 123
    assert module_0.closest_integer("-123.456") == -123

    print("All tests passed.")