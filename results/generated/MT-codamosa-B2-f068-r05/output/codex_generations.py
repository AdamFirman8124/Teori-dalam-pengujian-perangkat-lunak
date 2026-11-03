

# Generated at 2026-11-03 02:25:36.460199
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []

    # No even values
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([7]) == []

    # Single even value
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([1, 2, 3]) == [2, 1]

    # Multiple evens, smallest at various positions
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([2, 4, 6]) == [2, 0]
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

    # Duplicate smallest even -> first occurrence index
    assert module_0.pluck([1, 2, 3, 2, 4]) == [2, 1]
    assert module_0.pluck([0, 3, 0, 5]) == [0, 0]

    # Negative even values
    assert module_0.pluck([-2, -4, 3]) == [-4, 1]
    assert module_0.pluck([-1, 0, 1]) == [0, 1]

    # Large mixed array
    assert module_0.pluck([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [2, 7]

    print("All tests passed!")


if __name__ == "__main__":
    test_pluck()

# Generated at 2026-11-03 02:27:47.331597
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []
    
    # No even numbers
    assert module_0.pluck([1, 3, 5]) == []
    
    # Single even number
    assert module_0.pluck([2]) == [2, 0]
    
    # Basic case with one even
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    
    # Multiple evens, smallest comes first
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    
    # Ties: smallest value with earliest index wins
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    
    # Even value at the end
    assert module_0.pluck([1, 3, 6]) == [6, 2]
    
    # All evens, pick minimum
    assert module_0.pluck([8, 4, 6]) == [4, 1]
    
    # Zero is even
    assert module_0.pluck([1, 0, 5]) == [0, 1]
    
    # Negative even numbers
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]
    
    # Odd values larger than evens
    assert module_0.pluck([7, 2, 9, 4]) == [2, 1]
    
    # Single element, odd
    assert module_0.pluck([3]) == []
    
    # Duplicated smallest even
    assert module_0.pluck([2, 2, 1]) == [2, 0]
    
    print("All test_pluck tests passed!")


if __name__ == "__main__":
    test_pluck()

# Generated at 2026-11-03 02:30:05.202496
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []

    # No even values
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([1]) == []

    # Single element, even
    assert module_0.pluck([4]) == [4, 0]
    assert module_0.pluck([0]) == [0, 0]

    # Single element, odd
    assert module_0.pluck([3]) == []

    # Multiple evens, smallest even first
    assert module_0.pluck([2, 4, 6]) == [2, 0]

    # Smallest even appears later
    assert module_0.pluck([4, 2, 3]) == [2, 1]

    # Duplicate smallest evens - should return first index
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert module_0.pluck([2, 2, 1]) == [2, 0]

    # Mixed odd and even values
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([7, 6, 5, 4, 3, 2]) == [2, 5]

    # Contains zero
    assert module_0.pluck([1, 0, 5]) == [0, 1]

    # Negative even numbers
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]
    assert module_0.pluck([3, -2, -4]) == [-4, 2]
    assert module_0.pluck([-1, -3, -5]) == []

    # Larger array
    assert module_0.pluck([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 9]

    # All same even values
    assert module_0.pluck([6, 6, 6]) == [6, 0]

    print("All tests passed!")


test_pluck()

# Generated at 2026-11-03 02:31:15.688145
# Unit test for function pluck
def test_pluck():
    # Empty array returns empty list
    assert module_0.pluck([]) == []

    # Array with no even values returns empty list
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([7]) == []

    # Single even element
    assert module_0.pluck([0]) == [0, 0]
    assert module_0.pluck([4]) == [4, 0]

    # Basic cases: smallest even value and its index
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

    # Smallest even is at the first position
    assert module_0.pluck([2, 4, 6]) == [2, 0]

    # Smallest even is at the last position
    assert module_0.pluck([6, 4, 2]) == [2, 2]

    # Duplicate smallest even values: first occurrence index returned
    assert module_0.pluck([3, 2, 5, 2, 7]) == [2, 1]
    assert module_0.pluck([0, 3, 0, 5]) == [0, 0]

    # Even values larger than odd values present
    assert module_0.pluck([9, 8, 7, 6]) == [6, 3]

    # Negative even values
    assert module_0.pluck([-2, -4, 3]) == [-4, 1]

# Generated at 2026-11-03 02:32:51.903228
# Unit test for function pluck
def test_pluck():
    # Empty array returns empty list
    assert module_0.pluck([]) == []

    # No even values returns empty list
    assert module_0.pluck([7, 9, 7, 1]) == []
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([1]) == []

    # Single even value
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([1, 3, 2, 5]) == [2, 2]

    # Smallest even value is returned with its index
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([5, 4, 8, 4, 8]) == [4, 1]
    assert module_0.pluck([7, 6, 7, 1]) == [6, 1]

    # Zero is the smallest even value; first occurrence index is used
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert module_0.pluck([1, 2, 3, 0, 5, 3]) == [0, 3]

    # Ties: first occurrence of the smallest even value wins
    assert module_0.pluck([2, 2, 4]) == [2, 0]
    assert module_0.pluck([4, 2, 2]) == [2, 1]

    # Negative even values are handled correctly
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]
    assert module_0.pluck([1, -2, -4]) == [-4, 2]

    # All elements even
    assert module_0.pluck([8, 6, 4]) == [4, 2]
    assert module_0.pluck([0, 0]) == [0, 0]

    print("All tests passed!")


if __name__ == "__main__":
    test_pluck()