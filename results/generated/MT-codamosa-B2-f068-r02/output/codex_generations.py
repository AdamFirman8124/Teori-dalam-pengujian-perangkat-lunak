

# Generated at 2026-11-02 08:52:37.149884
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []
    # Smallest even value appears once
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    # Smallest even value appears multiple times -> return first index
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert module_0.pluck([1, 2, 3, 0, 5, 3]) == [0, 3]
    # Duplicate smallest even values
    assert module_0.pluck([5, 4, 8, 4, 8]) == [4, 1]
    # Only one even value
    assert module_0.pluck([7, 6, 7, 1]) == [6, 1]
    # No even values
    assert module_0.pluck([7, 9, 7, 1]) == []
    # Single element arrays
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([0]) == [0, 0]
    assert module_0.pluck([3]) == []
    # Negative even values
    assert module_0.pluck([-4, -2, 6]) == [-4, 0]
    assert module_0.pluck([3, -2, -4, 5]) == [-4, 2]
    # Even value at last index
    assert module_0.pluck([1, 3, 5, 8]) == [8, 3]

# Generated at 2026-11-02 08:52:53.773524
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []

    # No even values
    assert module_0.pluck([1, 3, 5, 7]) == []

    # Basic case with evens
    assert module_0.pluck([4, 2, 3]) == [2, 1]

    # Smallest even appears multiple times -> first index
    assert module_0.pluck([1, 2, 3, 2, 5, 2]) == [2, 1]

    # Single even element
    assert module_0.pluck([8]) == [8, 0]

    # Single odd element
    assert module_0.pluck([7]) == []

    # Zero is even and smallest
    assert module_0.pluck([5, 0, 3, 0, 7]) == [0, 1]

    # Negative even numbers
    assert module_0.pluck([-4, -2, 3, 6]) == [-4, 0]

    # Evens out of order, smallest last
    assert module_0.pluck([10, 8, 6, 4]) == [4, 3]

    # Mixed odds and evens, smallest even not at start
    assert module_0.pluck([1, 9, 4, 7, 6, 2]) == [2, 5]

    # All same even value
    assert module_0.pluck([2, 2, 2]) == [2, 0]

    print("All tests passed!")


if __name__ == "__main__":
    test_pluck()

# Generated at 2026-11-02 08:53:21.429871
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []

    # No even numbers
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([7, 9, 7, 1]) == []
    assert module_0.pluck([1]) == []

    # Single element with even number
    assert module_0.pluck([0]) == [0, 0]
    assert module_0.pluck([4]) == [4, 0]

    # Smallest even at various positions
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([3, 5, 2, 8]) == [2, 2]
    assert module_0.pluck([8, 6, 4]) == [4, 2]
    assert module_0.pluck([7, 6, 7, 1]) == [6, 1]

    # Zero is the smallest even
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert module_0.pluck([1, 2, 3, 0, 5, 3]) == [0, 3]

    # Duplicate smallest even -> first occurrence index
    assert module_0.pluck([5, 4, 8, 4, 8]) == [4, 1]
    assert module_0.pluck([2, 4, 2, 6]) == [2, 0]
    assert module_0.pluck([2, 2, 2]) == [2, 0]

    # Negative even numbers
    assert module_0.pluck([-2, -4, 3]) == [-4, 1]
    assert module_0.pluck([-4, -2, -6]) == [-6, 2]
    assert module_0.pluck([-1, 1, -3]) == []

    # Mixed values
    assert module_0.pluck([1, 2, 3, 4, 5, 6]) == [2, 1]
    assert module_0.pluck([10, 20, 30]) == [10, 0]
    assert module_0.pluck([9, 8, 7, 6, 5]) == [6, 3]

# Generated at 2026-11-02 08:54:07.298243
# Unit test for function pluck
def test_pluck():
    # Empty array returns empty list
    assert module_0.pluck([]) == []

    # No even values returns empty list
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([1]) == []
    assert module_0.pluck([3, 5, 7, 9]) == []

    # Single even element
    assert module_0.pluck([0]) == [0, 0]
    assert module_0.pluck([2]) == [2, 0]

    # Multiple evens: return smallest even value and its index
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3, 4, 5, 6]) == [2, 1]
    assert module_0.pluck([10, 8, 6, 4, 2]) == [2, 4]

    # Ties on value: index of first occurrence is returned
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert module_0.pluck([2, 2, 2]) == [2, 0]

    # Even at the end of array
    assert module_0.pluck([1, 3, 5, 4]) == [4, 3]

    # Negative even values are handled correctly
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]
    assert module_0.pluck([-3, -2, -4]) == [-4, 2]
    assert module_0.pluck([-1]) == []

    # Mix of large numbers
    assert module_0.pluck([1000001, 1000000, 999998]) == [999998, 2]

    # Zero counts as even
    assert module_0.pluck([1, 0, 2]) == [0, 1]

# Generated at 2026-11-02 08:54:48.364075
# Unit test for function pluck
def test_pluck():
    # Empty array returns empty list
    assert module_0.pluck([]) == []
    
    # Array with no even values returns empty list
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([1]) == []
    
    # Single even element
    assert module_0.pluck([4]) == [4, 0]
    
    # Basic case with evens
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    
    # Multiple even values, smallest returned
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    
    # Duplicate smallest even values -> first index returned
    assert module_0.pluck([2, 2, 3, 2]) == [2, 0]
    assert module_0.pluck([4, 2, 6, 2]) == [2, 1]
    
    # Negative even numbers
    assert module_0.pluck([-2, -4, 3]) == [-4, 1]
    assert module_0.pluck([-4, -4, 6]) == [-4, 0]
    
    # Even number at the end
    assert module_0.pluck([1, 3, 7, 8]) == [8, 3]
    
    # All even numbers
    assert module_0.pluck([8, 6, 4, 2]) == [2, 3]
    
    # Zero is even
    assert module_0.pluck([1, 0, 5]) == [0, 1]
    
    # Larger array
    assert module_0.pluck([7, 9, 2, 11, 4, 6]) == [2, 2]
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_pluck()