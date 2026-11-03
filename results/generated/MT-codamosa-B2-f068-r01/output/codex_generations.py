

# Generated at 2026-11-02 23:38:58.645904
# Unit test for function pluck
def test_pluck():
    # Empty array returns []
    assert module_0.pluck([]) == []

    # No even values returns []
    assert module_0.pluck([1, 3, 5, 7]) == []

    # Single even value
    assert module_0.pluck([2]) == [2, 0]

    # Single odd value returns []
    assert module_0.pluck([3]) == []

    # Basic case: smallest even with its index
    assert module_0.pluck([4, 2, 3]) == [2, 1]

    # Smallest even not at index 0
    assert module_0.pluck([1, 2, 3]) == [2, 1]

    # Duplicate smallest evens: first occurrence index returned
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

    # Duplicated even minimum at the end
    assert module_0.pluck([6, 4, 4]) == [4, 1]

    # Negative even values
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]

    # Mixed positive and negative
    assert module_0.pluck([7, -2, 5, -8]) == [-8, 3]

    # Zero is the smallest even
    assert module_0.pluck([0, 98, 76]) == [0, 0]

    # Evens appear after odds
    assert module_0.pluck([1, 3, 6, 8]) == [6, 2]

    # Large values
    assert module_0.pluck([1000000, 999998, 3]) == [999998, 1]

# Generated at 2026-11-02 23:40:37.196165
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []
    # No even numbers
    assert module_0.pluck([1, 3, 5]) == []
    # Single even element
    assert module_0.pluck([4]) == [4, 0]
    # Multiple elements, smallest even at start
    assert module_0.pluck([2, 4, 6]) == [2, 0]
    # Multiple elements, smallest even in middle
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    # Smallest even appears multiple times, return first index
    assert module_0.pluck([4, 2, 2, 6]) == [2, 1]
    # Even value larger than odd values
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    # All odd numbers
    assert module_0.pluck([1, 3, 7, 9]) == []
    # Zero counts as even
    assert module_0.pluck([0, 1, 2]) == [0, 0]
    # Negative even numbers
    assert module_0.pluck([3, -2, 5, -4]) == [-4, 3]
    # Even number after several odds
    assert module_0.pluck([1, 3, 5, 8, 7, 6]) == [6, 3]

test_pluck()
print("All tests passed!")

# Generated at 2026-11-02 23:41:52.231918
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []
    
    # No even numbers
    assert module_0.pluck([1]) == []
    assert module_0.pluck([7, 3, 5]) == []
    assert module_0.pluck([3, 1, 5, 7]) == []
    
    # Single even number
    assert module_0.pluck([0]) == [0, 0]
    assert module_0.pluck([4]) == [4, 0]
    
    # Basic cases with multiple evens
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([2, 4, 6]) == [2, 0]
    assert module_0.pluck([0, 2, 4]) == [0, 0]
    
    # Duplicate smallest even values -> first index returned
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert module_0.pluck([1, 3, 5, 2, 2]) == [2, 3]
    
    # Negative even numbers
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]
    assert module_0.pluck([3, -2, -4]) == [-4, 2]
    
    # Mixed positive/negative/zero
    assert module_0.pluck([5, -1, 0, 6, 2]) == [0, 2]
    
    # All even numbers
    assert module_0.pluck([8, 6, 4, 2]) == [2, 3]
    
    print("All test_pluck tests passed!")


test_pluck()

# Generated at 2026-11-02 23:42:56.552194
# Unit test for function pluck
def test_pluck():# Test empty array
    assert module_0.pluck([]) == []
    
    # Test array with no even numbers
    assert module_0.pluck([1, 3, 5, 7]) == []
    
    # Test single even number
    assert module_0.pluck([2]) == [2, 0]
    
    # Test single odd number
    assert module_0.pluck([3]) == []
    
    # Test multiple evens with unique minimum
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3, 4, 5]) == [2, 1]
    
    # Test duplicate minimum evens (should return first occurrence index)
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert module_0.pluck([2, 4, 2, 6]) == [2, 0]
    
    # Test evens appearing later in array
    assert module_0.pluck([1, 3, 5, 6, 7]) == [6, 3]
    assert module_0.pluck([7, 6, 7, 6, 8]) == [6, 1]
    
    # Test negative even numbers
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]
    assert module_0.pluck([0, -2, 4]) == [-2, 1]
    
    # Test zero as minimum even
    assert module_0.pluck([0, 2, 4]) == [0, 0]
    assert module_0.pluck([3, 0, 5, 2]) == [0, 1]
    
    # Test all same even values
    assert module_0.pluck([4, 4, 4]) == [4, 0]
    
    # Test larger array
    assert module_0.pluck(list(range(1, 100))) == [2, 1]
    assert module_0.pluck(list(range(0, 50))) == [0, 0]

# Generated at 2026-11-02 23:44:49.099250
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert module_0.pluck([1, 2, 3, 0, 5, 3]) == [0, 3]
    assert module_0.pluck([5, 4, 8]) == [4, 1]
    assert module_0.pluck([7, 1, 5, 3, 9]) == []          # no even values
    assert module_0.pluck([2, 4, 6]) == [2, 0]            # smallest even at index 0
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([0]) == [0, 0]                  # single even element
    assert module_0.pluck([1]) == []                      # single odd element
    assert module_0.pluck([2, 2, 2]) == [2, 0]            # duplicates: first index
    assert module_0.pluck([-2, -4, 3]) == [-4, 1]         # negative even values
    assert module_0.pluck([1, 3, 5, 4]) == [4, 3]         # only one even value