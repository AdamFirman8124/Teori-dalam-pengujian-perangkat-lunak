

# Generated at 2026-10-24 16:07:04.074241
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

# Generated at 2026-10-24 16:07:05.412367
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

# Generated at 2026-10-24 16:07:06.732929
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

# Generated at 2026-10-24 16:07:08.122881
# Unit test for function compare
def test_compare():
    # identical -> all zeros
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # general case
    assert module_0.compare([10, 20, 30], [8, 25, 30]) == [2, 5, 0]

    # order doesn't matter due to abs
    assert module_0.compare([3], [5]) == [2]
    assert module_0.compare([5], [3]) == [2]

    # negatives
    assert module_0.compare([-1, -5], [2, 3]) == [3, 8]

    # floats
    assert module_0.compare([1.5, 2.0], [1.0, 2.5]) == [0.5, 0.5]

    # empty
    assert module_0.compare([], []) == []
    assert module_0.compare([], [1, 2]) == []

    # different lengths -> zip truncates to shortest
    assert module_0.compare([1, 2, 3], [1, 2]) == [0, 0]

# Generated at 2026-10-24 16:07:09.554340
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