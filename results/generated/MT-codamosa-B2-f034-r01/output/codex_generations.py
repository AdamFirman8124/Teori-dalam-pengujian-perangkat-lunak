

# Generated at 2026-11-01 20:24:00.023449
# Unit test for function unique
def test_unique():
    # Basic case with duplicates
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]

    # Already sorted list without duplicates
    assert module_0.unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Unsorted list without duplicates
    assert module_0.unique([10, 2, 33, 4]) == [2, 4, 10, 33]

    # List with negative numbers
    assert module_0.unique([-1, -5, 0, 3, -1, 3]) == [-5, -1, 0, 3]

    # Empty list
    assert module_0.unique([]) == []

    # Single element
    assert module_0.unique([42]) == [42]

    # All identical elements
    assert module_0.unique([7, 7, 7, 7]) == [7]

    # Floats and ints
    assert module_0.unique([1.5, 2, 1.5, 3.0, 2]) == [1.5, 2, 3.0]

    # Strings
    assert module_0.unique(["banana", "apple", "cherry", "apple"]) == ["apple", "banana", "cherry"]

    # Result should be a new list (input unchanged)
    original = [3, 1, 2]
    result = module_0.unique(original)
    assert original == [3, 1, 2]
    assert result == [1, 2, 3]

    # Result contains no duplicates even for large input
    data = list(range(100)) * 3
    assert len(module_0.unique(data)) == 100
    assert module_0.unique(data) == list(range(100))

# Generated at 2026-11-01 20:24:18.965404
# Unit test for function unique
def test_unique():
    # Basic case with duplicates
    assert module_0.unique([5, 3, 5, 2, 3, 1]) == [1, 2, 3, 5]

    # Empty list
    assert module_0.unique([]) == []

    # List with no duplicates
    assert module_0.unique([1, 2, 3]) == [1, 2, 3]

    # Single element
    assert module_0.unique([7]) == [7]

    # Negative numbers
    assert module_0.unique([-1, 2, -1, 0, 2]) == [-1, 0, 2]

    # Already sorted unique list
    assert module_0.unique([1, 2, 3, 4]) == [1, 2, 3, 4]

    # Unsorted input with duplicates
    assert module_0.unique([10, 9, 10, 8, 9]) == [8, 9, 10]

    # Strings
    assert module_0.unique(["b", "a", "b", "c"]) == ["a", "b", "c"]

    # Result should be a list
    assert isinstance(module_0.unique([3, 1, 2]), list)

    # Duplicates removed correctly (length check)
    assert len(module_0.unique([1, 1, 1, 1])) == 1

    print("All test_unique tests passed!")


# Run the test
if __name__ == "__main__":
    test_unique()

# Generated at 2026-11-01 20:24:47.373921
# Unit test for function unique
def test_unique():
    # Basic case with duplicates
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
    assert module_0.unique([-3, -1, -2, -3, 0, 1]) == [-3, -2, -1, 0, 1]
    
    # Strings
    assert module_0.unique(["banana", "apple", "cherry", "apple"]) == ["apple", "banana", "cherry"]
    
    # Mixed floats and ints (equal values dedupe)
    assert module_0.unique([1, 1.0, 2]) == [1, 2]
    
    # Unsorted input preserves output ordering correctness
    result = module_0.unique([10, 2, 33, 2, 10, 55])
    assert result == sorted(result)
    assert len(result) == len(set(result))

# Generated at 2026-11-01 20:24:58.185750
# Unit test for function unique
def test_unique():
    # Basic test with duplicates
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    
    # Empty list
    assert module_0.unique([]) == []
    
    # Single element
    assert module_0.unique([1]) == [1]
    
    # All duplicates
    assert module_0.unique([7, 7, 7, 7]) == [7]
    
    # Already sorted unique elements
    assert module_0.unique([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Reverse sorted with duplicates
    assert module_0.unique([10, 9, 8, 9, 10]) == [8, 9, 10]
    
    # Negative numbers
    assert module_0.unique([-1, 1, -1, 0, 1]) == [-1, 0, 1]
    
    # Strings
    assert module_0.unique(["banana", "apple", "banana", "cherry"]) == ["apple", "banana", "cherry"]
    
    # Mixed floats and ints
    assert module_0.unique([1.5, 2, 1.5, 3.0]) == [1.5, 2, 3.0]
    
    # Verify result is a list
    assert isinstance(module_0.unique([3, 1, 2]), list)
    
    # Verify input list is not modified
    original = [3, 1, 3, 2]
    module_0.unique(original)
    assert original == [3, 1, 3, 2]

# Generated at 2026-11-01 20:25:05.769526
# Unit test for function unique
def test_unique():
    # Basic case with duplicates and unsorted input
    assert module_0.unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]
    # Empty list
    assert module_0.unique([]) == []
    # Single element
    assert module_0.unique([1]) == [1]
    # Already unique and sorted
    assert module_0.unique([1, 2, 3]) == [1, 2, 3]
    # Negative numbers and mixed values
    assert module_0.unique([-3, -1, -3, 2, 0, 2]) == [-3, -1, 0, 2]
    # All duplicates
    assert module_0.unique([7, 7, 7, 7]) == [7]
    # Reverse order input
    assert module_0.unique([4, 3, 2, 1]) == [1, 2, 3, 4]