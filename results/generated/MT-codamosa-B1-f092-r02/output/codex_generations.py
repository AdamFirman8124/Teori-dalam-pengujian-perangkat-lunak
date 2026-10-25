

# Generated at 2026-10-25 00:18:48.364480
# Unit test for function any_int
def test_any_int():
    # Each possible pair sums to the remaining value
    assert module_0.any_int(1, 2, 3) is True
    assert module_0.any_int(3, 1, 2) is True
    assert module_0.any_int(1, 3, 2) is True

    # Negative integers
    assert module_0.any_int(-1, 2, 1) is True

    # No pair sums to the remaining value
    assert module_0.any_int(1, 2, 4) is False
    assert module_0.any_int(0, 0, 1) is False

    # Non-integer arguments
    assert module_0.any_int(1.0, 2, 3) is False
    assert module_0.any_int("1", 2, 3) is False
    assert module_0.any_int(None, 2, 3) is False

# Generated at 2026-10-25 00:18:53.586297
# Unit test for function any_int
def test_any_int():
    assert module_0.any_int(2, 3, 5) is True
    assert module_0.any_int(5, 2, 3) is True
    assert module_0.any_int(2, 5, 3) is True

    assert module_0.any_int(2, 3, 6) is False
    assert module_0.any_int(1.5, 2, 3) is False
    assert module_0.any_int("2", 2, 4) is False

    assert module_0.any_int(-1, -2, -3) is True
    assert module_0.any_int(0, 0, 0) is True

# Generated at 2026-10-25 00:18:59.630300
# Unit test for function any_int
def test_any_int():
    # Each possible addition order
    assert module_0.any_int(2, 3, 5) is True
    assert module_0.any_int(5, 2, 3) is True
    assert module_0.any_int(2, 5, 3) is True

    # Includes negative numbers and zero
    assert module_0.any_int(-2, 5, 3) is True
    assert module_0.any_int(0, 0, 0) is True

    # No two values add up to the third
    assert module_0.any_int(1, 2, 4) is False

    # Non-integer arguments
    assert module_0.any_int(2.0, 3, 5) is False
    assert module_0.any_int("2", 3, 5) is False
    assert module_0.any_int(2, None, 2) is False

# Generated at 2026-10-25 00:19:05.159694
# Unit test for function any_int
def test_any_int():
    # Each possible pair sums to the third value
    assert module_0.any_int(1, 2, 3) is True
    assert module_0.any_int(3, 1, 2) is True
    assert module_0.any_int(2, 3, 1) is True

    # Integers that do not satisfy the condition
    assert module_0.any_int(1, 2, 4) is False
    assert module_0.any_int(0, 0, 1) is False

    # Negative integers
    assert module_0.any_int(-1, 2, 1) is True

    # Non-integer arguments
    assert module_0.any_int(1.0, 2, 3) is False
    assert module_0.any_int("1", 2, 3) is False
    assert module_0.any_int(1, None, 1) is False

# Generated at 2026-10-25 00:19:13.350011
# Unit test for function any_int
def test_any_int():
    # Each possible addition order
    assert module_0.any_int(2, 3, 5) is True
    assert module_0.any_int(2, 5, 3) is True
    assert module_0.any_int(5, 2, 3) is True

    # Negative and zero values
    assert module_0.any_int(-2, 5, 3) is True
    assert module_0.any_int(0, 0, 0) is True

    # No two values add up to the third
    assert module_0.any_int(1, 2, 4) is False

    # Non-integer arguments
    assert module_0.any_int(2.0, 3, 5) is False
    assert module_0.any_int("2", 3, 5) is False
    assert module_0.any_int(None, 3, 5) is False