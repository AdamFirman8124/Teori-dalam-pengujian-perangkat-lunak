

# Generated at 2026-10-24 19:36:47.219390
# Unit test for function truncate_number
def test_truncate_number():
    # Typical positive floats
    assert module_0.truncate_number(3.5) == 0.5
    assert module_0.truncate_number(123.456) == 0.456
    assert module_0.truncate_number(0.25) == 0.25

    # Whole numbers -> fractional part is 0
    assert module_0.truncate_number(7.0) == 0.0
    assert module_0.truncate_number(100.0) == 0.0

    # Negative numbers: Python's % returns a non-negative result
    assert module_0.truncate_number(-1.5) == 0.5   # -1.5 % 1.0 == 0.5
    assert module_0.truncate_number(-3.0) == 0.0

    # Very small / large values
    assert module_0.truncate_number(1e9 + 0.75) == 0.75
    assert module_0.truncate_number(1e-9) == 1e-9

    print("All tests passed!")


test_truncate_number()

# Generated at 2026-10-24 19:36:48.548200
# Unit test for function truncate_number
def test_truncate_number():
    # Typical positive floats
    assert module_0.truncate_number(3.5) == 0.5
    assert module_0.truncate_number(123.456) == 0.456
    assert module_0.truncate_number(0.25) == 0.25

    # Whole numbers -> fractional part is 0
    assert module_0.truncate_number(7.0) == 0.0
    assert module_0.truncate_number(100.0) == 0.0

    # Negative numbers: Python's % returns a non-negative result
    assert module_0.truncate_number(-1.5) == 0.5   # -1.5 % 1.0 == 0.5
    assert module_0.truncate_number(-3.0) == 0.0

    # Very small / large values
    assert module_0.truncate_number(1e9 + 0.75) == 0.75
    assert module_0.truncate_number(1e-9) == 1e-9

    print("All tests passed!")


test_truncate_number()

# Generated at 2026-10-24 19:36:50.969861
# Unit test for function truncate_number

# Generated at 2026-10-24 19:36:53.385109
# Unit test for function truncate_number

# Generated at 2026-10-24 19:36:56.003541
# Unit test for function truncate_number

# Generated at 2026-10-24 19:36:58.523454
# Unit test for function truncate_number

# Generated at 2026-10-24 19:37:00.939760
# Unit test for function truncate_number

# Generated at 2026-10-24 19:37:03.357346
# Unit test for function truncate_number

# Generated at 2026-10-24 19:37:08.076778
# Unit test for function truncate_number
def test_truncate_number():
    assert module_0.truncate_number(3.5) == 0.5
    assert module_0.truncate_number(123.456) == 0.456
    assert module_0.truncate_number(0.25) == 0.25
    assert module_0.truncate_number(10.0) == 0.0
    assert module_0.truncate_number(-1.75) == 0.25  # Python modulo returns non-negative for positive divisor
    assert module_0.truncate_number(7.0) == 0.0
    assert abs(module_0.truncate_number(2.999) - 0.999) < 1e-9  # floating point tolerance