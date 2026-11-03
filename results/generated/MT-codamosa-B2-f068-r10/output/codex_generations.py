

# Generated at 2026-11-02 18:50:04.014778
# Unit test for function pluck
def test_pluck():
    # Empty array returns empty list
    assert module_0.pluck([]) == []
    
    # Array with no even values returns empty list
    assert module_0.pluck([1, 3, 5, 7]) == []
    
    # Single odd element returns empty list
    assert module_0.pluck([7]) == []
    
    # Basic case: smallest even value with its index
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    
    # All odd except one even
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    
    # Even value at index 0
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    
    # Duplicated smallest even: returns first occurrence index
    assert module_0.pluck([2, 4, 2, 6]) == [2, 0]
    
    # Single even element
    assert module_0.pluck([8]) == [8, 0]
    
    # Negative even values
    assert module_0.pluck([-2, -4, 3]) == [-4, 1]
    
    # Zero counts as even
    assert module_0.pluck([1, 0, 5]) == [0, 1]
    
    # All even values
    assert module_0.pluck([10, 6, 8]) == [6, 1]
    
    print("All tests passed!")


if __name__ == "__main__":
    test_pluck()

# Generated at 2026-11-02 18:51:23.040111
# Unit test for function pluck
def test_pluck():
# nonce:cd892c08
    # Empty array returns empty list
    assert module_0.pluck([]) == []
    
    # No even values returns empty list
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([7]) == []
    
    # Single even element
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([1, 2]) == [2, 1]
    
    # Classic examples
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    
    # Smallest even appears multiple times -> first index returned
    assert module_0.pluck([2, 2, 2]) == [2, 0]
    assert module_0.pluck([4, 2, 8, 2, 6]) == [2, 1]
    
    # Only odd values except one even
    assert module_0.pluck([1, 3, 5, 4, 7]) == [4, 3]
    
    # Even number at first position
    assert module_0.pluck([0, 3, 5]) == [0, 0]
    
    # Zero is even and smallest
    assert module_0.pluck([10, 0, 5, 2]) == [0, 1]
    
    # Negative even numbers
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]
    assert module_0.pluck([3, -2, -8]) == [-8, 2]
    
    # Larger array with mixed values
    assert module_0.pluck([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 1]
    
    # All values even, same value repeated
    assert module_0.pluck([6, 6, 6, 6]) == [6, 0]
    
    print("All tests passed!")

# Generated at 2026-11-02 18:53:17.037713
# Unit test for function pluck
def test_pluck():
    # Empty array returns empty list
    assert module_0.pluck([]) == []

    # Array with no even numbers returns empty list
    assert module_0.pluck([1, 3, 5, 7]) == []

    # Single even element returns value and its index
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([1]) == []

    # Multiple evens: smallest even value with its first index
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3, 4, 5]) == [2, 1]
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

    # Duplicate minimum evens: first occurrence index is returned
    assert module_0.pluck([2, 2, 1, 2]) == [2, 0]
    assert module_0.pluck([3, 4, 4, 6]) == [4, 1]

    # Odd numbers present but evens exist
    assert module_0.pluck([1, 3, 6, 8, 5]) == [6, 2]

    # All even numbers
    assert module_0.pluck([8, 6, 4, 2]) == [2, 3]

    # Zero counts as an even number
    assert module_0.pluck([7, 0, 9]) == [0, 1]

    # Negative even numbers are handled correctly
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]
    assert module_0.pluck([3, -2, -4]) == [-4, 2]

    # Larger array with mixed values
    assert module_0.pluck([10, 21, 32, 43, 54, 65, 76]) == [10, 0]

    print("All test_pluck tests passed!")


if __name__ == "__main__":
    test_pluck()

# Generated at 2026-11-02 18:55:17.498733
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []

    # No even values
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([1]) == []

    # Basic cases with even values
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

    # Single element (even)
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([0]) == [0, 0]

    # Smallest even appears multiple times -> first index returned
    assert module_0.pluck([2, 2, 4]) == [2, 0]
    assert module_0.pluck([4, 2, 2, 6]) == [2, 1]

    # Larger even value earlier but not minimum
    assert module_0.pluck([8, 6, 3, 1]) == [6, 1]

    # Negative numbers
    assert module_0.pluck([-2, -4, 3]) == [-4, 1]
    assert module_0.pluck([-4, -2]) == [-4, 0]

    # All zeros
    assert module_0.pluck([0, 0, 0]) == [0, 0]

    # Mixed with odd values around evens
    assert module_0.pluck([1, 9, 4, 7, 6, 5]) == [4, 2]

    print("All test_pluck tests passed!")


test_pluck()

# Generated at 2026-11-02 18:56:44.404112
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []

    # No even numbers
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([7]) == []

    # Single element, even
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([0]) == [0, 0]

    # Single element, odd
    assert module_0.pluck([3]) == []

    # Typical cases: smallest even with its index
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

    # Duplicated smallest even -> first index
    assert module_0.pluck([2, 2, 4]) == [2, 0]
    assert module_0.pluck([6, 4, 4, 8]) == [4, 1]

    # Even number larger than odds present
    assert module_0.pluck([1, 9, 4, 7, 6]) == [4, 2]

    # Negative even numbers
    assert module_0.pluck([-2, -4, 3]) == [-4, 1]
    assert module_0.pluck([-1, -3]) == []

    # Zero handling
    assert module_0.pluck([3, 0, 5, 2]) == [0, 1]

    print("All test_pluck tests passed!")


if __name__ == "__main__":
    test_pluck()