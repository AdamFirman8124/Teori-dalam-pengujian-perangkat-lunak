

# Generated at 2026-11-02 12:07:26.384520
# Unit test for function compare
def test_compare():
    # Test basic case with all differences
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Test exact matches (all zeros)
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # Test guess higher than game (absolute values)
    assert module_0.compare([5, 10, 15], [2, 14, 11]) == [3, 4, 4]

    # Test mixed positive and negative differences
    assert module_0.compare([3, 7, 1], [1, 5, 9]) == [2, 2, 8]

    # Test single element lists
    assert module_0.compare([5], [3]) == [2]
    assert module_0.compare([5], [5]) == [0]

    # Test empty lists
    assert module_0.compare([], []) == []

    # Test with zeros
    assert module_0.compare([0, 0], [0, 0]) == [0, 0]
    assert module_0.compare([0], [7]) == [7]

    # Test with larger values
    assert module_0.compare([1000, 2000], [1500, 2500]) == [500, 500]

    # Test symmetric property: module_0.compare(a, b) == module_0.compare(b, a)
    a, b = [1, 5, 9], [4, 2, 8]
    assert module_0.compare(a, b) == module_0.compare(b, a)

    # Test result length matches input length
    result = module_0.compare([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
    assert len(result) == 5
    assert result == [4, 2, 0, 2, 4]

    # Test that all returned values are non-negative
    result = module_0.compare([1, 10, 3], [9, 2, 8])
    assert all(v >= 0 for v in result)

    print("All tests passed!")


if __name__ == "__main__":
    test_compare()

# Generated at 2026-11-02 12:08:28.640110
# Unit test for function compare
def test_compare():
    # Test case 1: all guesses correct
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # Test case 2: all guesses wrong by same amount
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Test case 3: negative differences use absolute value
    assert module_0.compare([5, 1, 8], [2, 6, 3]) == [3, 5, 5]

    # Test case 4: mixed correct and incorrect
    assert module_0.compare([10, 20, 30, 40], [10, 25, 30, 35]) == [0, 5, 0, 5]

    # Test case 5: single element lists
    assert module_0.compare([7], [7]) == [0]
    assert module_0.compare([7], [3]) == [4]

    # Test case 6: empty lists
    assert module_0.compare([], []) == []

    # Test case 7: zero values
    assert module_0.compare([0, 0], [0, 1]) == [0, 1]

    print("All test cases passed!")

test_compare()

# Generated at 2026-11-02 12:10:17.091337
# Unit test for function compare
def test_compare():
    # Identical lists -> all zeros
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    
    # Different values -> absolute differences
    assert module_0.compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2]
    assert module_0.compare([5, 10, 15], [3, 13, 20]) == [2, 3, 5]
    
    # Single element
    assert module_0.compare([7], [7]) == [0]
    assert module_0.compare([0], [9]) == [9]
    
    # Negative numbers use absolute difference
    assert module_0.compare([0, 0], [5, -5]) == [5, 5]
    assert module_0.compare([-1, -2], [-4, 2]) == [3, 4]
    
    # Empty lists
    assert module_0.compare([], []) == []

# Generated at 2026-11-02 12:12:17.173051
# Unit test for function compare
def test_compare():
    # All guesses correct
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # Some guesses incorrect
    assert module_0.compare([1, 2, 3], [1, 3, 2]) == [0, 1, 1]

    # All guesses incorrect
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Negative numbers
    assert module_0.compare([-1, -2, -3], [-1, -2, -3]) == [0, 0, 0]
    assert module_0.compare([-1, 2, -3], [1, -2, 3]) == [2, 4, 6]

    # Empty lists
    assert module_0.compare([], []) == []

    # Single element lists
    assert module_0.compare([5], [5]) == [0]
    assert module_0.compare([5], [10]) == [5]

    # Mixed magnitudes
    assert module_0.compare([0, 10, 20], [10, 0, 30]) == [10, 10, 10]

    # Larger lists
    assert module_0.compare([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == [4, 2, 0, 2, 4]

    # Absolute value ordering (guess less than game)
    assert module_0.compare([10, 20], [5, 15]) == [5, 5]

# Generated at 2026-11-02 12:13:29.801498
# Unit test for function compare
def test_compare():
    # Basic case: exact matches and differences
    assert module_0.compare([1, 2, 3], [3, 2, 1]) == [2, 0, 2]
    assert module_0.compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    
    # All exact matches
    assert module_0.compare([5, 5, 5], [5, 5, 5]) == [0, 0, 0]
    
    # All different
    assert module_0.compare([1, 1, 1], [10, 20, 30]) == [9, 19, 29]
    
    # Negative numbers
    assert module_0.compare([-1, -5, -3], [1, 5, 3]) == [2, 10, 6]
    assert module_0.compare([-2, 4], [4, -2]) == [6, 6]
    
    # Single element lists
    assert module_0.compare([7], [7]) == [0]
    assert module_0.compare([0], [9]) == [9]
    
    # Empty lists
    assert module_0.compare([], []) == []
    
    # Zeros
    assert module_0.compare([0, 0], [0, 0]) == [0, 0]
    
    print("All tests passed!")

test_compare()