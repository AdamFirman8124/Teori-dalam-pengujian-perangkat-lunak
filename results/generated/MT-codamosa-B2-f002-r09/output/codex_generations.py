

# Generated at 2026-11-02 09:55:41.831174
# Unit test for function truncate_number
def test_truncate_number():
    # nonce:89252c57
    import math

    # Positive numbers with a fractional part
    assert math.isclose(module_0.truncate_number(3.5), 0.5)
    assert math.isclose(module_0.truncate_number(2.25), 0.25)

    # Whole numbers have no fractional part
    assert module_0.truncate_number(4.0) == 0.0
    assert module_0.truncate_number(100.0) == 0.0
    assert module_0.truncate_number(0.0) == 0.0

    # Numbers between 0 and 1 return themselves
    assert math.isclose(module_0.truncate_number(0.75), 0.75)

    # Negative numbers: Python's % returns a non-negative remainder
    assert math.isclose(module_0.truncate_number(-1.5), 0.5)
    assert math.isclose(module_0.truncate_number(-0.25), 0.75)

    # Large number with fractional part
    assert math.isclose(module_0.truncate_number(123456.789), 0.789)

    # Return type and range checks
    assert isinstance(module_0.truncate_number(3.5), float)
    for value in [3.7, -3.7, 0.0, 99.99, -0.001, 123456.789]:
        result = module_0.truncate_number(value)
        assert 0.0 <= result < 1.0

# Generated at 2026-11-02 09:57:40.923457
# Unit test for function truncate_number
def test_truncate_number():
    # Typical positive float: integer part removed
    assert module_0.truncate_number(3.5) == 0.5
    assert module_0.truncate_number(2.25) == 0.25

    # Value less than 1 returns itself
    assert module_0.truncate_number(0.75) == 0.75

    # Whole number returns 0
    assert module_0.truncate_number(4.0) == 0.0
    assert module_0.truncate_number(0.0) == 0.0

    # Large number with fractional part
    assert module_0.truncate_number(123.456) == pytest.approx(0.456)

    # Negative number: Python modulo yields positive fractional part
    assert module_0.truncate_number(-1.5) == pytest.approx(0.5)
    assert module_0.truncate_number(-3.25) == pytest.approx(0.75)

    # Floating point precision handled via approx
    assert module_0.truncate_number(1.1) == pytest.approx(0.1)

# Generated at 2026-11-02 09:58:28.123492
# Unit test for function truncate_number
def test_truncate_number():
    import math

    # Typical positive float: integer part removed
    assert math.isclose(module_0.truncate_number(3.5), 0.5)
    assert math.isclose(module_0.truncate_number(2.25), 0.25)
    assert math.isclose(module_0.truncate_number(123.456), 0.456, abs_tol=1e-9)

    # Numbers with fractional part < 0.5
    assert math.isclose(module_0.truncate_number(1.1), 0.1, abs_tol=1e-9)
    assert math.isclose(module_0.truncate_number(10.01), 0.01, abs_tol=1e-9)

    # Numbers with fractional part > 0.5
    assert math.isclose(module_0.truncate_number(4.9), 0.9)
    assert math.isclose(module_0.truncate_number(7.75), 0.75)

    # Whole numbers: fractional part is zero
    assert module_0.truncate_number(5.0) == 0.0
    assert module_0.truncate_number(100.0) == 0.0
    assert module_0.truncate_number(0.0) == 0.0

    # Negative numbers: result of % 1.0 is in [0, 1)
    assert math.isclose(module_0.truncate_number(-1.5), 0.5)
    assert math.isclose(module_0.truncate_number(-3.25), 0.75)
    assert module_0.truncate_number(-4.0) == 0.0

    # Numbers between 0 and 1
    assert math.isclose(module_0.truncate_number(0.5), 0.5)
    assert math.isclose(module_0.truncate_number(0.999), 0.999, abs_tol=1e-9)

    # Very large number
    assert math.isclose(module_0.truncate_number(1e10 + 0.7), 0.7, abs_tol=1e-6)

    # Result type check
    assert isinstance(module_0.truncate_number(3.7), float)

    # Result is always within [0, 1)
    for value in [0.1, 1.7, 25.3, -6.9, 1000.123]:
        result = module_0.truncate_number(value)
        assert 0.0 <= result < 1.0

# Generated at 2026-11-02 09:59:39.089340
# Unit test for function truncate_number
def test_truncate_number():
    # Positive numbers with fractional parts
    assert module_0.truncate_number(3.5) == pytest.approx(0.5)
    assert module_0.truncate_number(1.25) == pytest.approx(0.25)
    assert module_0.truncate_number(100.75) == pytest.approx(0.75)
    assert module_0.truncate_number(123.456) == pytest.approx(0.456, abs=1e-9)

    # Whole numbers have no fractional part
    assert module_0.truncate_number(1.0) == pytest.approx(0.0)
    assert module_0.truncate_number(42.0) == pytest.approx(0.0)
    assert module_0.truncate_number(0.0) == pytest.approx(0.0)

    # Fraction less than 1 (no integer part)
    assert module_0.truncate_number(0.5) == pytest.approx(0.5)
    assert module_0.truncate_number(0.123) == pytest.approx(0.123, abs=1e-9)

    # Negative numbers: Python's % returns a positive remainder
    assert module_0.truncate_number(-1.5) == pytest.approx(0.5)
    assert module_0.truncate_number(-3.25) == pytest.approx(0.75)
    assert module_0.truncate_number(-2.0) == pytest.approx(0.0)

    # Very large number
    assert module_0.truncate_number(1e10 + 0.5) == pytest.approx(0.5)

# Generated at 2026-11-02 10:00:49.234872
# Unit test for function truncate_number
def test_truncate_number():
    # Typical positive numbers with fractional parts
    assert module_0.truncate_number(3.5) == 0.5
    assert module_0.truncate_number(1.25) == 0.25
    assert module_0.truncate_number(2.75) == 0.75

    # Whole numbers have no fractional part
    assert module_0.truncate_number(4.0) == 0.0
    assert module_0.truncate_number(0.0) == 0.0
    assert module_0.truncate_number(100.0) == 0.0

    # Numbers strictly between 0 and 1
    assert module_0.truncate_number(0.5) == 0.5
    assert module_0.truncate_number(0.25) == 0.25

    # Floating point precision handling
    assert module_0.truncate_number(123.456) == pytest.approx(0.456)
    assert module_0.truncate_number(123456.789) == pytest.approx(0.789)
    assert module_0.truncate_number(10.0000001) == pytest.approx(1e-07, abs=1e-09)

    # Result is always in the range [0, 1)
    for value in [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]:
        result = module_0.truncate_number(value)
        assert 0.0 <= result < 1.0