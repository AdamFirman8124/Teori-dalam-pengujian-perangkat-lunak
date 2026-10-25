

# Generated at 2026-10-25 00:18:33.461404
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([5]) == [5]

    # First + last is even: descending order
    assert module_0.sort_array([3, 1, 2, 5]) == [5, 3, 2, 1]
    assert module_0.sort_array([4, 1, 2, 6]) == [6, 4, 2, 1]

    # First + last is odd: ascending order
    assert module_0.sort_array([3, 5, 2, 4]) == [2, 3, 4, 5]
    assert module_0.sort_array([6, 3, 1, 5]) == [1, 3, 5, 6]

    # Handles duplicates and negative numbers
    assert module_0.sort_array([-2, 3, -2, 4]) == [4, 3, -2, -2]

# Generated at 2026-10-25 00:18:39.558254
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([]) == []

    # First + last is odd: ascending order
    assert module_0.sort_array([3, 1, 4, 2]) == [1, 2, 3, 4]

    # First + last is even: descending order
    assert module_0.sort_array([3, 1, 4, 5]) == [5, 4, 3, 1]

    assert module_0.sort_array([7]) == [7]
    assert module_0.sort_array([2, 2, 2]) == [2, 2, 2]

    # Verify the original list is not modified
    values = [4, 1, 3, 2]
    module_0.sort_array(values)
    assert values == [4, 1, 3, 2]

# Generated at 2026-10-25 00:18:45.599446
# Unit test for function sort_array
def test_sort_array():
    # Empty array
    assert module_0.sort_array([]) == []

    # First + last is odd: ascending order
    assert module_0.sort_array([5, 2, 9, 4]) == [2, 4, 5, 9]

    # First + last is even: descending order
    assert module_0.sort_array([5, 2, 9, 3]) == [9, 5, 3, 2]

    # Duplicates and negative values
    assert module_0.sort_array([-1, 3, -1, 1]) == [3, 1, -1, -1]

    # Single-element array
    assert module_0.sort_array([7]) == [7]

# Generated at 2026-10-25 00:18:51.129066
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([]) == []

    # First + last is even, so sort descending.
    assert module_0.sort_array([5, 2, 9, 1]) == [9, 5, 2, 1]

    # First + last is odd, so sort ascending.
    assert module_0.sort_array([5, 2, 9, 2]) == [2, 2, 5, 9]

    assert module_0.sort_array([3]) == [3]
    assert module_0.sort_array([-2, 4, -6]) == [4, -2, -6]

# Generated at 2026-10-25 00:18:56.740814
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([3, 1, 5, 2, 1]) == [5, 3, 2, 1, 1]  # 3 + 1 is even
    assert module_0.sort_array([3, 5, 1, 2]) == [1, 2, 3, 5]         # 3 + 2 is odd
    assert module_0.sort_array([4]) == [4]
    assert module_0.sort_array([-2, 3, 0, 4]) == [4, 3, 0, -2]      # -2 + 4 is even