

# Generated at 2026-11-02 09:32:57.865939
# Unit test for function by_length
def test_by_length():
    # Typical case: numbers 1-9 unsorted
    assert module_0.by_length([2, 1, 1, 4, 5, 8, 2, 3]) == [
        "Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"
    ]

    # Empty array
    assert module_0.by_length([]) == []

    # Single element
    assert module_0.by_length([1]) == ["One"]

    # Numbers outside 1-9 are ignored
    assert module_0.by_length([10, 0, 11]) == []
    assert module_0.by_length([0, -1, 10, 3]) == ["Three"]

    # Mixed valid and invalid numbers: invalid skipped, valid sorted descending
    assert module_0.by_length([1, -1, 55]) == ["One"]
    assert module_0.by_length([9, 100, 8, 0, 7]) == ["Nine", "Eight", "Seven"]

    # All valid numbers sorted descending
    assert module_0.by_length([9, 4, 6, 1, 8, 2, 5, 3, 7]) == [
        "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"
    ]

    # Duplicates preserved
    assert module_0.by_length([3, 3, 3]) == ["Three", "Three", "Three"]

    # Already sorted input
    assert module_0.by_length([5, 4, 3, 2, 1]) == ["Five", "Four", "Three", "Two", "One"]

    # All invalid values
    assert module_0.by_length([-5, 0, 100, 1000]) == []

    # Floats not in dictionary are ignored
    assert module_0.by_length([1.5, 2]) == ["Two"]

# Generated at 2026-11-02 09:36:46.329248
# Unit test for function by_length
def test_by_length():
    # Normal case: sorted descending and mapped to words
    assert module_0.by_length([2, 1, 3, 5, 4]) == ["Five", "Four", "Three", "Two", "One"]
    assert module_0.by_length([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [
        "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"
    ]
    # Empty array
    assert module_0.by_length([]) == []
    # Numbers outside 1-9 are ignored
    assert module_0.by_length([1, -1, 55]) == ["One"]
    assert module_0.by_length([0, 10, 100]) == []
    assert module_0.by_length([-2, -5, 12]) == []
    # Duplicates are kept
    assert module_0.by_length([3, 3, 2, 2]) == ["Three", "Three", "Two", "Two"]
    # Single element
    assert module_0.by_length([5]) == ["Five"]
    # Mixed valid and invalid values
    assert module_0.by_length([4, 15, 7, -3, 1]) == ["Seven", "Four", "One"]
    # Already sorted input
    assert module_0.by_length([1, 2, 3]) == ["Three", "Two", "One"]
    # All invalid values
    assert module_0.by_length([-1, 0, 10]) == []
    print("All tests passed!")


if __name__ == "__main__":
    test_by_length()

# Generated at 2026-11-02 09:39:30.658025
# Unit test for function by_length
def test_by_length():
    # Basic case: numbers 1-9 in mixed order
    assert module_0.by_length([2, 1, 1, 4, 5, 8, 2, 3]) == [
        "Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"
    ]

    # Empty array returns empty list
    assert module_0.by_length([]) == []

    # Array with numbers out of range 1-9 (ignored)
    assert module_0.by_length([1, -1, 55]) == ["One"]

    # Only out-of-range numbers
    assert module_0.by_length([0, 10, -5, 100]) == []

    # Already sorted descending
    assert module_0.by_length([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [
        "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"
    ]

    # All same numbers
    assert module_0.by_length([3, 3, 3]) == ["Three", "Three", "Three"]

    # Single element
    assert module_0.by_length([5]) == ["Five"]

    # Duplicates of boundary values
    assert module_0.by_length([9, 9, 1, 1]) == ["Nine", "Nine", "One", "One"]

    # Mixed valid and invalid values
    assert module_0.by_length([4, 12, 7, -3, 2, 0]) == ["Seven", "Four", "Two"]

    # Floats are not in dict and should be skipped
    assert module_0.by_length([1.5, 2]) == ["Two"]

    # Booleans: True == 1 and False == 0 in Python
    assert module_0.by_length([True, False]) == ["One"]

    print("All tests passed!")


if __name__ == "__main__":
    test_by_length()