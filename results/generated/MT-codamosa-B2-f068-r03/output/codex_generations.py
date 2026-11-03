

# Generated at 2026-11-02 13:56:12.307443
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []
    
    # Array with no even numbers
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([1]) == []
    assert module_0.pluck([7, 9, 11]) == []
    
    # Single even number
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([1, 2]) == [2, 1]
    assert module_0.pluck([2, 3]) == [2, 0]
    
    # Normal cases
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    
    # Multiple occurrences of smallest even value - first index returned
    assert module_0.pluck([2, 2, 2]) == [2, 0]
    assert module_0.pluck([4, 2, 4, 2]) == [2, 1]
    
    # Zero as smallest even
    assert module_0.pluck([0, 1, 2]) == [0, 0]
    assert module_0.pluck([3, 0, 5]) == [0, 1]
    
    # Negative even numbers
    assert module_0.pluck([-2, 1, 2]) == [-2, 0]
    assert module_0.pluck([1, -4, -2]) == [-4, 1]
    
    # Larger array
    assert module_0.pluck([1, 3, 5, 6, 7, 8]) == [6, 3]
    assert module_0.pluck([10, 21, 32, 43, 54]) == [10, 0]

if __name__ == "__main__":
    test_pluck()
    print("All tests passed!")

# Generated at 2026-11-02 13:58:47.049827
# Unit test for function pluck
def test_pluck():
    # Empty array returns empty list
    assert module_0.pluck([]) == []

    # No even numbers returns empty list
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([7]) == []

    # Single even element
    assert module_0.pluck([4]) == [4, 0]
    assert module_0.pluck([0]) == [0, 0]

    # Basic cases: smallest even value and its index
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

    # Duplicate smallest even values: first occurrence index is returned
    assert module_0.pluck([2, 2, 3, 2]) == [2, 0]
    assert module_0.pluck([6, 5, 4, 4, 2, 2]) == [2, 4]

    # Negative even numbers
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]
    assert module_0.pluck([3, -2, -4]) == [-4, 2]

    # All even numbers
    assert module_0.pluck([2, 4, 6, 8]) == [2, 0]

    # Even number appears only at the end
    assert module_0.pluck([1, 3, 5, 8]) == [8, 3]

    # Mixed larger values
    assert module_0.pluck([100, 3, 50, 7]) == [50, 2]
    assert module_0.pluck([1, 2, 3, 4, 5, 6]) == [2, 1]

# Generated at 2026-11-02 14:00:20.600313
# Unit test for function pluck
def test_pluck():
    # Empty array returns empty list
    assert module_0.pluck([]) == []

    # No even numbers returns empty list
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([7]) == []

    # Single element cases
    assert module_0.pluck([0]) == [0, 0]
    assert module_0.pluck([2]) == [2, 0]

    # Standard cases: smallest even value and its index
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

    # Multiple occurrences of minimum even: first index returned
    assert module_0.pluck([2, 2, 2]) == [2, 0]
    assert module_0.pluck([4, 2, 8, 2]) == [2, 1]

    # Even number appears after odd numbers
    assert module_0.pluck([1, 3, 6, 5]) == [6, 2]

    # Negative even numbers
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]
    assert module_0.pluck([1, -2, 4]) == [-2, 1]

    # Zero is even and smallest
    assert module_0.pluck([3, 0, 8]) == [0, 1]

    # All even numbers
    assert module_0.pluck([8, 6, 4, 2]) == [2, 3]

    # Large values
    assert module_0.pluck([1000000, 999998]) == [999998, 1]

# Generated at 2026-11-02 14:02:40.576898
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []

    # No even numbers
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([7]) == []

    # Single even number
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([1, 2, 3]) == [2, 1]

    # Multiple evens, smallest is unique
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

    # Duplicate smallest evens -> first occurrence index
    assert module_0.pluck([2, 2, 4]) == [2, 0]
    assert module_0.pluck([5, 4, 4, 6]) == [4, 1]

    # Even numbers only
    assert module_0.pluck([8, 6, 4, 2]) == [2, 3]

    # Smallest even is zero
    assert module_0.pluck([1, 0, 5, 2]) == [0, 1]

    # Even number at last position
    assert module_0.pluck([1, 3, 5, 6]) == [6, 3]

    # Even number at first position
    assert module_0.pluck([10, 21, 3, 8]) == [8, 3]

    # Larger mixed array
    assert module_0.pluck([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 1]

    # Larger value where smaller odd values exist
    assert module_0.pluck([9, 9, 9, 12]) == [12, 3]