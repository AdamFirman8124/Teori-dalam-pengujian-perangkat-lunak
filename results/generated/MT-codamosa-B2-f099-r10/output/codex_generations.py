

# Generated at 2026-11-03 03:25:22.570563
# Unit test for function closest_integer
def test_closest_integer():
    # No decimal point
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-7") == -7

    # Regular rounding (does not end in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.7") == -16
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0
    assert module_0.closest_integer("999.999") == 1000
    assert module_0.closest_integer("-999.999") == -1000

    # Ends in .5: rounds away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros stripped from string before conversion
    assert module_0.closest_integer("14.50") == 15
    assert module_0.closest_integer("-14.500") == -15
    assert module_0.closest_integer("1.20") == 1
    assert module_0.closest_integer("5.000") == 5
    assert module_0.closest_integer("0.000") == 0
    assert module_0.closest_integer("10.50") == 11
    assert module_0.closest_integer("-10.50") == -11
# nonce:abda9e9f

# Generated at 2026-11-03 03:27:09.856623
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Non-halfway decimals: normal rounding
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0
    assert module_0.closest_integer("0.6") == 1
    assert module_0.closest_integer("-0.6") == -1
    assert module_0.closest_integer("2.7") == 3
    assert module_0.closest_integer("-2.7") == -3

    # Halfway values (.5) round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros stripped before parsing
    assert module_0.closest_integer("10.50") == 11
    assert module_0.closest_integer("-10.50") == -11
    assert module_0.closest_integer("0.50") == 1
    assert module_0.closest_integer("-0.50") == -1
    assert module_0.closest_integer("10.00") == 10
    assert module_0.closest_integer("-10.00") == -10
    assert module_0.closest_integer("1.0") == 1
    assert module_0.closest_integer("-1.0") == -1

    print("All tests passed!")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-11-03 03:29:00.347592
# Unit test for function closest_integer
def test_closest_integer():
    # nonce:8279940c
    # Basic integers (no decimal point)
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Regular rounding (fraction not exactly .5) -> nearest integer
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.7") == -16
    assert module_0.closest_integer("10.4") == 10
    assert module_0.closest_integer("10.6") == 11
    assert module_0.closest_integer("-10.4") == -10
    assert module_0.closest_integer("-10.6") == -11

    # Halfway cases (.5) round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("14.50") == 15
    assert module_0.closest_integer("-14.50") == -15
    assert module_0.closest_integer("2.500") == 3
    assert module_0.closest_integer("-2.500") == -3
    assert module_0.closest_integer("10.50") == 11
    assert module_0.closest_integer("-10.50") == -11

    # Trailing zeros stripped, but result is not a .5 value
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("-10.0") == -10
    assert module_0.closest_integer("1.0") == 1
    assert module_0.closest_integer("0.0") == 0

    # Small decimals near zero
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("0.6") == 1
    assert module_0.closest_integer("-0.4") == 0
    assert module_0.closest_integer("-0.6") == -1

    print("All tests passed!")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-11-03 03:30:45.719470
# Unit test for function closest_integer
def test_closest_integer():
    # Plain integers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("7") == 7

    # Normal rounding of decimals
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.7") == -16
    assert module_0.closest_integer("2.4") == 2
    assert module_0.closest_integer("2.6") == 3

    # Values ending in .5 round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer(".5") == 1
    assert module_0.closest_integer("-.5") == -1

    # Trailing zeros are stripped when a '.' is present
    assert module_0.closest_integer("10.00") == 10
    assert module_0.closest_integer("10.5000") == 11
    assert module_0.closest_integer("-10.50") == -11
    assert module_0.closest_integer("0.0") == 0

    # Values that look like fractions but are not .5
    assert module_0.closest_integer("0.05") == 0
    assert module_0.closest_integer("10.49999") == 10

    # Empty string raises ValueError (float('') fails before the 0 branch)
    try:
        module_0.closest_integer("")
        assert False, "expected ValueError for empty string"
    except ValueError:
        pass

    # Invalid numeric strings raise ValueError
    for bad in ("abc", "1.2.3", "--5"):
        try:
            module_0.closest_integer(bad)
            assert False, "expected ValueError for %r" % bad
        except ValueError:
            pass


if __name__ == "__main__":
    test_closest_integer()
    print("All tests passed.")