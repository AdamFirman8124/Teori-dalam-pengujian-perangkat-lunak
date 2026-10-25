

# Generated at 2026-10-25 00:17:38.733773
# Unit test for function any_int
def test_any_int():
    # Two values add up to the third
    assert module_0.any_int(2, 3, 5) is True
    assert module_0.any_int(2, 5, 3) is True
    assert module_0.any_int(5, 2, 3) is True

    # No two values add up to the third
    assert module_0.any_int(1, 2, 4) is False

    # Negative numbers and zero
    assert module_0.any_int(-2, 5, 3) is True
    assert module_0.any_int(0, 0, 0) is True

    # All arguments must be integers
    assert module_0.any_int(2.0, 3, 5) is False
    assert module_0.any_int(2, "3", 5) is False
    assert module_0.any_int(None, 3, 5) is False

# Generated at 2026-10-25 00:17:46.411695
# Unit test for function any_int
def test_any_int():
    # Each possible addition order
    assert module_0.any_int(2, 3, 5) is True
    assert module_0.any_int(2, 5, 3) is True
    assert module_0.any_int(5, 2, 3) is True

    # Integers that do not satisfy the condition
    assert module_0.any_int(1, 2, 4) is False

    # Negative numbers and zero
    assert module_0.any_int(-2, 5, 3) is True
    assert module_0.any_int(0, 0, 0) is True

    # Non-integer arguments
    assert module_0.any_int(2.0, 3, 5) is False
    assert module_0.any_int("2", 3, 5) is False
    assert module_0.any_int(None, 3, 5) is False

# Generated at 2026-10-25 00:17:51.839122
# Unit test for function any_int
def test_any_int():
    # One integer is the sum of the other two
    assert module_0.any_int(2, 3, 5) is True
    assert module_0.any_int(5, 2, 3) is True
    assert module_0.any_int(2, 5, 3) is True

    # No integer is the sum of the other two
    assert module_0.any_int(1, 2, 4) is False

    # Inputs must all be integers
    assert module_0.any_int(2.0, 3, 5) is False
    assert module_0.any_int("2", 3, 5) is False
    assert module_0.any_int(2, None, 2) is False


test_any_int()
print("All tests passed.")

# Generated at 2026-10-25 00:17:59.211333
# Unit test for function any_int
def test_any_int():
    # Each possible addition order
    assert module_0.any_int(2, 3, 5) is True
    assert module_0.any_int(5, 3, 2) is True
    assert module_0.any_int(2, 5, 3) is True

    # Negative and zero values
    assert module_0.any_int(-2, 5, 3) is True
    assert module_0.any_int(0, 4, 4) is True

    # No two numbers add up to the third
    assert module_0.any_int(1, 2, 4) is False

    # Non-integer arguments
    assert module_0.any_int(2.0, 3, 5) is False
    assert module_0.any_int(2, "3", 5) is False
    assert module_0.any_int(None, 3, 5) is False

# Generated at 2026-10-25 00:18:06.006829
# Unit test for function any_int
def test_any_int():
    assert module_0.any_int(2, 3, 5) is True
    assert module_0.any_int(5, 2, 3) is True
    assert module_0.any_int(2, 5, 3) is True
    assert module_0.any_int(-2, 5, 3) is True

    assert module_0.any_int(1, 2, 4) is False
    assert module_0.any_int(2.0, 3, 5) is False
    assert module_0.any_int("2", 3, 5) is False
    assert module_0.any_int(1, None, 1) is False