

# Generated at 2026-10-25 11:04:57.708446
# Unit test for function rolling_max
def test_rolling_max():
    # Basic case
    assert module_0.rolling_max([1, 2, 3, 2, 1]) == [1, 2, 3, 3, 3]

    # Single element
    assert module_0.rolling_max([5]) == [5]

    # Empty list
    assert module_0.rolling_max([]) == []

    # Decreasing sequence
    assert module_0.rolling_max([9, 8, 7, 6]) == [9, 9, 9, 9]

    # Increasing sequence
    assert module_0.rolling_max([1, 3, 5, 7]) == [1, 3, 5, 7]

    # Negative numbers
    assert module_0.rolling_max([-5, -1, -10, -2]) == [-5, -1, -1, -1]

    # Duplicates
    assert module_0.rolling_max([4, 4, 4]) == [4, 4, 4]

    print("All tests passed!")


test_rolling_max()

# Generated at 2026-10-25 11:05:04.774062
# Unit test for function rolling_max
def test_rolling_max():
    assert module_0.rolling_max([3, 1, 4, 2, 5]) == [3, 3, 4, 4, 5]
    assert module_0.rolling_max([-3, -1, -4, -2]) == [-3, -1, -1, -1]
    assert module_0.rolling_max([]) == []
    assert module_0.rolling_max([7]) == [7]
    assert module_0.rolling_max([2, 2, 2]) == [2, 2, 2]

# Generated at 2026-10-25 11:05:12.146499
# Unit test for function rolling_max
def test_rolling_max():
    assert module_0.rolling_max([]) == []
    assert module_0.rolling_max([1]) == [1]
    assert module_0.rolling_max([1, 3, 2, 5, 4]) == [1, 3, 3, 5, 5]
    assert module_0.rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]
    assert module_0.rolling_max([-3, -1, -2, 0, -4]) == [-3, -1, -1, 0, 0]
    assert module_0.rolling_max([2, 2, 2]) == [2, 2, 2]

# Generated at 2026-10-25 11:05:21.978015
# Unit test for function rolling_max
def test_rolling_max():
    assert module_0.rolling_max([]) == []
    assert module_0.rolling_max([3, 1, 4, 2, 4]) == [3, 3, 4, 4, 4]
    assert module_0.rolling_max([-5, -2, -8]) == [-5, -2, -2]
    assert module_0.rolling_max([7]) == [7]

# Generated at 2026-10-25 11:05:24.623377
# Unit test for function rolling_max

# Generated at 2026-10-25 11:05:27.040479
# Unit test for function rolling_max

# Generated at 2026-10-25 11:05:29.452792
# Unit test for function rolling_max