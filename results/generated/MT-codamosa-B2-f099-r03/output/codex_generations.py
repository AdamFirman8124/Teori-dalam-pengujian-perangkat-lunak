

# Generated at 2026-11-03 03:00:18.504570
# Unit test for function closest_integer
def test_closest_integer():
    # Whole numbers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("0") == 0
    assert module_0.closest_integer("-10") == -10

    # Non-halfway decimals: standard rounding
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("-15.7") == -16

    # Halfway cases (.5): round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("15.5") == 16
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("-15.5") == -16
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1

    # Trailing zeros stripped so '.5' rule still applies
    assert module_0.closest_integer("14.50") == 15
    assert module_0.closest_integer("14.500") == 15
    assert module_0.closest_integer("-14.50") == -15
    assert module_0.closest_integer("2.50") == 3
    assert module_0.closest_integer("-2.50") == -3
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("0.0") == 0

    # Small fractional values
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("0.6") == 1
    assert module_0.closest_integer("-0.4") == 0
    assert module_0.closest_integer("-0.6") == -1

    # Large values
    assert module_0.closest_integer("123456789.5") == 123456790
    assert module_0.closest_integer("-123456789.5") == -123456790

# Generated at 2026-11-03 03:03:42.672132
# Unit test for function closest_integer

# Generated at 2026-11-03 03:05:21.903334
# Unit test for function closest_integer
def test_closest_integer():
    # Basic positive integer string
    assert module_0.closest_integer("10") == 10

    # Rounding down (fraction below .5)
    assert module_0.closest_integer("15.3") == 15

    # Rounding up (fraction above .5)
    assert module_0.closest_integer("15.7") == 16

    # .5 rounds away from zero for positives
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("0.5") == 1

    # .5 rounds away from zero for negatives
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("-2.5") == -3
    assert module_0.closest_integer("-0.5") == -1

    # Negative non-.5 values round normally
    assert module_0.closest_integer("-15.7") == -16
    assert module_0.closest_integer("-15.3") == -15

    # Trailing zeros after decimal point are stripped, still treated as .5
    assert module_0.closest_integer("10.50") == 11
    assert module_0.closest_integer("10.500") == 11
    assert module_0.closest_integer("-10.50") == -11

    # Trailing zeros on a whole number
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("-10.0") == -10

    # Small values
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0
    assert module_0.closest_integer("1.5") == 2
    assert module_0.closest_integer("-1.5") == -2

# Generated at 2026-11-03 03:08:10.853614
# Unit test for function closest_integer
def test_closest_integer():
    # Plain integers
    assert module_0.closest_integer("10") == 10
    assert module_0.closest_integer("-3") == -3
    assert module_0.closest_integer("0") == 0

    # Normal rounding (round half to even via Python's round)
    assert module_0.closest_integer("1.4") == 1
    assert module_0.closest_integer("1.6") == 2
    assert module_0.closest_integer("-1.4") == -1
    assert module_0.closest_integer("-1.6") == -2
    assert module_0.closest_integer("0.4") == 0
    assert module_0.closest_integer("-0.4") == 0

    # Halfway values round away from zero
    assert module_0.closest_integer("14.5") == 15
    assert module_0.closest_integer("-14.5") == -15
    assert module_0.closest_integer("0.5") == 1
    assert module_0.closest_integer("-0.5") == -1
    assert module_0.closest_integer(".5") == 1
    assert module_0.closest_integer("-.5") == -1
    assert module_0.closest_integer("2.5") == 3
    assert module_0.closest_integer("-2.5") == -3

    # Trailing zeros stripped before deciding
    assert module_0.closest_integer("10.0") == 10
    assert module_0.closest_integer("10.00") == 10
    assert module_0.closest_integer("2.50") == 3      # becomes "2.5" -> away from zero
    assert module_0.closest_integer("-2.50") == -3    # becomes "-2.5" -> away from zero
    assert module_0.closest_integer("0.00") == 0
    assert module_0.closest_integer("-14.50") == -15

    # More decimal cases
    assert module_0.closest_integer("15.3") == 15
    assert module_0.closest_integer("-15.3") == -15
    assert module_0.closest_integer("15.7") == 16
    assert module_0.closest_integer("-15.7") == -16

    print("All tests passed!")


test_closest_integer()