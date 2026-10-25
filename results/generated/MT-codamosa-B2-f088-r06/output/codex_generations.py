

# Generated at 2026-10-25 02:37:34.345187
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([3, 1, 2]) == [1, 2, 3]       # 3 + 2 is odd
    assert module_0.sort_array([3, 2, 1]) == [3, 2, 1]       # 3 + 1 is even
    assert module_0.sort_array([1, 4, 3, 2, 5]) == [1, 2, 3, 4, 5]
    assert module_0.sort_array([2, 1, 3, 4]) == [4, 3, 2, 1]
    assert module_0.sort_array([7]) == [7]
    assert module_0.sort_array([2, 2, 1, 1]) == [1, 1, 2, 2]

# Generated at 2026-10-25 02:37:41.100752
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([5]) == [5]

    # First + last is odd, so sort ascending
    assert module_0.sort_array([3, 1, 2, 4]) == [1, 2, 3, 4]

    # First + last is even, so sort descending
    assert module_0.sort_array([3, 1, 2, 5]) == [5, 3, 2, 1]

    # Duplicates and negative numbers
    assert module_0.sort_array([-3, 2, 2, 1]) == [-3, 1, 2, 2]
    assert module_0.sort_array([-3, 2, 2, -1]) == [2, 2, -1, -3]

    # The original list should not be modified
    values = [4, 1, 3, 2]
    module_0.sort_array(values)
    assert values == [4, 1, 3, 2]

# Generated at 2026-10-25 02:37:56.772935
# Unit test for function sort_array
def test_sort_array():assert module_0.sort_array([]) == []

# Generated at 2026-10-25 02:38:04.755530
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([5]) == [5]
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]  # 1 + 3 is even
    assert module_0.sort_array([1, 3, 4]) == [1, 3, 4]  # 1 + 4 is odd
    assert module_0.sort_array([4, 1, 2]) == [4, 2, 1]  # 4 + 2 is even
    assert module_0.sort_array([-3, 2, 4]) == [-3, 2, 4]  # -3 + 4 is odd
    assert module_0.sort_array([2, 1, 2, 3, 2]) == [3, 2, 2, 2, 1]

# Generated at 2026-10-25 02:38:11.619288
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([5]) == [5]

    # First + last is odd: ascending order
    assert module_0.sort_array([4, 1, 3, 5]) == [1, 3, 4, 5]

    # First + last is even: descending order
    assert module_0.sort_array([3, 1, 4, 5]) == [5, 4, 3, 1]

    # Duplicates and negative values
    assert module_0.sort_array([-3, 2, -1, 5]) == [5, 2, -1, -3]
    assert module_0.sort_array([2, 1, 2, 4]) == [4, 2, 2, 1]