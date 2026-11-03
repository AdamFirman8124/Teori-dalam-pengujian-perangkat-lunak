

# Generated at 2026-11-02 09:28:01.292423
# Unit test for function by_length
def test_by_length():
    # Test with mixed numbers that should be sorted descending and mapped to words
    assert module_0.by_length([2, 1, 1, 4, 5, 8, 2, 3]) == [
        "Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"
    ]

    # Test with empty array
    assert module_0.by_length([]) == []

    # Test with values outside 1-9 range (should be ignored)
    assert module_0.by_length([1, -1, 55]) == ["One"]

    # Test with all invalid values
    assert module_0.by_length([0, -5, 10, 100]) == []

    # Test with single element
    assert module_0.by_length([9]) == ["Nine"]

    # Test with duplicates
    assert module_0.by_length([3, 3, 3]) == ["Three", "Three", "Three"]

    # Test that sorting is in descending order
    assert module_0.by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [
        "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"
    ]

    # Test with floats (keys won't match dict, should be ignored)
    assert module_0.by_length([1.5, 2]) == ["Two"]

    # Test with already sorted descending input
    assert module_0.by_length([5, 4, 3]) == ["Five", "Four", "Three"]

    print("All tests passed!")

# Generated at 2026-11-02 09:29:59.311203
# Unit test for function by_length
def test_by_length():
    # Test with a typical array containing numbers 1-9
    assert module_0.by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
    # Test with empty array
    assert module_0.by_length([]) == []
    
    # Test with numbers outside the range (should be ignored)
    assert module_0.by_length([1, -1, 55]) == ["One"]
    
    # Test with all numbers 1-9 in reverse order
    assert module_0.by_length([9, 8, 7, 6, 5, 4, 3, 2, 1]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
    
    # Test with all numbers 1-9 in random order
    assert module_0.by_length([3, 1, 7, 5, 9, 2, 8, 6, 4]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
    
    # Test with duplicates
    assert module_0.by_length([3, 3, 3]) == ["Three", "Three", "Three"]
    
    # Test with only invalid numbers
    assert module_0.by_length([0, 10, -5, 100]) == []
    
    # Test with mixed valid and invalid numbers
    assert module_0.by_length([4, 12, 2, 0, 7]) == ["Seven", "Four", "Two"]
    
    # Test with single element
    assert module_0.by_length([5]) == ["Five"]
    
    # Test that sorting is descending
    assert module_0.by_length([1, 2, 3]) == ["Three", "Two", "One"]

# Generated at 2026-11-02 09:32:41.180211
# Unit test for function by_length
def test_by_length():
    # Basic case: numbers 1-9 sorted descending and mapped to names
    assert module_0.by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]

    # Empty array returns empty list
    assert module_0.by_length([]) == []

    # Numbers outside 1-9 are ignored
    assert module_0.by_length([0, 10, 5]) == ["Five"]

    # All out-of-range numbers return empty list
    assert module_0.by_length([0, 10, -1, 100]) == []

    # Duplicates are preserved
    assert module_0.by_length([3, 3, 3]) == ["Three", "Three", "Three"]

    # Already sorted descending input
    assert module_0.by_length([9, 8, 7]) == ["Nine", "Eight", "Seven"]

    # Single element
    assert module_0.by_length([1]) == ["One"]

    # Mixed valid and invalid values
    assert module_0.by_length([4, 12, 6, 0, 1]) == ["Six", "Four", "One"]

    # Reverse sorted input gets sorted descending
    assert module_0.by_length([1, 2, 3]) == ["Three", "Two", "One"]

    # Result is empty for empty-like inputs
    assert module_0.by_length(list(range(10, 20))) == []

    print("All tests passed!")


if __name__ == "__main__":
    test_by_length()