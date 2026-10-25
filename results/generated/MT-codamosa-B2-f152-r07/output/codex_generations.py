

# Generated at 2026-10-24 14:49:13.904439
# Unit test for function compare
def test_compare():
    # Exact matches -> 0
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # All wrong -> absolute differences
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Mixed hits and misses
    assert module_0.compare([1, 2, 3, 4], [1, 2, 3, -4]) == [0, 0, 0, 8]

    # Negative numbers
    assert module_0.compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

    # Empty input -> empty output
    assert module_0.compare([], []) == []

    # Unequal lengths raise no error with zip, but should be tested intentionally
    assert module_0.compare([1, 2], [1]) == [0]  # zip truncates â document this behavior

    print("All tests passed!")

test_compare()

# Generated at 2026-10-24 14:49:15.220837
# Unit test for function compare
def test_compare():
    # Exact matches -> 0
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # All wrong -> absolute differences
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Mixed hits and misses
    assert module_0.compare([1, 2, 3, 4], [1, 2, 3, -4]) == [0, 0, 0, 8]

    # Negative numbers
    assert module_0.compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

    # Empty input -> empty output
    assert module_0.compare([], []) == []

    # Unequal lengths raise no error with zip, but should be tested intentionally
    assert module_0.compare([1, 2], [1]) == [0]  # zip truncates â document this behavior

    print("All tests passed!")

test_compare()

# Generated at 2026-10-24 14:49:16.603282
# Unit test for function compare
def test_compare():
    # Exact matches -> 0
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # All wrong -> absolute differences
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Mixed hits and misses
    assert module_0.compare([1, 2, 3, 4], [1, 2, 3, -4]) == [0, 0, 0, 8]

    # Negative numbers
    assert module_0.compare([-1, -2, -3], [-1, -2, -4]) == [0, 0, 1]

    # Empty input -> empty output
    assert module_0.compare([], []) == []

    # Unequal lengths raise no error with zip, but should be tested intentionally
    assert module_0.compare([1, 2], [1]) == [0]  # zip truncates â document this behavior

    print("All tests passed!")

test_compare()

# Generated at 2026-10-24 14:49:19.019149
# Unit test for function compare

# Generated at 2026-10-24 14:49:21.539545
# Unit test for function compare

# Generated at 2026-10-24 14:49:24.054380
# Unit test for function compare

# Generated at 2026-10-24 14:49:26.467266
# Unit test for function compare

# Generated at 2026-10-24 14:49:28.881129
# Unit test for function compare

# Generated at 2026-10-24 14:49:31.293891
# Unit test for function compare