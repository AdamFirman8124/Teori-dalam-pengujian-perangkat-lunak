

# Generated at 2026-11-01 22:32:32.042098
# Unit test for function sort_even
def test_sort_even():
    # Basic cases: even-indexed values sorted, odd-indexed values kept in place
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

    # Edge cases: empty and single-element lists
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([1]) == [1]

    # Two-element list
    assert module_0.sort_even([2, 1]) == [2, 1]

    # Odd-length list: leftover even-indexed element (max of evens) appended at end
    assert module_0.sort_even([5, 6, 3, 4, 1]) == [1, 6, 3, 4, 5]
    assert module_0.sort_even([3, 4, 5, 6, 7]) == [3, 4, 5, 6, 7]
    assert module_0.sort_even([9, 7, 8]) == [8, 7, 9]

    # Longer list
    assert module_0.sort_even([10, 1, 2, 3, 4, 5, 6]) == [2, 1, 4, 3, 6, 5, 10]

    # Negative numbers
    assert module_0.sort_even([-2, 1, -3, 2]) == [-3, 1, -2, 2]

    # Duplicates
    assert module_0.sort_even([2, 1, 2, 3]) == [2, 1, 2, 3]

    # Works with strings (any comparable type)
    assert module_0.sort_even(["d", "a", "b", "c"]) == ["b", "a", "d", "c"]

    # Original input list must not be mutated
    original = [3, 2, 1]
    module_0.sort_even(original)
    assert original == [3, 2, 1]

    # Property check: odd-indexed positions are unchanged
    data = [7, 1, 5, 9, 3, 4]
    result = module_0.sort_even(data)
    assert result[1::2] == data[1::2]
    assert result[::2] == sorted(data[::2])

    print("All tests passed!")


if __name__ == "__main__":
    test_sort_even()

# Generated at 2026-11-01 22:32:51.701955
# Unit test for function sort_even
def test_sort_even():
    # Even-indexed values already sorted
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_even([3, 1]) == [3, 1]

    # Even-indexed values need sorting
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert module_0.sort_even([3, 1, 2, 4, 5, 6]) == [2, 1, 3, 4, 5, 6]

    # Longer mixed example with negatives and duplicates
    assert module_0.sort_even([5, 3, -5, 2, 3, 3, 9, 0, 123, 1, -10]) == [
        -10, 3, -5, 2, 3, 3, 5, 0, 9, 1, 123
    ]

    # Edge cases
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([1]) == [1]
    assert module_0.sort_even([2, 2, 2]) == [2, 2, 2]

    # Duplicates and negatives at even indices
    assert module_0.sort_even([-1, 0, -3, 0, -2, 0]) == [-3, 0, -2, 0, -1, 0]

    # Odd-indexed values must remain untouched in their positions
    assert module_0.sort_even([10, 99, 5, 88, 1, 77]) == [1, 99, 5, 88, 10, 77]

    # Original input list should not be mutated
    original = [9, 1, 8, 2]
    module_0.sort_even(original)
    assert original == [9, 1, 8, 2]

    print("All tests passed!")


if __name__ == "__main__":
    test_sort_even()

# Generated at 2026-11-01 22:33:38.191336
# Unit test for function sort_even
def test_sort_even():
    # Basic documented behavior
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

    # Edge cases
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([7]) == [7]
    assert module_0.sort_even([1, 2]) == [1, 2]
    assert module_0.sort_even([2, 1]) == [2, 1]  # single even-index element: order unchanged

    # Odd-length list: leftover even-index element goes last
    assert module_0.sort_even([3, 1, 2, 4, 5]) == [2, 1, 3, 4, 5]

    # Longer list with negatives and duplicate even-index values
    assert module_0.sort_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == \
        [-10, 3, -5, 2, -3, 3, 5, 0, 9, 1, 123]

    # Duplicates among even-index positions
    assert module_0.sort_even([3, 1, 3, 2]) == [3, 1, 3, 2]

    # Works with other sortable types
    assert module_0.sort_even(['b', 'x', 'a', 'y']) == ['a', 'x', 'b', 'y']

    # Input list must not be mutated
    src = [9, 1, 7, 2]
    module_0.sort_even(src)
    assert src == [9, 1, 7, 2]

    print("test_sort_even passed")


if __name__ == "__main__":
    test_sort_even()

# Generated at 2026-11-01 22:34:07.581062
# Unit test for function sort_even
def test_sort_even():
    # Basic cases: elements at even indices get sorted
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert module_0.sort_even([4, 3, 2, 1, 5]) == [2, 3, 4, 1, 5]

    # Edge cases
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([1]) == [1]
    assert module_0.sort_even([2, 1]) == [2, 1]

    # Duplicates and negatives
    assert module_0.sort_even([3, 1, 3, 2, 1]) == [1, 1, 3, 2, 3]
    assert module_0.sort_even([-2, 5, -1, 4, -3]) == [-3, 5, -2, 4, -1]

    # Longer list
    assert module_0.sort_even([10, 1, 9, 2, 8, 3, 7]) == [7, 1, 8, 2, 9, 3, 10]

# Generated at 2026-11-01 22:34:41.971065
# Unit test for function sort_even
def test_sort_even():
    # Empty list
    assert module_0.sort_even([]) == []

    # Single element (only an even index)
    assert module_0.sort_even([1]) == [1]

    # Two elements: single even-index value, nothing to sort
    assert module_0.sort_even([2, 1]) == [2, 1]

    # Three elements: even-index values sorted, odd-index untouched
    assert module_0.sort_even([3, 2, 1]) == [1, 2, 3]

    # Four elements: even indices sorted, odd indices unchanged
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

    # Six elements with duplicates
    assert module_0.sort_even([5, 1, 3, 2, 4, 9]) == [3, 1, 4, 2, 5, 9]

    # Longer odd-length list with negatives and duplicates
    assert module_0.sort_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [
        -10, 3, -5, 2, -3, 3, 5, 0, 9, 1, 123
    ]

    # Even-index values already sorted (trailing even element preserved)
    assert module_0.sort_even([1, 9, 2, 8, 3]) == [1, 9, 2, 8, 3]

    # Works with strings
    assert module_0.sort_even(["b", "z", "a", "y"]) == ["a", "z", "b", "y"]

    # Input list is not mutated
    data = [3, 1, 2]
    module_0.sort_even(data)
    assert data == [3, 1, 2]


if __name__ == "__main__":
    test_sort_even()
    print("All tests passed!")