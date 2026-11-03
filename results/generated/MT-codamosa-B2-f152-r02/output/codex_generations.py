

# Generated at 2026-11-02 11:14:39.409016
# Unit test for function compare
def test_compare():
    # Test case 1: All guesses correct (no differences)
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # Test case 2: All guesses wrong (constant difference)
    assert module_0.compare([1, 2, 3], [3, 4, 5]) == [2, 2, 2]

    # Test case 3: Mixed correct and incorrect guesses
    assert module_0.compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

    # Test case 4: Empty lists
    assert module_0.compare([], []) == []

    # Test case 5: Single element lists
    assert module_0.compare([5], [5]) == [0]
    assert module_0.compare([5], [10]) == [5]

    # Test case 6: Negative numbers
    assert module_0.compare([-1, -2, -3], [1, 2, 3]) == [2, 4, 6]

    # Test case 7: Zero values
    assert module_0.compare([0, 0], [0, 5]) == [0, 5]

    # Test case 8: Larger values
    assert module_0.compare([100, 200], [150, 100]) == [50, 100]

# Generated at 2026-11-02 11:17:15.262842
# Unit test for function compare
def test_compare():
    # Basic case: mixed correct and incorrect guesses
    assert module_0.compare([1, 2, 3, 4, 5], [0, 2, 4, 4, 5]) == [1, 0, 1, 0, 0]
    # All guesses exactly correct
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    # All guesses wrong
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
    # Absolute difference ignores sign of deviation
    assert module_0.compare([5, 3, 8], [2, 7, 1]) == [3, 4, 7]
    # Single element lists
    assert module_0.compare([10], [7]) == [3]
    # Empty lists
    assert module_0.compare([], []) == []
    # Negative numbers
    assert module_0.compare([-1, -5], [-3, -2]) == [2, 3]
    # Mixed positive and negative numbers
    assert module_0.compare([-1, 1], [1, -1]) == [2, 2]
    # Larger values
    assert module_0.compare([100, 200], [150, 150]) == [50, 50]
# nonce:d8befa3b

test_compare()
print("All tests passed!")

# Generated at 2026-11-02 11:18:58.894459
# Unit test for function compare
def test_compare():
    # Test with identical values - all differences should be 0
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    
    # Test with different values
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
    
    # Test with mixed differences
    assert module_0.compare([1, 2, 3, 4], [1, 3, 2, 4]) == [0, 1, 1, 0]
    
    # Test with negative numbers
    assert module_0.compare([-1, -2, -3], [-4, -5, -6]) == [3, 3, 3]
    assert module_0.compare([-1, 2, -3], [1, -2, 3]) == [2, 4, 6]
    
    # Test with zeros
    assert module_0.compare([0, 0], [0, 5]) == [0, 5]
    
    # Test with single element
    assert module_0.compare([5], [10]) == [5]
    
    # Test with empty lists
    assert module_0.compare([], []) == []
    
    # Test with floats
    assert module_0.compare([1.5, 2.5], [2.0, 2.0]) == [0.5, 0.5]
    
    # Test symmetric property (abs of difference)
    assert module_0.compare([7, 3], [3, 7]) == [4, 4]
    
    print("All test_compare tests passed!")


if __name__ == "__main__":
    test_compare()

# Generated at 2026-11-02 11:20:39.040354
# Unit test for function compare
def test_compare():
    # All guesses correct
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # All guesses incorrect by same amount
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Mixed differences
    assert module_0.compare([1, 5, 2, 8, 3], [2, 1, 4, 7, 9]) == [1, 4, 2, 1, 6]

    # Negative numbers
    assert module_0.compare([-1, -2, -3], [1, 2, 3]) == [2, 4, 6]

    # Empty lists
    assert module_0.compare([], []) == []

    # Single element lists
    assert module_0.compare([5], [5]) == [0]
    assert module_0.compare([5], [10]) == [5]

    # Differences in both directions
    assert module_0.compare([10, 20, 30], [5, 25, 30]) == [5, 5, 0]

# Generated at 2026-11-02 11:22:07.932557
# Unit test for function compare
def test_compare():
    # Test with typical positive integers
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # Test with single element lists
    assert module_0.compare([5], [10]) == [5]

    # Test with negative numbers
    assert module_0.compare([-1, -2, -3], [-4, -5, -6]) == [3, 3, 3]
    assert module_0.compare([-1, 2, -3], [4, -5, 6]) == [5, 7, 9]

    # Test with mixed positive and negative
    assert module_0.compare([10, -10], [-10, 10]) == [20, 20]

    # Test with zeros
    assert module_0.compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]
    assert module_0.compare([0], [5]) == [5]

    # Test with empty lists
    assert module_0.compare([], []) == []

    # Test with larger differences
    assert module_0.compare([100, 200], [1, 2]) == [99, 198]

    # Test result type and length
    result = module_0.compare([1, 2], [3, 4])
    assert isinstance(result, list)
    assert len(result) == 2

    # Test all elements are non-negative
    result = module_0.compare([1, 5, 10], [10, 1, 5])
    assert all(x >= 0 for x in result)
    assert result == [9, 4, 5]