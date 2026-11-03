

# Generated at 2026-11-02 14:24:20.897986
# Unit test for function sort_array
def test_sort_array():
    # Empty array should return an empty list
    assert module_0.sort_array([]) == []

    # Single-element arrays
    assert module_0.sort_array([5]) == [5]
    assert module_0.sort_array([0]) == [0]

    # First + last is odd -> sort ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]   # 2 + 5 = 7 (odd)
    assert module_0.sort_array([1, 3, 2, 4]) == [1, 2, 3, 4]               # 1 + 4 = 5 (odd)
    assert module_0.sort_array([-3, -1, -2]) == [-3, -2, -1]               # -3 + -2 = -5 (odd)

    # First + last is even -> sort descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]  # 2 + 6 = 8 (even)
    assert module_0.sort_array([1, 3, 5, 7]) == [7, 5, 3, 1]                    # 1 + 7 = 8 (even)
    assert module_0.sort_array([-2, -4, -3, 0]) == [0, -2, -3, -4]              # -2 + 0 = -2 (even)

    # Arrays with duplicates
    assert module_0.sort_array([3, 1, 3]) == [3, 3, 1]        # 3 + 3 = 6 (even) -> descending
    assert module_0.sort_array([3, 2, 1, 4]) == [1, 2, 3, 4]  # 3 + 4 = 7 (odd)  -> ascending

    # Original input array must not be modified
    original = [2, 4, 3, 0, 1, 5]
    module_0.sort_array(original)
    assert original == [2, 4, 3, 0, 1, 5]

# Generated at 2026-11-02 14:27:34.094239
# Unit test for function sort_array
def test_sort_array():
    # Empty array returns empty array
    assert module_0.sort_array([]) == []

    # Single element array
    assert module_0.sort_array([5]) == [5]
    assert module_0.sort_array([0]) == [0]

    # First + last is odd -> sort ascending
    # 2 + 5 = 7 (odd)
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    # 3 + 0 = 3 (odd)
    assert module_0.sort_array([3, 6, 4, 5, 3, 7, 2, 9, 0]) == [0, 2, 3, 3, 4, 5, 6, 7, 9]
    # 2 + 1 = 3 (odd)
    assert module_0.sort_array([2, 1]) == [1, 2]
    # 5 + 2 = 7 (odd)
    assert module_0.sort_array([5, 4, 3, 2, 2]) == [2, 2, 3, 4, 5]

    # First + last is even -> sort descending
    # 1 + 3 = 4 (even)
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]
    # 5 + 3 = 8 (even)
    assert module_0.sort_array([5, 2, 3]) == [5, 3, 2]
    # 2 + 6 = 8 (even)
    assert module_0.sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    # 0 + 0 = 0 (even)
    assert module_0.sort_array([0, 4, 6, 8]) == [8, 6, 4, 0]

    # Negative numbers
    # -1 + 3 = 2 (even) -> descending
    assert module_0.sort_array([-1, 2, -3, 3]) == [3, 2, -1, -3]
    # -5 + 2 = -3 (odd) -> ascending
    assert module_0.sort_array([-5, 3, -2, 2]) == [-5, -2, 2, 3]

    # Array with duplicates
    # 1 + 2 = 3 (odd) -> ascending
    assert module_0.sort_array([1, 1, 2, 2]) == [1, 1, 2, 2]
    # 2 + 2 = 4 (even) -> descending
    assert module_0.sort_array([2, 2, 1, 1]) == [2, 2, 1, 1]

    # Already sorted arrays
    # 1 + 9 = 10 (even) -> descending
    assert module_0.sort_array([1, 3, 5, 7, 9]) == [9, 7, 5, 3, 1]
    # 0 + 8 = 8 (even) -> descending
    assert module_0.sort_array([0, 2, 4, 8]) == [8, 4, 2, 0]

    print("All tests passed!")


test_sort_array()

# Generated at 2026-11-02 14:31:59.946391
# Unit test for function sort_array
def test_sort_array():
    # Empty array returns empty list
    assert module_0.sort_array([]) == []

    # Single element array
    assert module_0.sort_array([5]) == [5]

    # First + last is odd -> sort ascending
    assert module_0.sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]  # 2 + 5 = 7 (odd)
    assert module_0.sort_array([1, 2]) == [1, 2]                          # 1 + 2 = 3 (odd)
    assert module_0.sort_array([2, 1]) == [1, 2]                          # 2 + 1 = 3 (odd)

    # First + last is even -> sort descending
    assert module_0.sort_array([2, 4, 3, 0, 1, 4]) == [4, 4, 3, 2, 1, 0]  # 2 + 4 = 6 (even)
    assert module_0.sort_array([3, 5]) == [5, 3]                          # 3 + 5 = 8 (even)
    assert module_0.sort_array([5, 3]) == [5, 3]                          # 5 + 3 = 8 (even)

    # All identical elements
    assert module_0.sort_array([1, 1, 1]) == [1, 1, 1]                    # 1 + 1 = 2 (even)

    # Negative numbers: odd sum -> ascending
    assert module_0.sort_array([-2, -4, 3, 0, 1, -5]) == [-5, -2, 0, 1, 3, 4]  # -2 + -5 = -7 (odd)

    # Negative numbers: even sum -> descending
    assert module_0.sort_array([-2, -4, 3, 0, 1, -4]) == [3, 1, 0, -2, -4, -4]  # -2 + -4 = -6 (even)

    print("All sort_array tests passed!")


if __name__ == "__main__":
    test_sort_array()