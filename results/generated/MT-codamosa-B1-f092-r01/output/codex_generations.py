

# Generated at 2026-10-25 01:12:08.014992
# Unit test for function any_int
def test_any_int():
    assert module_0.any_int(1, 2, 3) is True
    assert module_0.any_int(3, 1, 2) is True
    assert module_0.any_int(1, 3, 2) is True
    assert module_0.any_int(-2, 5, 3) is True
    assert module_0.any_int(0, 0, 0) is True

    assert module_0.any_int(1, 2, 4) is False
    assert module_0.any_int(-1, -2, 4) is False

    assert module_0.any_int(1.0, 2, 3) is False
    assert module_0.any_int("1", 2, 3) is False
    assert module_0.any_int(None, 2, 3) is False

# Generated at 2026-10-25 01:12:19.614628
# Unit test for function any_int
def test_any_int():
    # Each possible pair sums to the third value
    assert module_0.any_int(1, 2, 3) is True
    assert module_0.any_int(3, 1, 2) is True
    assert module_0.any_int(2, 3, 1) is True

    # Negative and zero values
    assert module_0.any_int(-2, 5, 3) is True
    assert module_0.any_int(0, 0, 0) is True

    # No two values sum to the third
    assert module_0.any_int(1, 2, 4) is False
    assert module_0.any_int(-1, -2, 5) is False

    # Non-integer arguments
    assert module_0.any_int(1.0, 2, 3) is False
    assert module_0.any_int(1, "2", 3) is False
    assert module_0.any_int(1, 2, None) is False

# Generated at 2026-10-25 01:12:22.031118
# Unit test for function any_int

# Generated at 2026-10-25 01:12:24.552739
# Unit test for function any_int

# Generated at 2026-10-25 01:12:26.967322
# Unit test for function any_int

# Generated at 2026-10-25 01:12:29.507678
# Unit test for function any_int

# Generated at 2026-10-25 01:12:31.923430
# Unit test for function any_int

# Generated at 2026-10-25 01:12:34.337136
# Unit test for function any_int

# Generated at 2026-10-25 01:12:36.913879
# Unit test for function any_int

# Generated at 2026-10-25 01:12:39.328562
# Unit test for function any_int

# Generated at 2026-10-25 01:12:41.747787
# Unit test for function any_int