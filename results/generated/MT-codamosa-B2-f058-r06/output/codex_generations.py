

# Generated at 2026-11-03 00:50:10.717939
# Unit test for function common
def test_common():
    # Common elements exist
    assert module_0.common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []
    assert module_0.common([1, 2, 3], [3, 2, 1]) == [1, 2, 3]
    
    # Duplicates in input should not duplicate results
    assert module_0.common([1, 1, 2, 2, 3], [2, 3, 3, 4]) == [2, 3]
    
    # Empty lists
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], []) == []
    
    # Strings
    assert module_0.common(["apple", "banana"], ["banana", "cherry"]) == ["banana"]
    
    # Result is sorted even if inputs are unsorted
    assert module_0.common([9, 5, 1], [1, 9, 5]) == [1, 5, 9]
    
    # Mixed types
    assert module_0.common([1, "a", 2.0], ["a", 2.0, "b"]) == [2.0, "a"]

# Generated at 2026-11-03 00:50:58.638562
# Unit test for function common
def test_common():
    # Basic case with common elements
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    
    # No common elements
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []
    
    # Empty lists
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], []) == []
    
    # Duplicates in inputs should be deduplicated in output
    assert module_0.common([1, 1, 2, 2, 3], [2, 3, 3, 4]) == [2, 3]
    
    # Identical lists
    assert module_0.common([5, 3, 1], [5, 3, 1]) == [1, 3, 5]
    
    # Result should be sorted even if inputs are unsorted
    assert module_0.common([9, 7, 5], [5, 7, 9]) == [5, 7, 9]
    assert module_0.common([3, 1, 2], [2, 3, 1]) == [1, 2, 3]
    
    # Single common element
    assert module_0.common([1, 2, 3], [3]) == [3]
    assert module_0.common([3], [1, 2, 3]) == [3]
    
    # String elements
    assert module_0.common(["apple", "banana", "cherry"], ["banana", "cherry", "date"]) == ["banana", "cherry"]
    
    # Mixed types that are comparable
    assert module_0.common([1, "a", 2.0], [2.0, "a"]) == [2.0, "a"]
    
    # Negative numbers
    assert module_0.common([-1, -2, 0], [0, -1, 5]) == [-1, 0]
    
    # One element contained multiple times in both
    assert module_0.common([7, 7, 7], [7, 7]) == [7]
    
    # Lists of different lengths
    assert module_0.common([1, 2], [1, 2, 3, 4, 5]) == [1, 2]
    
    # Result is a list type
    assert isinstance(module_0.common([1], [1]), list)
    
    # Boolean and int equality (True == 1 in Python)
    assert module_0.common([True, 2], [1, 2]) == [1, 2]
    
    print("All tests passed!")


if __name__ == "__main__":
    test_common()

# Generated at 2026-11-03 00:52:30.488867
# Unit test for function common
def test_common():
    # Test with common elements
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    
    # Test with no common elements
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []
    
    # Test with empty lists
    assert module_0.common([], []) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], [1, 2, 3]) == []
    
    # Test with duplicate elements
    assert module_0.common([1, 1, 2, 2, 3], [2, 2, 3, 3, 4]) == [2, 3]
    
    # Test with strings
    assert module_0.common(["apple", "banana", "cherry"], ["banana", "cherry", "date"]) == ["banana", "cherry"]
    
    # Test result is sorted
    assert module_0.common([5, 3, 1], [1, 3, 5]) == [1, 3, 5]
    assert module_0.common([9, 7, 5], [5, 7, 9]) == [5, 7, 9]
    
    # Test with mixed types
    assert module_0.common([1, "a", 2.5], ["a", 2.5, 3]) == [2.5, "a"]
    
    # Test identical lists
    assert module_0.common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    
    # Test single element lists
    assert module_0.common([1], [1]) == [1]
    assert module_0.common([1], [2]) == []
    
    # Test negative numbers
    assert module_0.common([-1, -2, -3], [-2, -3, -4]) == [-3, -2]
    
    print("All tests passed!")


if __name__ == "__main__":
    test_common()

# Generated at 2026-11-03 00:53:46.980277
# Unit test for function common
def test_common():
    # Basic case with common elements
    assert module_0.common([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]

    # No common elements
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []

    # Duplicates in both lists should still return unique results
    assert module_0.common([1, 1, 2, 2, 3], [2, 2, 3, 3]) == [2, 3]

    # Empty lists
    assert module_0.common([], []) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], [1, 2, 3]) == []

    # One list is a subset of the other
    assert module_0.common([1, 2, 3], [1, 2, 3, 4, 5]) == [1, 2, 3]

    # Unsorted inputs should produce sorted output
    assert module_0.common([5, 3, 1], [1, 5, 9]) == [1, 5]

    # Works with strings
    assert module_0.common(["apple", "banana", "cherry"], ["banana", "date"]) == ["banana"]

    # Works with negative numbers and mixed values
    assert module_0.common([-1, 0, 5], [0, -1, 10]) == [-1, 0]

    # Single element lists
    assert module_0.common([7], [7]) == [7]
    assert module_0.common([7], [8]) == []

    # Common elements appear only once in result even if repeated many times
    assert module_0.common([1, 1, 1, 1], [1, 1]) == [1]

    # Works with floats
    assert module_0.common([1.5, 2.5, 3.5], [2.5, 3.5, 4.5]) == [2.5, 3.5]

    # Result is always sorted regardless of input order
    assert module_0.common([9, 4, 7], [7, 9, 4]) == [4, 7, 9]

    print("All tests passed!")


if __name__ == "__main__":
    test_common()

# Generated at 2026-11-03 00:55:40.849843
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
    
    # Test with duplicates in both lists
    assert module_0.common([1, 1, 2, 2, 3], [2, 2, 3, 3, 4]) == [2, 3]
    
    # Test with unsorted input, verifying sorted output
    assert module_0.common([5, 1, 3], [3, 5, 2]) == [3, 5]
    
    # Test with strings
    assert module_0.common(["apple", "banana", "cherry"], ["banana", "date", "apple"]) == ["apple", "banana"]
    
    # Test with mixed types
    assert module_0.common([1, "a", 2.5], ["a", 2.5, True]) == ["a", 2.5]
    
    # Test identical lists
    assert module_0.common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    
    # Test single common element
    assert module_0.common([1, 2], [2, 3]) == [2]
    
    # Test with negative numbers
    assert module_0.common([-1, -2, 3], [-2, 3, 4]) == [-2, 3]
    
    print("All tests passed!")


if __name__ == "__main__":
    test_common()