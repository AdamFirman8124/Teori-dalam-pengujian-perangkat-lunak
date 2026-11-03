

# Generated at 2026-11-01 21:37:39.034899
# Unit test for function pluck
def test_pluck():
    # Test with empty array
    assert module_0.pluck([]) == [], "Expected [] for empty array"

    # Test with array containing only odd numbers
    assert module_0.pluck([1, 3, 5, 7]) == [], "Expected [] when there are no even values"

    # Test typical cases
    assert module_0.pluck([4, 2, 3]) == [2, 1], "Should return smallest even value and its index"
    assert module_0.pluck([1, 2, 3]) == [2, 1], "Should return smallest even value and its index"
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1], "Should return first occurrence of smallest even value"

    # Test with single element arrays
    assert module_0.pluck([0]) == [0, 0], "Single even element at index 0"
    assert module_0.pluck([1]) == [], "Single odd element yields []"

    # Test where smallest even appears multiple times -> first index wins
    assert module_0.pluck([8, 2, 6, 2]) == [2, 1], "Duplicate minimums should return lowest index"

    # Test with negative even numbers
    assert module_0.pluck([-4, -2, 3]) == [-4, 0], "Negative evens handled correctly"

    # Test where all elements are the same even number
    assert module_0.pluck([6, 6, 6]) == [6, 0], "All identical evens should return first index"

    print("test_pluck passed!")


if __name__ == "__main__":
    test_pluck()

# Generated at 2026-11-01 21:38:25.522562
# Unit test for function pluck
def test_pluck():
    # Empty array
    assert module_0.pluck([]) == []
    
    # No even numbers
    assert module_0.pluck([1, 3, 5, 7]) == []
    
    # Single even number
    assert module_0.pluck([2]) == [2, 0]
    
    # Multiple evens, smallest is first
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    
    # Multiple evens, smallest appears later
    assert module_0.pluck([1, 5, 2, 3, 4]) == [2, 2]
    
    # Duplicate smallest even values - should return first index
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    
    # All even numbers
    assert module_0.pluck([2, 4, 6]) == [2, 0]
    
    # Negative even numbers
    assert module_0.pluck([-4, -2, 3, 6]) == [-4, 0]
    
    # Zero in array
    assert module_0.pluck([1, 0, 3, 7]) == [0, 1]
    
    # Larger array with mixed values
    assert module_0.pluck([7, 1, 5, 3, 8, 2, 9, 4]) == [2, 5]
    
    print("All pluck tests passed!")

test_pluck()

# Generated at 2026-11-01 21:39:12.217582
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

    # Smallest even value returned with its index
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3]) == [2, 1]

    # Tie on smallest value: return the smallest index
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert module_0.pluck([2, 4, 2]) == [2, 0]

    # All even numbers
    assert module_0.pluck([8, 6, 4, 2]) == [2, 3]

    # Negative even numbers
    assert module_0.pluck([-2, -4, 6]) == [-4, 1]

    # Zero counts as even
    assert module_0.pluck([7, 0, 4]) == [0, 1]

# Generated at 2026-11-01 21:40:14.070868
# Unit test for function pluck
def test_pluck():
    # Test with empty array
    assert module_0.pluck([]) == []

    # Test with no even numbers
    assert module_0.pluck([1, 3, 5]) == []

    # Test with single even number
    assert module_0.pluck([2]) == [2, 0]

    # Test with smallest even at beginning
    assert module_0.pluck([4, 6, 8]) == [4, 0]

    # Test with smallest even in middle
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

    # Test with duplicate minimum evens - returns first occurrence index
    assert module_0.pluck([2, 4, 2, 6]) == [2, 0]
    assert module_0.pluck([7, 6, 2, 2]) == [2, 2]

    # Test with negative even numbers
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]
    assert module_0.pluck([3, -2, 5, -4]) == [-4, 3]

    # Test with odd and even mix, odd value smaller than even min
    assert module_0.pluck([1, 2, 3]) == [2, 1]

    # Test with zero present
    assert module_0.pluck([9, 0, 7, 4]) == [0, 1]

    # Test with larger array
    assert module_0.pluck(list(range(10))) == [0, 0]

    print("All test_pluck tests passed!")


test_pluck()

# Generated at 2026-11-01 21:40:35.160150
# Unit test for function pluck
def test_pluck():
    # Test empty array
    assert module_0.pluck([]) == []

    # Test array with no even numbers
    assert module_0.pluck([1, 3, 5, 7]) == []

    # Test array with only even numbers
    assert module_0.pluck([2, 4, 6]) == [2, 0]

    # Test smallest even is not first
    assert module_0.pluck([4, 2, 3]) == [2, 1]

    # Test single element array with even number
    assert module_0.pluck([8]) == [8, 0]

    # Test single element array with odd number
    assert module_0.pluck([7]) == []

    # Test duplicate smallest even values (should return first index)
    assert module_0.pluck([4, 2, 2, 6]) == [2, 1]

    # Test with negative even numbers
    assert module_0.pluck([-4, -2, 3, 6]) == [-4, 0]

    # Test with negative and positive evens
    assert module_0.pluck([5, 0, 3, 0, 4, 2]) == [0, 1]

    # Test with mixed odd and even, smallest even in middle
    assert module_0.pluck([1, 3, 8, 5, 6, 2]) == [2, 5]

    # Test with zero as smallest even
    assert module_0.pluck([3, 0, 5]) == [0, 1]

    # Test all same even values
    assert module_0.pluck([6, 6, 6]) == [6, 0]

    # Test large even numbers
    assert module_0.pluck([100, 200, 300]) == [100, 0]

    # Test odd numbers interleaved with evens
    assert module_0.pluck([1, 2, 3, 4, 5, 6]) == [2, 1]

# Run the tests
if __name__ == "__main__":
    test_pluck()
    print("All tests passed!")