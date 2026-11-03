

# Generated at 2026-11-02 16:24:35.776267
# Unit test for function sort_even
def test_sort_even():
    # Basic case: evens already sorted
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]

    # Evens need sorting
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

    # Longer list with unsorted even indices
    assert module_0.sort_even([10, 1, 2, 3, 0, 4]) == [0, 1, 2, 3, 10, 4]

    # Empty list
    assert module_0.sort_even([]) == []

    # Single element (only even index)
    assert module_0.sort_even([42]) == [42]

    # Two elements
    assert module_0.sort_even([7, 8]) == [7, 8]

    # Even indices longer than odd indices (last even element appended)
    assert module_0.sort_even([3, 1, 2]) == [2, 1, 3]

    # Duplicates in even positions
    assert module_0.sort_even([2, 100, 2, 5]) == [2, 100, 2, 5]

    # Negative numbers
    assert module_0.sort_even([-1, 5, -3, 6]) == [-3, 5, -1, 6]

    # All even positions descending
    assert module_0.sort_even([9, 0, 7, 0, 5, 0]) == [5, 0, 7, 0, 9, 0]

    # Odd positions untouched even if unsorted
    assert module_0.sort_even([1, 9, 2, 8, 3, 7]) == [1, 9, 2, 8, 3, 7]

    # Result length matches input length
    for input_list in [[], [1], [1, 2], [4, 3, 2, 1], [5, 4, 3, 2, 1]]:
        assert len(module_0.sort_even(input_list)) == len(input_list)

    print("All test_sort_even tests passed!")


if __name__ == "__main__":
    test_sort_even()

# Generated at 2026-11-02 16:25:38.447644
# Unit test for function sort_even
def test_sort_even():
    # Empty list
    assert module_0.sort_even([]) == []

    # Single element (odd length, even index only)
    assert module_0.sort_even([1]) == [1]

    # Two elements
    assert module_0.sort_even([2, 1]) == [2, 1]

    # Odd length list: evens sorted, last even appended
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_even([5, 1, 3, 2, 2]) == [2, 1, 3, 2, 5]

    # Even length list: evens at indices 0,2 sorted and interleaved
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

    # Evens already sorted
    assert module_0.sort_even([1, 9, 2, 8, 3, 7]) == [1, 9, 2, 8, 3, 7]

    # Evens in reverse order
    assert module_0.sort_even([9, 1, 8, 2, 7, 3]) == [7, 1, 8, 2, 9, 3]

    # Duplicates among even-index values
    assert module_0.sort_even([3, 1, 3, 2, 1, 5]) == [1, 1, 3, 2, 3, 5]

    # Works with strings
    assert module_0.sort_even(["b", "a", "a", "b"]) == ["a", "a", "b", "b"]

    # Original input list must not be modified
    original = [5, 6, 3, 4]
    module_0.sort_even(original)
    assert original == [5, 6, 3, 4]

# Generated at 2026-11-02 16:27:14.666982
# Unit test for function sort_even
def test_sort_even():
    # nonce:93ef9ec2
    # Empty list
    assert module_0.sort_even([]) == []
    # Single element
    assert module_0.sort_even([1]) == [1]
    # Two elements
    assert module_0.sort_even([3, 1]) == [3, 1]
    # Odd-length list (extra even element appended at end)
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_even([4, 1, 2]) == [2, 1, 4]
    # Even-length list
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    # Longer list with unsorted even indices
    assert module_0.sort_even([10, 1, 2, 3, 0, 5]) == [0, 1, 2, 3, 10, 5]
    # Negative numbers
    assert module_0.sort_even([-1, 5, -3, 2]) == [-3, 5, -1, 2]
    # Duplicates
    assert module_0.sort_even([3, 1, 3, 2, 1, 5]) == [1, 1, 3, 2, 3, 5]
    # All equal elements
    assert module_0.sort_even([2, 2, 2, 2]) == [2, 2, 2, 2]
    # Descending input
    assert module_0.sort_even([5, 4, 3, 2, 1, 0]) == [1, 4, 3, 2, 5, 0]
    # Original list must not be modified
    original = [9, 1, 7, 2, 3, 8]
    snapshot = list(original)
    module_0.sort_even(original)
    assert original == snapshot

# Generated at 2026-11-02 16:28:30.726221
# Unit test for function sort_even
def test_sort_even():
    # Canonical examples
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

    # Edge cases
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([1]) == [1]
    assert module_0.sort_even([2, 1]) == [2, 1]

    # Odd-length list: leftover even-index element appended at end
    assert module_0.sort_even([3, 1, 2, 4, 5]) == [2, 1, 3, 4, 5]
    assert module_0.sort_even([9, 8, 7, 6, 5, 4, 3]) == [3, 8, 5, 6, 7, 4, 9]
    assert module_0.sort_even([1, 5, 2, 4, 3]) == [1, 5, 2, 4, 3]

    # Even-length list
    assert module_0.sort_even([5, 1, 3, 2, 4, 6]) == [3, 1, 4, 2, 5, 6]

    # Duplicates among even-index values
    assert module_0.sort_even([4, 1, 2, 3, 2]) == [2, 1, 2, 3, 4]

    # Negative numbers
    assert module_0.sort_even([5, -1, -3, 2, 0]) == [-3, -1, 0, 2, 5]

    # Original input list must not be mutated
    original = [5, 6, 3, 4]
    module_0.sort_even(original)
    assert original == [5, 6, 3, 4]

# Generated at 2026-11-02 16:29:48.787390
# Unit test for function sort_even
def test_sort_even():
    # Basic case: odd length list
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]

    # Even length list with unsorted evens
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]

    # Empty list
    assert module_0.sort_even([]) == []

    # Single element
    assert module_0.sort_even([1]) == [1]

    # Longer list with mixed values
    assert module_0.sort_even([3, 1, 2, 4, 5]) == [2, 1, 3, 4, 5]

    # Two elements, evens already sorted
    assert module_0.sort_even([2, 1]) == [2, 1]

    # All evens need reordering, odd indices preserved
    assert module_0.sort_even([4, 3, 2, 1, 1, 0]) == [1, 3, 2, 1, 4, 0]

    # Negative numbers
    assert module_0.sort_even([-1, 10, -5, 20, 0]) == [-5, 10, -1, 20, 0]

    # Duplicates in even positions
    assert module_0.sort_even([7, 1, 7, 2, 3, 3]) == [3, 1, 7, 2, 7, 3]

    # Strings
    assert module_0.sort_even(["b", "x", "a", "y"]) == ["a", "x", "b", "y"]

    # Original list should not be mutated
    original = [5, 6, 3, 4]
    module_0.sort_even(original)
    assert original == [5, 6, 3, 4]

    print("All test_sort_even tests passed!")


if __name__ == "__main__":
    test_sort_even()