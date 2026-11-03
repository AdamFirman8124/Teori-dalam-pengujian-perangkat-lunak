

# Generated at 2026-11-03 01:17:13.993285
# Unit test for function closest_integer
def test_closest_integer():
    # Integer strings
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-10") == -10
    assert module_0.closest_integer("0") == 0

    # Normal rounding (not ending in .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("3.7") == 4
    assert module_0.closest_integer("-3.7") == -4
    assert module_0.closest_integer("15.4") == 15
    assert module_0.closest_integer("-15.4") == -15

    # Halfway values round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros are stripped before the .5 check
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("1.50") == 2
    assert module_0.closest_integer("-1.50") == -2
    assert module_0.closest_integer("2.500") == 3
    assert module_0.closest_integer("-2.500") == -3

    # No leading integer digit
    assert module_0.closest_integer(".5") == 1
    assert module_0.closest_integer("-.5") == -1

    # Return type is int
    assert isinstance(module_0.closest_integer("14.5"), int)
    assert isinstance(module_0.closest_integer("10"), int)

    print("All tests passed!")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-11-03 01:18:28.938162
# Unit test for function closest_integer
def test_closest_integer():
    # Basic integers (no decimal point)
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-3") == -3

    # Non-halfway decimals: standard rounding
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("2.7") == 3
    assert module_0.closest_integer("-2.7") == -3

    # Halfway values: round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros are stripped before rounding
    assert module_0.closest_integer("2.50") == 3
    assert module_0.closest_integer("-2.50") == -3
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("3.500") == 4

    # Values that round to zero
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    # Edge case: empty string
    assert module_0.closest_integer("") == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_closest_integer()

# Generated at 2026-11-03 01:19:27.813487
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-0") == 0
    assert module_0.closest_integer("-10") == -10

    # Regular rounding (nearest integer)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.7") == -16

    # Halfway values round away from zero
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15

    # Trailing zeros are stripped before evaluation
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("-10.0") == -10
    assert module_0.closest_integer("10.50") == 11
    assert module_0.closest_integer("1.000") == 1

# Generated at 2026-11-03 01:20:29.554282
# Unit test for function closest_integer
def test_closest_integer():
    # Basic integer strings
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-5") == -5

    # Normal rounding (not .5)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.7") == -16
    assert module_0.closest_integer("1.4") == 1
    assert module_0.closest_integer("1.6") == 2
    assert module_0.closest_integer("-1.4") == -1
    assert module_0.closest_integer("-1.6") == -2

    # .5 case rounds away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros removed before .5 detection
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("2.50") == 3
    assert module_0.closest_integer("-2.50") == -3
    assert module_0.closest_integer("14.5000") == 15
    assert module_0.closest_integer("-14.5000") == -15
    assert module_0.closest_integer("0.00") == 0

# nonce:a42de357

# Generated at 2026-11-03 01:21:53.112048
# Unit test for function closest_integer
def test_closest_integer():
    # Basic integer strings
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-5") == -5
    assert module_0.closest_integer("100") == 100

    # Regular rounding (non-.5 fractions)
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.7") == -16
    assert module_0.closest_integer("3.50001") == 4

    # .5 values round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("1.5") == 2
    assert module_0.closest_integer("-1.5") == -2

    # Trailing zeros stripped before parsing
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("10.00") == 10
    assert module_0.closest_integer("14.50") == 15
    assert module_0.closest_integer("-14.50") == -15
    assert module_0.closest_integer("0.50") == 1
    assert module_0.closest_integer("-0.50") == -1

    # Fractional forms without leading digit
    assert module_0.closest_integer(".5") == 1
    assert module_0.closest_integer("-.5") == -1

    print("All tests passed!")


test_closest_integer()

# Generated at 2026-11-03 01:23:23.032567
# Unit test for function closest_integer
def test_closest_integer():
# nonce:8c20954b
    # Whole numbers
    assert closest

# Generated at 2026-11-03 01:25:21.941772
# Unit test for function closest_integer
def test_closest_integer():
    # Plain integers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-5") == -5
    assert module_0.closest_integer("100") == 100

    # Standard rounding (non .5 fractions)
    assert module_0.closest_integer("15.6") == 16
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("0.6") == 1
    assert module_0.closest_integer("-12.7") == -13
    assert module_0.closest_integer("-1.4") == -1
    assert module_0.closest_integer("-0.4") == 0
    assert module_0.closest_integer("-0.6") == -1
    assert module_0.closest_integer("2.6") == 3

    # Ties (.5) must round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros stripped before parsing
    assert module_0.closest_integer("2.50") == 3
    assert module_0.closest_integer("-2.50") == -3
    assert module_0.closest_integer("1.0") == 1
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("14.500") == 15
    assert module_0.closest_integer("-14.500") == -15
    assert module_0.closest_integer("0.000") == 0

    print("All tests passed!")


if __name__ == "__main__":
    test_closest_integer()