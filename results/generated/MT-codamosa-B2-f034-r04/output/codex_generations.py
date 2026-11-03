

# Generated at 2026-11-02 21:29:15.598137
# Unit test for function unique
def test_unique():
    # Test with basic integers containing duplicates
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    
    # Test with empty list
    assert module_0.unique([]) == []
    
    # Test with single element
    assert module_0.unique([42]) == [42]
    
    # Test with all identical elements
    assert module_0.unique([7, 7, 7, 7]) == [7]
    
    # Test with negative numbers
    assert module_0.unique([-1, 1, -1, 0, 1]) == [-1, 0, 1]
    
    # Test with strings
    assert module_0.unique(["b", "a", "b", "c"]) == ["a", "b", "c"]
    
    # Test with floats
    assert module_0.unique([1.5, 2.5, 1.5, 3.0]) == [1.5, 2.5, 3.0]
    
    # Test that result is already sorted
    result = module_0.unique([10, 2, 33, 2, 10, 1])
    assert result == sorted(result)
    assert len(result) == 4

# Generated at 2026-11-02 21:30:39.855754
# Unit test for function unique
def test_unique():
    # Basic case: unsorted list with duplicates
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

    # Already sorted unique list
    assert module_0.unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Reverse sorted with duplicates
    assert module_0.unique([5, 4, 3, 2, 1, 1, 2, 3]) == [1, 2, 3, 4, 5]

    # Empty list
    assert module_0.unique([]) == []

    # Single element
    assert module_0.unique([42]) == [42]

    # All duplicates
    assert module_0.unique([7, 7, 7, 7]) == [7]

    # Negative numbers
    assert module_0.unique([-3, 1, -3, 0, 1, -10]) == [-10, -3, 0, 1]

    # Strings
    assert module_0.unique(["banana", "apple", "banana", "cherry"]) == ["apple", "banana", "cherry"]

    # Result should be a list
    assert isinstance(module_0.unique([1, 2, 3]), list)

    # Original input list should not be modified
    original = [3, 1, 2, 3]
    module_0.unique(original)
    assert original == [3, 1, 2, 3]

# Generated at 2026-11-02 21:33:03.752772
# Unit test for function unique
def test_unique():
    # Basic case with duplicates
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

    # Already sorted list
    assert module_0.unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Unsorted list with duplicates
    assert module_0.unique([3, 1, 2, 1, 3]) == [1, 2, 3]

    # Empty list
    assert module_0.unique([]) == []

    # Single element
    assert module_0.unique([42]) == [42]

    # All duplicates
    assert module_0.unique([7, 7, 7, 7]) == [7]

    # Negative numbers
    assert module_0.unique([-1, 5, -1, 0, 5, -10]) == [-10, -1, 0, 5]

    # Floats and ints (same value deduplicates)
    assert module_0.unique([1, 1.0, 2]) == [1, 2]

    # Strings
    assert module_0.unique(["b", "a", "b", "c"]) == ["a", "b", "c"]

    # Result contains no duplicates
    result = module_0.unique([4, 4, 1, 1, 3, 3, 2, 2])
    assert len(result) == len(set(result)) == 4
    assert result == sorted(result)

    print("All tests passed!")


# Run the test
test_unique()

# Generated at 2026-11-02 21:35:02.601293
# Unit test for function unique
def test_unique():
    # Basic case with duplicates and unsorted input
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

    # Already sorted unique list
    assert module_0.unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Empty list
    assert module_0.unique([]) == []

    # Single element
    assert module_0.unique([42]) == [42]

    # All duplicates
    assert module_0.unique([7, 7, 7, 7]) == [7]

    # Negative numbers
    assert module_0.unique([-1, 1, -1, 0, -5, 1]) == [-5, -1, 0, 1]

    # Two elements out of order
    assert module_0.unique([2, 1]) == [1, 2]

    # Result has no duplicates
    result = module_0.unique([3, 1, 3, 2, 1])
    assert len(result) == len(set(result))

    # Strings are sorted and deduplicated
    assert module_0.unique(["b", "a", "b", "c"]) == ["a", "b", "c"]

    # Floats and ints deduplicate by value
    assert module_0.unique([1.0, 1, 2, 2.0]) == [1, 2]

    # Input list is not modified
    original = [3, 1, 2]
    module_0.unique(original)
    assert original == [3, 1, 2]

    print("All tests passed!")


if __name__ == "__main__":
    test_unique()

# Generated at 2026-11-02 21:38:28.225174
# Unit test for function unique
def test_unique():
    # Test with a list of duplicates
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

    # Test with an empty list
    assert module_0.unique([]) == []

    # Test with a list of all duplicates
    assert module_0.unique([1, 1, 1, 1]) == [1]

    # Test with already sorted unique list
    assert module_0.unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Test with negative numbers
    assert module_0.unique([-1, 1, 0, -1, 2]) == [-1, 0, 1, 2]

    # Test with strings
    assert module_0.unique(["b", "a", "b", "c"]) == ["a", "b", "c"]

    # Test result is sorted
    result = module_0.unique([10, 2, 33, 2, 10, 7])
    assert result == sorted(result)
    assert result == [2, 7, 10, 33]

    # Test length matches number of unique elements
    assert len(module_0.unique([1, 2, 2, 3, 3, 3])) == 3