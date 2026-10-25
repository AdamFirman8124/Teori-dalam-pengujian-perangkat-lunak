

# Generated at 2026-10-25 01:00:06.356861
# Unit test for function any_int

# Generated at 2026-10-25 01:00:08.877892
# Unit test for function any_int

# Generated at 2026-10-25 01:00:11.425365
# Unit test for function any_int

# Generated at 2026-10-25 01:00:13.839567
# Unit test for function any_int

# Generated at 2026-10-25 01:00:16.254064
# Unit test for function any_int

# Generated at 2026-10-25 01:00:18.671559
# Unit test for function any_int

# Generated at 2026-10-25 01:00:26.424577
# Unit test for function any_int
def test_any_int():
    # Each possible pair sums to the third value
    assert module_0.any_int(1, 2, 3) is True
    assert module_0.any_int(1, 3, 2) is True
    assert module_0.any_int(3, 1, 2) is True

    # All integers, but no pair sums to the third
    assert module_0.any_int(1, 2, 4) is False

    # One or more arguments are not integers
    assert module_0.any_int(1.0, 2, 3) is False
    assert module_0.any_int(1, "2", 3) is False
    assert module_0.any_int(1, 2, None) is False

    # Edge cases
    assert module_0.any_int(0, 0, 0) is True
    assert module_0.any_int(-1, -2, -3) is True

# Generated at 2026-10-25 01:00:32.262430
# Unit test for function any_int
def test_any_int():
    assert module_0.any_int(2, 3, 5) is True
    assert module_0.any_int(5, 2, 3) is True
    assert module_0.any_int(2, 5, 3) is True
    assert module_0.any_int(-2, 2, 0) is True

    assert module_0.any_int(1, 2, 4) is False
    assert module_0.any_int(0, 0, 1) is False
    assert module_0.any_int(2.0, 3, 5) is False
    assert module_0.any_int("2", 3, 5) is False


test_any_int()
print("All tests passed.")

# Generated at 2026-10-25 01:00:37.359646
# Unit test for function any_int
def test_any_int():
    # One integer is the sum of the other two
    assert module_0.any_int(2, 3, 5) is True
    assert module_0.any_int(5, 2, 3) is True
    assert module_0.any_int(2, 5, 3) is True

    # No integer is the sum of the other two
    assert module_0.any_int(1, 2, 4) is False

    # Negative and zero values
    assert module_0.any_int(-2, 5, 3) is True
    assert module_0.any_int(0, 0, 0) is True

    # Non-integer arguments
    assert module_0.any_int(2.0, 3, 5) is False
    assert module_0.any_int("2", 3, 5) is False
    assert module_0.any_int(2, None, 5) is False