

# Generated at 2026-11-01 22:22:22.244626
# Unit test for function sort_even
def test_sort_even():
    # Empty list
    assert module_0.sort_even([]) == []
    # Single element (odd length, last even appended)
    assert module_0.sort_even([1]) == [1]
    # Already sorted even-index elements
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]
    # Even-length list with unsorted even indices
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    # Odd-length list, even indices sorted, last element appended
    assert module_0.sort_even([4, 1, 3, 2, 5]) == [3, 1, 4, 2, 5]
    # Reverse-sorted even indices
    assert module_0.sort_even([9, 1, 7, 2, 5, 3]) == [5, 1, 7, 2, 9, 3]
    # Negative numbers
    assert module_0.sort_even([-3, 1, -1, 2]) == [-3, 1, -1, 2]
    # Duplicates among even indices
    assert module_0.sort_even([2, 1, 2, 3]) == [2, 1, 2, 3]
    # Odd-index elements remain untouched
    assert module_0.sort_even([10, 100, 1, 200, 5, 300]) == [1, 100, 5, 200, 10, 300]
    # Floats mixed with ints
    assert module_0.sort_even([3.5, 1, 1.5, 2]) == [1.5, 1, 3.5, 2]
    # Original input list must not be mutated
    original = [5, 6, 3, 4]
    module_0.sort_even(original)
    assert original == [5, 6, 3, 4]
    print("All sort_even tests passed.")


if __name__ == "__main__":
    test_sort_even()

# Generated at 2026-11-01 22:23:35.871063
# Unit test for function sort_even
def test_sort_even():
    # Basic cases
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

    # Empty list
    assert module_0.sort_even([]) == []

    # Single element (only even index)
    assert module_0.sort_even([42]) == [42]

    # Two elements
    assert module_0.sort_even([10, 1]) == [10, 1]
    assert module_0.sort_even([3, 1]) == [3, 1]

    # Longer list where evens need sorting
    assert module_0.sort_even([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 8, 5, 6, 7, 4, 9, 2, 1]

    # Odd-length list: last even-index element has no odd partner
    assert module_0.sort_even([5, 1, 3, 2, 4]) == [3, 1, 4, 2, 5]

    # Duplicates among even-index values
    assert module_0.sort_even([2, 100, 2, 200, 1]) == [1, 100, 2, 200, 2]

    # Negative numbers
    assert module_0.sort_even([-1, 5, -3, 6, -2]) == [-3, 5, -1, 6, -2]

    # Already sorted evens remain unchanged
    assert module_0.sort_even([1, 99, 2, 98, 3]) == [1, 99, 2, 98, 3]

    # All even indices, no odd partners beyond interleaving
    assert module_0.sort_even([3, 0, 1, 0, 2]) == [1, 0, 2, 0, 3]

    print("All test_sort_even tests passed!")


if __name__ == "__main__":
    test_sort_even()

# Generated at 2026-11-01 22:25:00.720740
# Unit test for function sort_even
def test_sort_even():
    # Already sorted even indices
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]

    # Unsorted even indices, even-length list
    assert module_0.sort_even([5, 3, 1, 4]) == [1, 3, 5, 4]

    # Odd-length list with negatives (evens sorted, odds untouched)
    assert module_0.sort_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == \
        [-5, 3, -3, 2, -10, 3, 5, 0, 9, 1, 123]

    # Empty list
    assert module_0.sort_even([]) == []

    # Single element
    assert module_0.sort_even([42]) == [42]

    # Two elements
    assert module_0.sort_even([2, 1]) == [2, 1]

    # Duplicates in even positions
    assert module_0.sort_even([3, 1, 3, 2, 1, 5]) == [1, 1, 3, 2, 3, 5]

    # All identical elements
    assert module_0.sort_even([7, 7, 7, 7]) == [7, 7, 7, 7]

    # Negative numbers only at even indices
    assert module_0.sort_even([-1, 10, -5, 20, -3, 30]) == [-5, 10, -3, 20, -1, 30]

    # Original list must not be mutated
    original = [4, 2, 3, 1]
    _ = module_0.sort_even(original)
    assert original == [4, 2, 3, 1]

    # Result length matches input length
    assert len(module_0.sort_even([9, 8, 7, 6, 5])) == 5

# Generated at 2026-11-01 22:26:29.030526
# Unit test for function sort_even
def test_sort_even():
# nonce:c2696e0c
    # Odd-length list: evens sorted, odds stay in place, last even appended
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_even([5, 3, -5, 2, 3, 3, 9, 0, 123, 1, -10]) == [-10, 3, -5, 2, 3, 3, 5, 0, 9, 1, 123]

    # Even-length list: no leftover element appended
    assert module_0.sort_even([5, 8, -5, 4, 1, -1]) == [-5, 8, 1, 4, 5, -1]
    assert module_0.sort_even([4, 1, 3, 2, 2, 5]) == [2, 1, 3, 2, 4, 5]

    # Empty list
    assert module_0.sort_even([]) == []

    # Single element
    assert module_0.sort_even([5]) == [5]

    # Even indices need reordering
    assert module_0.sort_even([3, 1, 2]) == [2, 1, 3]

    # Duplicates handled correctly
    assert module_0.sort_even([2, 1, 2, 1]) == [2, 1, 2, 1]

    # Odd-index values are untouched
    assert module_0.sort_even([3, 100, 1, 200, 2, 300]) == [1, 100, 2, 200, 3, 300]

# Generated at 2026-11-01 22:27:28.087799
# Unit test for function sort_even
def test_sort_even():
    # Basic case: already sorted evens
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]

    # Evens out of order get sorted, odds stay in place
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

    # Empty list
    assert module_0.sort_even([]) == []

    # Single element (only even index)
    assert module_0.sort_even([42]) == [42]

    # Two elements
    assert module_0.sort_even([10, 1]) == [10, 1]
    assert module_0.sort_even([2, 99]) == [2, 99]

    # Longer list with duplicates and negatives
    assert module_0.sort_even([4, 1, 2, 2, -1, 3]) == [-1, 1, 2, 2, 4, 3]

    # Odd-length list: last even-index element has no odd partner
    assert module_0.sort_even([9, 8, 7, 6, 5]) == [5, 8, 7, 6, 9]

    # All equal values
    assert module_0.sort_even([3, 3, 3, 3]) == [3, 3, 3, 3]

    # Original list must not be mutated beyond returned result check
    data = [5, 1, 3, 2]
    result = module_0.sort_even(data)
    assert result == [3, 1, 5, 2]
    assert isinstance(result, list)

    print("All tests passed!")


if __name__ == "__main__":
    test_sort_even()