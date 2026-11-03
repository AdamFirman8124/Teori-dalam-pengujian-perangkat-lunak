

# Generated at 2026-11-02 13:44:59.336398
# Unit test for function by_length
def test_by_length():
    # nonce:9a2739dd
    # Basic case: sorted descending and mapped to names
    assert module_0.by_length([2, 1, 3]) == ["Three", "Two", "One"]

    # Empty array returns empty list
    assert module_0.by_length([]) == []

    # Numbers outside 1-9 are ignored
    assert module_0.by_length([2, 1, 10, 0, 5]) == ["Five", "Two", "One"]

    # Single element
    assert module_0.by_length([4]) == ["Four"]

    # Duplicates are preserved
    assert module_0.by_length([1, 1, 2]) == ["Two", "One", "One"]

    # Full range 1-9
    assert module_0.by_length([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [
        "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"
    ]

    # Already sorted descending input
    assert module_0.by_length([5, 3]) == ["Five", "Three"]

    # Only invalid numbers yields empty list
    assert module_0.by_length([10, 20, 100]) == []

    # Negative numbers are ignored
    assert module_0.by_length([-2, 3, -5]) == ["Three"]

    # Mixed valid and invalid, with unsorted input
    assert module_0.by_length([-1, 4, 15, 8, 2]) == ["Eight", "Four", "Two"]

    print("All tests passed!")


if __name__ == "__main__":
    test_by_length()

# Generated at 2026-11-02 13:45:39.409426
# Unit test for function by_length
def test_by_length():
    # Basic case: numbers get sorted descending and mapped to names
    assert module_0.by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]

    # Empty array returns empty list
    assert module_0.by_length([]) == []

    # Numbers outside 1-9 are silently ignored
    assert module_0.by_length([1, -1, 55]) == ["One"]

    # All values out of range yields empty list
    assert module_0.by_length([0, 10, -5, 100]) == []

    # Already sorted input still reversed correctly
    assert module_0.by_length([1, 2, 3]) == ["Three", "Two", "One"]

    # Single element
    assert module_0.by_length([9]) == ["Nine"]

    # Mixed valid and invalid values
    assert module_0.by_length([4, 7, 12, 3, 0]) == ["Seven", "Four", "Three"]

    # Duplicates preserved
    assert module_0.by_length([5, 5, 5]) == ["Five", "Five", "Five"]

    # Floats and strings that aren't dict keys are ignored
    assert module_0.by_length([1, "two", 2.5, 3]) == ["Three", "One"]

    # Large input with many invalid values
    assert module_0.by_length([9, 8, 7, 6, 5, 4, 3, 2, 1, 10, -10]) == [
        "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"
    ]

# Generated at 2026-11-02 13:46:03.670358
# Unit test for function by_length
def test_by_length():
    # nonce:08adab2c
    # Basic case: sorted descending, mapped to words
    assert module_0.by_length([2, 1, 1, 4, 5, 8, 2, 3]) == [
        "Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"
    ]

    # Empty input returns empty list
    assert module_0.by_length([]) == []

    # Out-of-range numbers are ignored
    assert module_0.by_length([1, -1, 55]) == ["One"]

    # All numbers out of range
    assert module_0.by_length([-5, 0, 10, 55]) == []

    # Single valid element
    assert module_0.by_length([9]) == ["Nine"]

    # Duplicates preserved
    assert module_0.by_length([3, 3, 3]) == ["Three", "Three", "Three"]

    # Already sorted descending input
    assert module_0.by_length([9, 8, 7]) == ["Nine", "Eight", "Seven"]

    # Mixed valid and invalid numbers, unsorted
    assert module_0.by_length([4, 100, 2, -3, 7]) == ["Seven", "Four", "Two"]

    # Input list is not mutated
    arr = [3, 1, 2]
    module_0.by_length(arr)
    assert arr == [3, 1, 2]

# Generated at 2026-11-02 13:47:02.520803
# Unit test for function by_length
def test_by_length():
    # Basic case: sort descending and convert to words
    assert module_0.by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]

    # Empty array returns empty list
    assert module_0.by_length([]) == []

    # Numbers outside 1-9 are ignored
    assert module_0.by_length([10, 0, 11]) == []

    # Mixed valid and invalid numbers: only valid ones kept
    assert module_0.by_length([1, -1, 55]) == ["One"]

    # Already sorted descending input
    assert module_0.by_length([9, 8, 7]) == ["Nine", "Eight", "Seven"]

    # Duplicates are preserved
    assert module_0.by_length([3, 3, 3]) == ["Three", "Three", "Three"]

    # Negative numbers are ignored
    assert module_0.by_length([-5, 2, -1]) == ["Two"]

    # Single element
    assert module_0.by_length([5]) == ["Five"]

    # All numbers 1-9 present
    assert module_0.by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [
        "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"
    ]

    print("All tests passed!")


if __name__ == "__main__":
    test_by_length()

# Generated at 2026-11-02 13:48:03.420287
# Unit test for function by_length
def test_by_length():
    assert module_0.by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    assert module_0.by_length([]) == []
    assert module_0.by_length([1, -1, 55]) == ["One"]
    assert module_0.by_length([9, 8, 7, 6, 5, 4, 3, 2, 1]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
    assert module_0.by_length([10, 11, 12]) == []
    assert module_0.by_length([5]) == ["Five"]
    assert module_0.by_length([-1, -2, -3]) == []
    assert module_0.by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
    assert module_0.by_length([3, 3, 3]) == ["Three", "Three", "Three"]
    assert module_0.by_length([0, 1, 0, 2]) == ["Two", "One"]
    assert module_0.by_length([4.5, 4]) == ["Four"]