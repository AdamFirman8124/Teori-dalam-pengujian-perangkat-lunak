

# Generated at 2026-11-02 19:11:52.179342
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []

    # No even numbers
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([3]) == []

    # Single even element
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([0]) == [0, 0]

    # Basic cases
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3]) == [2, 1]

    # Smallest even at the start
    assert module_0.pluck([2, 4, 6]) == [2, 0]

    # Zero as smallest even, first occurrence index used
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

    # Duplicate minimum evens -> first occurrence index
    assert module_0.pluck([4, 2, 2, 6]) == [2, 1]
    assert module_0.pluck([0, 2, 0]) == [0, 0]

    # Negative even numbers
    assert module_0.pluck([-2, 4, 6]) == [-2, 0]
    assert module_0.pluck([4, -2, -2, 6]) == [-2, 1]

    # Larger evens only, index in original array
    assert module_0.pluck([1, 3, 8, 5, 8]) == [8, 2]

    # Even value after trailing odds
    assert module_0.pluck([7, 5, 3, 2]) == [2, 3]

    print("All tests passed!")


test_pluck()

# Generated at 2026-11-02 19:14:21.441729
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []

    # No even values
    assert module_0.pluck([1, 3, 5]) == []

    # Single even value
    assert module_0.pluck([2]) == [2, 0]

    # Multiple evens, smallest first
    assert module_0.pluck([2, 4, 6]) == [2, 0]

    # Multiple evens, smallest later in array
    assert module_0.pluck([4, 2, 3]) == [2, 1]

    # Ties: pick the first occurrence of the smallest even
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

    # Negative even values
    assert module_0.pluck([-2, -4, 3]) == [-4, 1]

    # Mixed odd and even
    assert module_0.pluck([1, 2, 3, 4, 5, 6]) == [2, 1]

    # All zeros
    assert module_0.pluck([0, 0, 0]) == [0, 0]

    # Large values
    assert module_0.pluck([1000, 999, 998, 997]) == [998, 2]

# Generated at 2026-11-02 19:16:00.407105
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []
    
    # No even numbers
    assert module_0.pluck([1, 3, 5]) == []
    
    # Single even number
    assert module_0.pluck([4]) == [4, 0]
    
    # Mixed odd and even numbers
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    
    # Smallest even is not first
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    
    # Duplicate smallest evens - returns first index
    assert module_0.pluck([2, 4, 2, 6]) == [2, 0]
    
    # Negative even numbers
    assert module_0.pluck([-4, -2, 3, 6]) == [-4, 0]
    
    # Zero is even
    assert module_0.pluck([1, 0, 3, 8]) == [0, 1]
    
    # All even numbers
    assert module_0.pluck([8, 6, 4, 2]) == [2, 3]
    
    # Large numbers
    assert module_0.pluck([1000000, 999999, 2]) == [2, 2]
    
    # Single odd number
    assert module_0.pluck([7]) == []
    
    # Even at last position
    assert module_0.pluck([1, 3, 5, 8]) == [8, 3]

# Generated at 2026-11-02 19:16:44.918445
# Unit test for function pluck
def test_pluck():
    # Empty array returns empty list
    assert module_0.pluck([]) == []

    # No even numbers returns empty list
    assert module_0.pluck([1, 3, 5]) == []

    # Basic case: smallest even with its index
    assert module_0.pluck([4, 2, 3]) == [2, 1]

    # Duplicate smallest even values: returns first occurrence index
    assert module_0.pluck([1, 2, 3, 2, 4]) == [2, 1]

    # Single even element
    assert module_0.pluck([2]) == [2, 0]

    # Single odd element
    assert module_0.pluck([5]) == []

    # Smallest even at the end
    assert module_0.pluck([8, 6, 4]) == [4, 2]

    # Negative even numbers
    assert module_0.pluck([-2, -4, 3]) == [-4, 1]

    # Zero counts as even
    assert module_0.pluck([0, 2, 5]) == [0, 0]

    # All elements even
    assert module_0.pluck([2, 4, 6]) == [2, 0]

    print("All tests passed!")

# Generated at 2026-11-02 19:17:29.023868
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []  # no even numbers
    assert module_0.pluck([2, 4, 6]) == [2, 0]  # smallest even at index 0
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]  # duplicates: first index of min
    assert module_0.pluck([4, 2, 3]) == [2, 1]  # min even not at first position
    assert module_0.pluck([1]) == []  # single odd element
    assert module_0.pluck([8]) == [8, 0]  # single even element
    assert module_0.pluck([-4, -2, 3, 5]) == [-4, 0]  # negative evens
    assert module_0.pluck([7, 1, 9, 2, 4]) == [2, 3]  # min even in middle
    assert module_0.pluck([0]) == [0, 0]  # zero is even
    assert module_0.pluck([3, 6, 3, 6]) == [6, 1]  # smallest even repeated


if __name__ == "__main__":
    test_pluck()
    print("All tests passed!")