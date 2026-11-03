

# Generated at 2026-11-03 05:06:21.204022
# Unit test for function unique
def test_unique():
    # Basic test with duplicates and unsorted input
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

    # Empty list
    assert module_0.unique([]) == []

    # Single element
    assert module_0.unique([1]) == [1]

    # All duplicates
    assert module_0.unique([2, 2, 2]) == [2]

    # Already sorted unique elements
    assert module_0.unique([1, 2, 3]) == [1, 2, 3]

    # Reverse sorted input
    assert module_0.unique([3, 2, 1]) == [1, 2, 3]

    # Negative numbers
    assert module_0.unique([-3, 1, -3, 0, 1]) == [-3, 0, 1]

    # Strings
    assert module_0.unique(['b', 'a', 'b', 'c']) == ['a', 'b', 'c']

    # Mixed duplicates of negatives and positives
    assert module_0.unique([0, -1, 0, -1, 5]) == [-1, 0, 5]

    # Result is a list
    assert isinstance(module_0.unique([3, 1, 2]), list)

    # Result length matches number of unique elements
    assert len(module_0.unique([1, 1, 2, 2, 3])) == 3

    # Large numbers
    assert module_0.unique([1000000, 999999, 1000000]) == [999999, 1000000]

    # Original list is not modified
    original = [3, 1, 3]
    module_0.unique(original)
    assert original == [3, 1, 3]

# Generated at 2026-11-03 05:10:02.997951
# Unit test for function unique
def test_unique():
    # Basic case with duplicates
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    
    # Empty list
    assert module_0.unique([]) == []
    
    # Single element
    assert module_0.unique([1]) == [1]
    
    # Already unique and sorted
    assert module_0.unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Reverse sorted with duplicates
    assert module_0.unique([5, 4, 3, 2, 1, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Negative numbers
    assert module_0.unique([-3, -1, -3, 0, 2, -1]) == [-3, -1, 0, 2]
    
    # All duplicates
    assert module_0.unique([7, 7, 7, 7]) == [7]
    
    # Strings
    assert module_0.unique(["banana", "apple", "banana", "cherry"]) == ["apple", "banana", "cherry"]
    
    # Mixed floats and ints
    assert module_0.unique([1.5, 2, 1.5, 3.0]) == [1.5, 2, 3.0]
    
    # Result contains no duplicates
    result = module_0.unique([10, 20, 10, 30, 20])
    assert len(result) == len(set(result))
    
    print("All tests passed!")


test_unique()

# Generated at 2026-11-03 05:12:59.532645
# Unit test for function unique
def test_unique():
    # Basic case with duplicates
    assert module_0.unique([5, 3, 5, 2, 3, 1]) == [1, 2, 3, 5]
    # Already sorted unique list
    assert module_0.unique([1, 2, 3]) == [1, 2, 3]
    # Empty list
    assert module_0.unique([]) == []
    # Single element
    assert module_0.unique([7]) == [7]
    # Negative numbers
    assert module_0.unique([-1, 2, -1, 0, 2]) == [-1, 0, 2]
    # Strings
    assert module_0.unique(["b", "a", "b", "c"]) == ["a", "b", "c"]
    # All duplicates
    assert module_0.unique([4, 4, 4, 4]) == [4]
    # Result contains no duplicates
    result = module_0.unique([10, 5, 10, 5, 1])
    assert len(result) == len(set(result))
    # Result is sorted
    assert result == sorted(result)
    # Floats and ints mix
    assert module_0.unique([2.5, 2.5, 1]) == [1, 2.5]