

# Generated at 2026-11-02 19:35:35.148969
# Unit test for function truncate_number
def test_truncate_number():
    # Typical positive values with fractional parts
    assert math.isclose(module_0.truncate_number(3.5), 0.5)
    assert math.isclose(module_0.truncate_number(1.25), 0.25)
    assert math.isclose(module_0.truncate_number(123.456), 0.456)

    # Whole numbers have no fractional part
    assert math.isclose(module_0.truncate_number(2.0), 0.0)
    assert math.isclose(module_0.truncate_number(100.0), 0.0)

    # Zero input
    assert math.isclose(module_0.truncate_number(0.0), 0.0)

    # Value smaller than 1 returns itself
    assert math.isclose(module_0.truncate_number(0.75), 0.75)

    # Negative number: Python's % yields result with sign of divisor
    assert math.isclose(module_0.truncate_number(-1.5), 0.5)
    assert math.isclose(module_0.truncate_number(-3.25), 0.75)

    # Large value
    assert math.isclose(module_0.truncate_number(1000000.999), 0.999)

# Generated at 2026-11-02 19:37:27.171755
# Unit test for function truncate_number
def test_truncate_number():
    # Positive numbers with fractional parts
    assert math.isclose(module_0.truncate_number(3.5), 0.5)
    assert math.isclose(module_0.truncate_number(2.25), 0.25)
    assert math.isclose(module_0.truncate_number(1.33), 0.33, abs_tol=1e-6)
    assert math.isclose(module_0.truncate_number(123.456), 0.456, abs_tol=1e-6)

    # Whole numbers should return 0.0
    assert module_0.truncate_number(4.0) == 0.0
    assert module_0.truncate_number(100.0) == 0.0
    assert module_0.truncate_number(0.0) == 0.0

    # Numbers less than 1 return themselves
    assert math.isclose(module_0.truncate_number(0.5), 0.5)
    assert math.isclose(module_0.truncate_number(0.123), 0.123, abs_tol=1e-6)

    # Negative numbers: Python's % yields positive fractional part
    assert math.isclose(module_0.truncate_number(-3.5), 0.5)
    assert math.isclose(module_0.truncate_number(-1.25), 0.75)

    # Large numbers keep only the fractional part
    assert math.isclose(module_0.truncate_number(1e10 + 0.5), 0.5)

    # Result must always lie in [0.0, 1.0)
    for value in [3.7, -3.7, 0.0, 10.25, -10.25, 999.999]:
        result = module_0.truncate_number(value)
        assert 0.0 <= result < 1.0, f"Result {result} out of range for input {value}"

# Generated at 2026-11-02 19:39:21.189996
# Unit test for function truncate_number
def test_truncate_number():
    # Fractional part of a positive decimal number
    assert math.isclose(module_0.truncate_number(3.5), 0.5)

    # Whole numbers have no fractional part
    assert module_0.truncate_number(4.0) == 0.0
    assert module_0.truncate_number(0.0) == 0.0

    # Number smaller than 1 returns itself
    assert math.isclose(module_0.truncate_number(0.25), 0.25)

    # Large number with fractional part (allow float precision error)
    assert math.isclose(module_0.truncate_number(123.456), 0.456, abs_tol=1e-9)

    # Very small fractional part
    assert math.isclose(module_0.truncate_number(1.0000001), 0.0000001, abs_tol=1e-12)

    # Negative number: Python's % yields a positive remainder
    assert math.isclose(module_0.truncate_number(-3.5), 0.5)

    # Result is always in the range [0, 1)
    result = module_0.truncate_number(7.77)
    assert 0.0 <= result < 1.0
    assert math.isclose(result, 0.77, abs_tol=1e-9)

# Generated at 2026-11-02 19:40:57.694860
# Unit test for function truncate_number
def test_truncate_number():
    # Numbers with a fractional part
    assert math.isclose(module_0.truncate_number(3.5), 0.5)
    assert math.isclose(module_0.truncate_number(1.25), 0.25)
    assert math.isclose(module_0.truncate_number(123.456), 0.456)

    # Whole numbers have no fractional part
    assert module_0.truncate_number(2.0) == 0.0
    assert module_0.truncate_number(100.0) == 0.0

    # Numbers less than one
    assert math.isclose(module_0.truncate_number(0.5), 0.5)
    assert math.isclose(module_0.truncate_number(0.001), 0.001)

    # Zero
    assert module_0.truncate_number(0.0) == 0.0

    # Negative numbers: Python's % returns a non-negative result for positive divisor
    assert math.isclose(module_0.truncate_number(-3.5), 0.5)
    assert math.isclose(module_0.truncate_number(-1.25), 0.75)

    # Floating point precision edge case
    assert math.isclose(module_0.truncate_number(1.1), 0.1)

    # Result is always in the range [0, 1)
    for n in [3.7, -2.9, 0.0, 15.999, -0.123, 42.0]:
        result = module_0.truncate_number(n)
        assert 0.0 <= result < 1.0

# Generated at 2026-11-02 19:43:31.202605
# Unit test for function truncate_number
def test_truncate_number():
    # Typical positive float
    assert math.isclose(module_0.truncate_number(3.5), 0.5)
    assert math.isclose(module_0.truncate_number(1.25), 0.25)
    assert math.isclose(module_0.truncate_number(123.456), 0.456, abs_tol=1e-9)

    # Whole numbers have no fractional part
    assert module_0.truncate_number(5.0) == 0.0
    assert module_0.truncate_number(0.0) == 0.0

    # Negative numbers: Python's % returns non-negative result for positive divisor
    assert math.isclose(module_0.truncate_number(-3.5), 0.5)
    assert module_0.truncate_number(-4.0) == 0.0

    # Result is always in the range [0, 1)
    for value in [10.7, -10.7, 0.001, -0.001, 99.999]:
        frac = module_0.truncate_number(value)
        assert 0.0 <= frac < 1.0
        # Reconstructing the integer part should recover the original value
        assert math.isclose(int(value) + frac, value, abs_tol=1e-9)

    # Very large number
    assert math.isclose(module_0.truncate_number(1e10 + 0.123), 0.123, abs_tol=1e-9)