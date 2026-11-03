

# Generated at 2026-11-02 20:05:43.010970
# Unit test for function truncate_number
def test_truncate_number():
    # Fractional part of a positive number
    assert abs(module_0.truncate_number(3.5) - 0.5) < 1e-9

    # Whole numbers have no fractional part
    assert module_0.truncate_number(2.0) == 0.0
    assert module_0.truncate_number(100.0) == 0.0
    assert module_0.truncate_number(1.0) == 0.0

    # Zero
    assert module_0.truncate_number(0.0) == 0.0

    # Numbers between 0 and 1
    assert abs(module_0.truncate_number(0.25) - 0.25) < 1e-9
    assert abs(module_0.truncate_number(0.75) - 0.75) < 1e-9

    # Larger numbers with fractional parts (floating point tolerance)
    assert abs(module_0.truncate_number(123.456) - 0.456) < 1e-9

    # Negative numbers: Python's % operator yields a result in [0, 1)
    assert abs(module_0.truncate_number(-1.5) - 0.5) < 1e-9
    assert abs(module_0.truncate_number(-0.25) - 0.75) < 1e-9

    # Result is always within [0, 1)
    for value in [0.1, 5.7, 42.999, -3.14, 1e9 + 0.125]:
        frac = module_0.truncate_number(value)
        assert 0.0 <= frac < 1.0

    # For positive values, integer part + fractional part reconstructs the number
    value = 7.89
    assert abs(int(value) + module_0.truncate_number(value) - value) < 1e-9

# Generated at 2026-11-02 20:06:40.773918
# Unit test for function truncate_number
def test_truncate_number():
    # Test with a positive float with fractional part
    assert module_0.truncate_number(3.5) == 0.5

    # Test with another positive float
    assert module_0.truncate_number(2.25) == 0.25

    # Test with an integer value (no fractional part)
    assert module_0.truncate_number(4.0) == 0.0

    # Test with a float less than 1
    assert module_0.truncate_number(0.75) == 0.75

    # Test with a large number
    assert module_0.truncate_number(123456.789) == pytest.approx(0.789)

    # Test with a very small fractional part
    assert module_0.truncate_number(10.001) == pytest.approx(0.001)

    # Test with zero
    assert module_0.truncate_number(0.0) == 0.0

    # Test with a number just below an integer
    assert module_0.truncate_number(5.999999) == pytest.approx(0.999999)

    # Test with a negative float
    # In Python, modulo of a negative number returns a positive result
    # -3.5 % 1.0 == 0.5
    assert module_0.truncate_number(-3.5) == 0.5

    # Test with negative integer value
    assert module_0.truncate_number(-2.0) == 0.0

    # Test with negative float less than -1
    assert module_0.truncate_number(-1.25) == 0.75

    # Test result is always in range [0, 1)
    result = module_0.truncate_number(7.3)
    assert 0 <= result < 1.0

# Generated at 2026-11-02 20:07:43.515519
# Unit test for function truncate_number
def test_truncate_number():
    # Typical positive floats: fractional part is returned
    assert module_0.truncate_number(3.5) == 0.5
    assert module_0.truncate_number(2.25) == 0.25
    assert module_0.truncate_number(123.456) == pytest.approx(0.456)

    # Whole numbers have zero fractional part
    assert module_0.truncate_number(1.0) == 0.0
    assert module_0.truncate_number(100.0) == 0.0

    # Number less than 1 is itself
    assert module_0.truncate_number(0.5) == 0.5
    assert module_0.truncate_number(0.999) == pytest.approx(0.999)

    # Zero
    assert module_0.truncate_number(0.0) == 0.0

    # Negative numbers: Python's % returns value with sign of divisor (positive)
    assert module_0.truncate_number(-1.5) == pytest.approx(0.5)
    assert module_0.truncate_number(-0.25) == pytest.approx(0.75)

    # Result is always in range [0, 1)
    result = module_0.truncate_number(42.731)
    assert 0.0 <= result < 1.0

# Generated at 2026-11-02 20:09:13.822548
# Unit test for function truncate_number
def test_truncate_number():
    # Positive number with fractional part
    assert math.isclose(module_0.truncate_number(3.5), 0.5)
    assert math.isclose(module_0.truncate_number(1.25), 0.25)
    assert math.isclose(module_0.truncate_number(123.456), 0.456)

    # Whole numbers return 0
    assert module_0.truncate_number(5.0) == 0.0
    assert module_0.truncate_number(100.0) == 0.0
    assert module_0.truncate_number(0.0) == 0.0

    # Numbers between 0 and 1
    assert math.isclose(module_0.truncate_number(0.7), 0.7)
    assert math.isclose(module_0.truncate_number(0.999), 0.999)

    # Large numbers
    assert math.isclose(module_0.truncate_number(1e6 + 0.5), 0.5)

    # Negative numbers (Python modulo of negative yields positive remainder)
    assert math.isclose(module_0.truncate_number(-3.5), 0.5)
    assert math.isclose(module_0.truncate_number(-0.25), 0.75)

    # Result is always in [0, 1)
    for value in [3.7, -3.7, 0.0, 12.999, -0.001]:
        result = module_0.truncate_number(value)
        assert 0.0 <= result < 1.0

# Generated at 2026-11-02 20:10:44.027779
# Unit test for function truncate_number
def test_truncate_number():
    # Typical float with a fractional part
    assert math.isclose(module_0.truncate_number(3.5), 0.5)

    # Whole numbers have no fractional part
    assert module_0.truncate_number(5.0) == 0.0
    assert module_0.truncate_number(1.0) == 0.0
    assert module_0.truncate_number(0.0) == 0.0

    # Value smaller than 1
    assert math.isclose(module_0.truncate_number(0.25), 0.25)

    # Larger value with a fractional part
    assert math.isclose(module_0.truncate_number(123.456), 0.456)

    # Value just below the next integer
    assert math.isclose(module_0.truncate_number(3.999), 0.999)

    # Very small fractional part
    assert math.isclose(module_0.truncate_number(2.0001), 0.0001)

    # Negative input: Python's modulo yields the positive fractional part
    assert math.isclose(module_0.truncate_number(-1.5), 0.5)