

# Generated at 2026-11-02 06:31:10.000190
# Unit test for function common
def test_common():
    # Test basic common elements
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert module_0.common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

    # Test no common elements
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []

    # Test empty lists
    assert module_0.common([], []) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], [1, 2, 3]) == []

    # Test duplicates in both lists
    assert module_0.common([1, 1, 2, 2, 3], [2, 2, 3, 3, 4]) == [2, 3]

    # Test identical lists
    assert module_0.common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]

    # Test result is sorted
    assert module_0.common([5, 1, 3], [3, 5, 1]) == [1, 3, 5]

    # Test strings
    assert module_0.common(["apple", "banana", "cherry"], ["banana", "date", "apple"]) == ["apple", "banana"]

    # Test negative numbers
    assert module_0.common([-1, -2, 3], [-2, 3, 4]) == [-2, 3]

    # Test mixed types (int and float equal values)
    assert module_0.common([1, 2.0, 3], [2, 3.0, 4]) == [2, 3]

    # Test single common element
    assert module_0.common([7], [7]) == [7]

    # Test large lists
    assert module_0.common(list(range(100)), list(range(50, 150))) == list(range(50, 100))

# Generated at 2026-11-02 06:31:21.591904
# Unit test for function common
def test_common():
    # nonce:26ffc0c9
    # Common elements present
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    # No common elements
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []
    # Duplicates in inputs are deduplicated
    assert module_0.common([1, 1, 2, 2], [1, 1, 3]) == [1]
    # Empty list cases
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], []) == []
    # Result is sorted regardless of input order
    assert module_0.common([5, 3, 1], [1, 5, 3]) == [1, 3, 5]
    # Works with strings
    assert module_0.common(['a', 'b', 'c'], ['b', 'c', 'd']) == ['b', 'c']
    # Works with negative numbers and zero
    assert module_0.common([-1, -2, 0], [-2, 3, 0]) == [-2, 0]
    # Single element lists
    assert module_0.common([7], [7]) == [7]
    assert module_0.common([7], [8]) == []
    # One list fully contained in the other
    assert module_0.common([1, 2, 3, 4, 5], [2, 4]) == [2, 4]

# Generated at 2026-11-02 06:31:28.841434
# Unit test for function common
def test_common():
    # Basic case with common elements
    assert module_0.common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    
    # No common elements
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []
    
    # Duplicates in input should not cause duplicates in output
    assert module_0.common([1, 1, 2, 3], [1, 1, 3, 3]) == [1, 3]
    
    # Empty lists
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], []) == []
    
    # Identical lists
    assert module_0.common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    
    # Unsorted input should produce sorted output
    assert module_0.common([5, 1, 3], [3, 5, 2]) == [3, 5]
    
    # Strings
    assert module_0.common(["apple", "banana"], ["banana", "cherry"]) == ["banana"]
    
    # Overlapping string elements with duplicates
    assert module_0.common(["a", "b", "a"], ["a", "c", "a"]) == ["a"]
    
    # One list is a subset of the other
    assert module_0.common([1, 2], [1, 2, 3, 4]) == [1, 2]
    
    # Mixed integers and floats that are equal
    assert module_0.common([1, 2.0], [2, 1.0]) == [1, 2]
    
    # Negative numbers
    assert module_0.common([-1, -2, 3], [-2, 3, 4]) == [-2, 3]

# Generated at 2026-11-02 06:31:34.810723
# Unit test for function common
def test_common():
    # Test with common elements
    assert module_0.common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

    # Test with no common elements
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []

    # Test with empty lists
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], []) == []

    # Test with duplicate elements
    assert module_0.common([1, 2, 2, 3], [2, 2, 4]) == [2]

    # Test with identical lists
    assert module_0.common([5, 1, 3], [3, 1, 5]) == [1, 3, 5]

    # Test with strings
    assert module_0.common(["a", "b", "c"], ["b", "c", "d"]) == ["b", "c"]

    # Test with unsorted input, sorted output
    assert module_0.common([9, 4, 7], [7, 2, 9]) == [7, 9]

    # Test with mixed types (int and float equality)
    assert module_0.common([1, 2.0], [2, 3]) == [2]

    # Test with negative numbers
    assert module_0.common([-1, -2, 3], [-2, 3, 5]) == [-2, 3]

    # Test with one element
    assert module_0.common([1], [1]) == [1]

# Generated at 2026-11-02 06:31:39.595177
# Unit test for function common
def test_common():
    # Test with common elements
    assert module_0.common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    
    # Test with no common elements
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []
    
    # Test with empty lists
    assert module_0.common([], []) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], [1, 2, 3]) == []
    
    # Test with duplicates in both lists
    assert module_0.common([1, 1, 2, 2, 3], [2, 2, 3, 3, 4]) == [2, 3]
    
    # Test with strings
    assert module_0.common(["a", "b", "c"], ["b", "c", "d"]) == ["b", "c"]
    
    # Test with unsorted input, checking sorted output
    assert module_0.common([5, 1, 3], [3, 5, 2]) == [3, 5]
    
    # Test with mixed types (ints and floats that are equal)
    assert module_0.common([1, 2.0, 3], [2, 3.0, 4]) == [2, 3]
    
    # Test with identical lists
    assert module_0.common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    
    # Test result is a list
    result = module_0.common([1], [1])
    assert isinstance(result, list)
    
    # Test single element lists
    assert module_0.common([7], [7]) == [7]
    assert module_0.common([7], [8]) == []