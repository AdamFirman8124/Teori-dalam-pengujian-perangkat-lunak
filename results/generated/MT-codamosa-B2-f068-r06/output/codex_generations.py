

# Generated at 2026-11-02 23:27:13.005326
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []
    
    # No even numbers
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([7]) == []
    
    # Basic case with evens
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    
    # Multiple occurrences of smallest even -> first index
    assert module_0.pluck([2, 4, 2, 6]) == [2, 0]
    assert module_0.pluck([5, 2, 3, 2]) == [2, 1]
    
    # Single element with even
    assert module_0.pluck([8]) == [8, 0]
    
    # Negative numbers
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]
    assert module_0.pluck([3, -2, -2]) == [-2, 1]
    
    # All evens
    assert module_0.pluck([10, 6, 8]) == [6, 1]
    
    # Zero as smallest even
    assert module_0.pluck([1, 0, 5, 2]) == [0, 1]

# Generated at 2026-11-02 23:29:10.558422
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []

    # No even numbers
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([7]) == []
    assert module_0.pluck([3]) == []

    # Single even element
    assert module_0.pluck([2]) == [2, 0]

    # Basic cases
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

    # All even values
    assert module_0.pluck([2, 4, 6]) == [2, 0]

    # Duplicate minimum evens -> first occurrence index
    assert module_0.pluck([4, 2, 2, 6]) == [2, 1]
    assert module_0.pluck([0, 2, 0]) == [0, 0]

    # Negative even numbers
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]
    assert module_0.pluck([-2, -4, 6]) == [-4, 1]

    # Even value larger than all odds
    assert module_0.pluck([1, 3, 8]) == [8, 2]

    # Zero as smallest even
    assert module_0.pluck([3, 0]) == [0, 1]

    # Larger mixed array
    assert module_0.pluck([1, 9, 4, 7, 6, 5, 2]) == [2, 6]


if __name__ == "__main__":
    test_pluck()
    print("All tests passed!")

# Generated at 2026-11-02 23:30:12.608970
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []
    # No even values
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([7]) == []
    # Single even value
    assert module_0.pluck([0]) == [0, 0]
    assert module_0.pluck([2]) == [2, 0]
    # Basic cases
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    # Duplicated smallest even value -> smallest index
    assert module_0.pluck([2, 2, 4]) == [2, 0]
    assert module_0.pluck([4, 2, 2]) == [2, 1]
    # Negative even values
    assert module_0.pluck([-2, -4, 3]) == [-4, 1]
    # Even value at first index
    assert module_0.pluck([8, 3, 5, 6]) == [6, 3]
    # Large mixed array
    assert module_0.pluck([1, 9, 4, 7, 6, 3, 2]) == [2, 6]
    print("All tests passed!")

test_pluck()

# Generated at 2026-11-02 23:31:13.747696
# Unit test for function pluck
def test_pluck():
    # Empty array returns empty list
    assert module_0.pluck([]) == []
    # No even values returns empty list
    assert module_0.pluck([1, 3, 5, 7]) == []
    # Single element array with even value
    assert module_0.pluck([4]) == [4, 0]
    # Single element array with odd value
    assert module_0.pluck([5]) == []
    # Smallest even value and its index
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    # Smallest even appears after odd numbers
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    # Multiple occurrences of smallest even - first index returned
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    # Larger array with multiple evens
    assert module_0.pluck([1, 2, 3, 4, 5, 6]) == [2, 1]
    # Negative even numbers
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]
    # All zeros
    assert module_0.pluck([0, 0, 0]) == [0, 0]
    # Even number larger than surrounding odds
    assert module_0.pluck([7, 8, 9]) == [8, 1]
    # Duplicate smallest evens at different positions
    assert module_0.pluck([2, 4, 2, 6]) == [2, 0]
    # Evens present only at the end
    assert module_0.pluck([1, 3, 5, 6]) == [6, 3]

# Generated at 2026-11-02 23:32:32.906484
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []
    # No even numbers
    assert module_0.pluck([1, 3, 5, 7]) == []
    # Single element, even
    assert module_0.pluck([2]) == [2, 0]
    # Single element, odd
    assert module_0.pluck([3]) == []
    # Basic case
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    # Smallest even appears multiple times -> first index
    assert module_0.pluck([1, 2, 3, 2, 4]) == [2, 1]
    # All even numbers
    assert module_0.pluck([8, 6, 4, 2]) == [2, 3]
    # Even number at the beginning
    assert module_0.pluck([0, 3, 5]) == [0, 0]
    # Larger array with mixed values
    assert module_0.pluck([7, 1, 5, 3, 6, 4]) == [4, 5]
    # Negative even numbers
    assert module_0.pluck([-2, -4, 3]) == [-4, 1]
    # Zero is even
    assert module_0.pluck([1, 0, 5, 2]) == [0, 1]
    print("All tests passed!")

test_pluck()