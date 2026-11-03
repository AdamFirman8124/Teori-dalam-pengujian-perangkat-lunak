

# Generated at 2026-11-03 01:37:51.384624
# Unit test for function by_length
def test_by_length():
    # Basic test with mixed valid numbers
    assert module_0.by_length([2, 1, 1, 4, 5, 8, 2, 3]) == [
        "Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"
    ]

    # Empty array should return empty list
    assert module_0.by_length([]) == []

    # All numbers out of range should return empty list
    assert module_0.by_length([10, 11, 0, -1]) == []

    # Single valid number
    assert module_0.by_length([1]) == ["One"]

    # Single out-of-range number
    assert module_0.by_length([15]) == []

    # Duplicates preserved
    assert module_0.by_length([3, 3, 3]) == ["Three", "Three", "Three"]

    # Already sorted descending
    assert module_0.by_length([9, 8, 7]) == ["Nine", "Eight", "Seven"]

    # Reverse sorted input gets sorted descending
    assert module_0.by_length([1, 2, 3]) == ["Three", "Two", "One"]

    # Mix of valid and invalid numbers - invalid are ignored
    assert module_0.by_length([4, 100, 1, 0, 9, -5, 2]) == [
        "Nine", "Four", "Two", "One"
    ]

    # Result type check
    assert isinstance(module_0.by_length([1, 2]), list)

# Generated at 2026-11-03 01:39:05.523092
# Unit test for function by_length
def test_by_length():
    # Typical case: sort descending and map to words
    assert module_0.by_length([2, 1, 1, 4, 5, 8, 2, 3]) == [
        "Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"
    ]

    # Empty input returns empty list
    assert module_0.by_length([]) == []

    # Numbers outside 1-9 are ignored
    assert module_0.by_length([1, -1, 55]) == ["One"]

    # All numbers out of range
    assert module_0.by_length([0, 10, -5, 100]) == []

    # Already sorted input
    assert module_0.by_length([9, 8, 7]) == ["Nine", "Eight", "Seven"]

    # Reverse sorted input
    assert module_0.by_length([1, 2, 3]) == ["Three", "Two", "One"]

    # Duplicates preserved
    assert module_0.by_length([5, 5, 5]) == ["Five", "Five", "Five"]

    # Single element
    assert module_0.by_length([6]) == ["Six"]

    # Mixed valid and invalid values
    assert module_0.by_length([4, 12, 3, 0, 9]) == ["Nine", "Four", "Three"]

    # Full range 1-9
    assert module_0.by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [
        "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"
    ]

# Generated at 2026-11-03 01:40:42.725476
# Unit test for function by_length
def test_by_length():
    # nonce:7dee3ae4
    # Normal case: sort descending, map to words, duplicates preserved
    assert module_0.by_length([2, 1, 1, 4, 5, 8, 2, 3]) == [
        "Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"
    ]

    # Empty input returns empty list
    assert module_0.by_length([]) == []

    # All numbers out of range (1-9) are ignored
    assert module_0.by_length([-1, -2, 0, 10, 55]) == []

    # Mixed valid and invalid numbers - only valid ones mapped
    assert module_0.by_length([1, -1, 55]) == ["One"]

    # Already sorted descending input
    assert module_0.by_length([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [
        "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"
    ]

    # Single out-of-range element
    assert module_0.by_length([0]) == []
    assert module_0.by_length([100]) == []

    # Single valid element
    assert module_0.by_length([3]) == ["Three"]

    # Boundary values only
    assert module_0.by_length([1, 9]) == ["Nine", "One"]

    # Unsorted with negatives and large numbers interleaved
    assert module_0.by_length([4, -3, 7, 12, 2, 0]) == ["Seven", "Four", "Two"]

    # Duplicates of boundary values
    assert module_0.by_length([9, 9, 1, 1]) == ["Nine", "Nine", "One", "One"]

# Generated at 2026-11-03 01:42:56.737180
# Unit test for function by_length
def test_by_length():
    # Basic case with all numbers 1-9
    assert module_0.by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]

    # Empty array
    assert module_0.by_length([]) == []

    # Numbers outside 1-9 range are ignored
    assert module_0.by_length([1, -1, 55]) == ["One"]

    # All numbers out of range
    assert module_0.by_length([10, 0, -5, 100]) == []

    # Single element
    assert module_0.by_length([9]) == ["Nine"]

    # Duplicates preserved
    assert module_0.by_length([3, 3, 3]) == ["Three", "Three", "Three"]

    # Already sorted input (descending)
    assert module_0.by_length([9, 8, 7]) == ["Nine", "Eight", "Seven"]

    # Already sorted input (ascending)
    assert module_0.by_length([1, 2, 3]) == ["Three", "Two", "One"]

    # Mixed valid and invalid values
    assert module_0.by_length([4, 15, 2, -3, 7]) == ["Seven", "Four", "Two"]

    # Floats not in dict are ignored
    assert module_0.by_length([1.5, 2]) == ["Two"]

    # Result is a list
    assert isinstance(module_0.by_length([1]), list)

    # Input list is not mutated
    arr = [3, 1, 2]
    module_0.by_length(arr)
    assert arr == [3, 1, 2]

    print("All tests passed!")


if __name__ == "__main__":
    test_by_length()

# Generated at 2026-11-03 01:43:55.521422
# Unit test for function by_length
def test_by_length():
    # Test with numbers 1 through 9
    assert module_0.by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]

    # Test with empty array
    assert module_0.by_length([]) == []

    # Test with numbers outside 1-9 range (should be ignored)
    assert module_0.by_length([1, -1, 55]) == ["One"]

    # Test with all invalid numbers
    assert module_0.by_length([0, 10, -5, 100]) == []

    # Test with single element
    assert module_0.by_length([9]) == ["Nine"]

    # Test with duplicates
    assert module_0.by_length([3, 3, 3]) == ["Three", "Three", "Three"]

    # Test reverse ordering
    assert module_0.by_length([1, 2, 3]) == ["Three", "Two", "One"]

    # Test mixed valid and invalid numbers
    assert module_0.by_length([4, 7, 12, 2, 0]) == ["Seven", "Four", "Two"]

    print("All tests passed!")


if __name__ == "__main__":
    test_by_length()