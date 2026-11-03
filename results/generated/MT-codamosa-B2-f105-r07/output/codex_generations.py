

# Generated at 2026-11-02 15:16:26.510210
# Unit test for function by_length
def test_by_length():
    # Basic case: sort descending and map to words
    assert module_0.by_length([2, 1, 1, 4, 5, 8, 2, 3]) == [
        "Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"
    ]

    # Empty array returns empty list
    assert module_0.by_length([]) == []

    # Numbers out of range (1-9) are ignored
    assert module_0.by_length([1, -1, 55]) == ["One"]

    # All numbers out of range
    assert module_0.by_length([-1, 0, 10, 55]) == []

    # Already sorted descending input
    assert module_0.by_length([9, 8, 7]) == ["Nine", "Eight", "Seven"]

    # Already sorted ascending input
    assert module_0.by_length([1, 2, 3]) == ["Three", "Two", "One"]

    # Single element
    assert module_0.by_length([5]) == ["Five"]

    # Duplicates preserved
    assert module_0.by_length([3, 3, 3]) == ["Three", "Three", "Three"]

    # Mixed valid, invalid, and duplicates
    assert module_0.by_length([4, 4, 100, 2, 0, 9]) == ["Nine", "Four", "Four", "Two"]

    # Negative numbers ignored
    assert module_0.by_length([-5, -3, 7]) == ["Seven"]

# Generated at 2026-11-02 15:18:44.036605
# Unit test for function by_length
def test_by_length():
    # Basic case: unsorted array of valid numbers
    assert module_0.by_length([2, 1, 1, 4, 5, 8, 2, 3]) == [
        "Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"
    ]

    # Empty array returns empty list
    assert module_0.by_length([]) == []

    # Numbers out of range (including 0, negatives, and >9) are ignored
    assert module_0.by_length([10, 0, -1, 100]) == []

    # Mixed: out-of-range values filtered, valid ones sorted descending
    assert module_0.by_length([1, -1, 55]) == ["One"]

    # Single element
    assert module_0.by_length([9]) == ["Nine"]

    # All numbers 1 through 9, sorted descending
    assert module_0.by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [
        "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"
    ]

    # Duplicates preserved
    assert module_0.by_length([3, 3, 3]) == ["Three", "Three", "Three"]

    # Already sorted descending input
    assert module_0.by_length([9, 8, 7]) == ["Nine", "Eight", "Seven"]

    # Already sorted ascending input gets reversed
    assert module_0.by_length([1, 2, 3]) == ["Three", "Two", "One"]

    # Floats not in dict are ignored
    assert module_0.by_length([1.5, 2]) == ["Two"]

    # Result of filtering everything out is an empty list
    assert module_0.by_length([0, 10, 20]) == []

    print("All tests passed!")


# Run tests
if __name__ == "__main__":
    test_by_length()

# Generated at 2026-11-02 15:21:35.361789
# Unit test for function by_length
def test_by_length():
    # Test basic sorting and mapping
    assert module_0.by_length([2, 1, 1, 4, 5, 8, 2, 3]) == [
        "Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"
    ]

    # Test empty array
    assert module_0.by_length([]) == []

    # Test array with invalid numbers (outside 1-9)
    assert module_0.by_length([1, -1, 55]) == ["One"]
    assert module_0.by_length([-1, -2]) == []
    assert module_0.by_length([0, 10]) == []

    # Test full range of valid numbers
    assert module_0.by_length([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [
        "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"
    ]

    # Test already sorted descending input
    assert module_0.by_length([5, 3, 1]) == ["Five", "Three", "One"]

    # Test unsorted input requiring descending sort
    assert module_0.by_length([1, 5, 3]) == ["Five", "Three", "One"]

    # Test duplicates
    assert module_0.by_length([3, 3, 3]) == ["Three", "Three", "Three"]

    # Test single element
    assert module_0.by_length([7]) == ["Seven"]

    # Test mix of valid and invalid numbers
    assert module_0.by_length([4, 12, 2, -3, 8]) == ["Eight", "Four", "Two"]

    print("All tests passed!")


if __name__ == "__main__":
    test_by_length()

# Generated at 2026-11-02 15:24:12.456241
# Unit test for function by_length
def test_by_length():
    # Basic case: numbers 1-9 sorted descending
    assert module_0.by_length([2, 1, 5, 3, 4, 7, 6, 9, 8]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]

    # Empty array
    assert module_0.by_length([]) == []

    # Numbers out of range (0, 10, negatives) are skipped
    assert module_0.by_length([0, 10, -1, 2, 3]) == ["Three", "Two"]

    # Duplicates preserved
    assert module_0.by_length([3, 3, 1]) == ["Three", "Three", "One"]

    # Single element
    assert module_0.by_length([5]) == ["Five"]

    # All invalid values yield empty list
    assert module_0.by_length([0, 10, -5, 100]) == []

    # Already sorted descending
    assert module_0.by_length([9, 8, 7]) == ["Nine", "Eight", "Seven"]

    # Mixed valid and invalid values
    assert module_0.by_length([1, -1, 55, 9]) == ["Nine", "One"]

    # Floats are not in dict, should be skipped
    assert module_0.by_length([1.5, 2]) == ["Two"]

    # Strings are not in dict, should be skipped
    assert module_0.by_length(["a", 4]) == ["Four"]

    print("All tests passed!")


if __name__ == "__main__":
    test_by_length()