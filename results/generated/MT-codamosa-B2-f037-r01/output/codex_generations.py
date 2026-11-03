

# Generated at 2026-11-02 21:15:41.682482
# Unit test for function sort_even
def test_sort_even():
    # Basic case: even indices already sorted
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]

    # Even indices out of order
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

    # Empty list
    assert module_0.sort_even([]) == []

    # Single element (only even index)
    assert module_0.sort_even([2]) == [2]

    # Two elements: even index stays, odd index untouched
    assert module_0.sort_even([2, 1]) == [2, 1]

    # Odd-index elements kept in place, even-index sorted
    assert module_0.sort_even([4, 1, 3, 2, 5]) == [3, 1, 4, 2, 5]

    # Duplicates among even-index values
    assert module_0.sort_even([3, 1, 3, 2, 1]) == [1, 1, 3, 2, 3]

    # Negative numbers
    assert module_0.sort_even([-1, 5, -3, 2]) == [-3, 5, -1, 2]

    # Original list should not be modified
    original = [5, 6, 3, 4]
    module_0.sort_even(original)
    assert original == [5, 6, 3, 4]

    # Longer list
    assert module_0.sort_even([9, 0, 7, 1, 8, 2]) == [7, 0, 8, 1, 9, 2]

    print("All tests passed!")


test_sort_even()

# Generated at 2026-11-02 21:16:52.950960
# Unit test for function sort_even
def test_sort_even():
    # Basic case: even-indexed values already sorted
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]

    # Even-indexed values out of order
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

    # Longer list with negatives, from the classic example
    assert module_0.sort_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == \
        [-10, 3, -5, 2, -3, 3, 5, 0, 9, 1, 123]

    # Odd-length list: last even-indexed element goes to the end
    assert module_0.sort_even([5, 3, 2, 8, 4, 6, 1, 7, 9]) == [1, 3, 2, 8, 4, 6, 5, 7, 9]
    assert module_0.sort_even([3, 1, 2]) == [2, 1, 3]

    # Even-length list
    assert module_0.sort_even([4, 1, 3, 2]) == [3, 1, 4, 2]
    assert module_0.sort_even([2, 1]) == [2, 1]

    # Edge cases
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([1]) == [1]

    # Duplicates among even-indexed values
    assert module_0.sort_even([2, 0, 2, 0, 1, 0]) == [1, 0, 2, 0, 2, 0]

    # Negative numbers only
    assert module_0.sort_even([-1, 100, -5, 100, -3]) == [-5, 100, -3, 100, -1]

    # Input list must not be mutated
    original = [3, 2, 1, 0]
    module_0.sort_even(original)
    assert original == [3, 2, 1, 0]

    # Works with strings at even indices
    assert module_0.sort_even(["b", 1, "a", 2]) == ["a", 1, "b", 2]

# Generated at 2026-11-02 21:17:45.577153
# Unit test for function sort_even
def test_sort_even():
    # Empty list
    assert module_0.sort_even([]) == []

    # Single element (even index only)
    assert module_0.sort_even([1]) == [1]

    # Two elements (one even, one odd index)
    assert module_0.sort_even([2, 1]) == [2, 1]

    # Odd length list: evens sorted, odds untouched
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

    # Already sorted evens
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]

    # Reverse sorted evens
    assert module_0.sort_even([5, 1, 3, 2, 1]) == [1, 1, 3, 2, 5]

    # Evens need sorting, odds stay in place
    assert module_0.sort_even([9, 8, 7, 6, 5, 4]) == [5, 8, 7, 6, 9, 4]

    # Odd-length list where last even element must be appended
    assert module_0.sort_even([3, 1, 2]) == [2, 1, 3]

    # Duplicates among even-indexed elements
    assert module_0.sort_even([4, 0, 2, 0, 6, 9]) == [2, 0, 4, 0, 6, 9]

    # Negative numbers
    assert module_0.sort_even([-3, 10, -1, 20, -5]) == [-5, 10, -3, 20, -1]

    # Input list must not be mutated
    original = [5, 6, 3, 4]
    module_0.sort_even(original)
    assert original == [5, 6, 3, 4]

    print("All tests passed!")


test_sort_even()

# Generated at 2026-11-02 21:19:29.318227
# Unit test for function sort_even
def test_sort_even():
    # Empty list
    assert module_0.sort_even([]) == []

    # Single element (odd length: extra even-index element appended last)
    assert module_0.sort_even([3]) == [3]

    # Two elements (even length: odd positions untouched)
    assert module_0.sort_even([5, 1]) == [5, 1]
    assert module_0.sort_even([1, 5]) == [1, 5]

    # Even length list
    assert module_0.sort_even([4, 1, 3, 2]) == [3, 1, 4, 2]

    # Odd length list: largest sorted even-index value goes to the end
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert module_0.sort_even([-1, 0, -3, 0, -2]) == [-3, 0, -2, 0, -1]

    # Canonical example with negatives and duplicates
    assert module_0.sort_even([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == \
        [-10, 3, -5, 2, -3, 3, 5, 0, 9, 1, 123]

    # Duplicates at even indices
    assert module_0.sort_even([2, 1, 2, 1]) == [2, 1, 2, 1]

    # Even-index values sorted, odd-index values preserved in place
    result = module_0.sort_even([10, 7, 1, 8, 5, 9])
    assert result == [1, 7, 5, 8, 10, 9]
    assert result[1::2] == [7, 8, 9]
    assert result[::2] == [1, 5, 10]

    # Input list is not mutated
    original = [3, 1, 2]
    module_0.sort_even(original)
    assert original == [3, 1, 2]

# Generated at 2026-11-02 21:20:54.830228
# Unit test for function sort_even
def test_sort_even():
    # Empty list
    assert module_0.sort_even([]) == []

    # Single element (only even index)
    assert module_0.sort_even([5]) == [5]

    # Two elements (no sorting change)
    assert module_0.sort_even([3, 1]) == [3, 1]

    # Odd-length list: evens sorted, odds stay in place
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

    # Odd-length list where evens longer than odds
    assert module_0.sort_even([5, 3, 4, 2, 1]) == [1, 3, 4, 2, 5]

    # Even-length list
    assert module_0.sort_even([4, 1, 2, 3]) == [2, 1, 4, 3]

    # Already sorted even indices
    assert module_0.sort_even([1, 9, 2, 8, 3, 7]) == [1, 9, 2, 8, 3, 7]

    # Duplicates
    assert module_0.sort_even([2, 1, 2, 1, 1]) == [1, 1, 2, 1, 2]

    # Negative numbers
    assert module_0.sort_even([-3, 0, -1, 5, -2]) == [-3, 0, -2, 5, -1]

    # Even indices descending, odds untouched
    assert module_0.sort_even([10, 1, 9, 2, 8, 3]) == [8, 1, 9, 2, 10, 3]

    print("All tests passed!")


test_sort_even()