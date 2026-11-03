

# Generated at 2026-11-02 10:32:18.739161
# Unit test for function compare
def test_compare():
    # All guesses correct
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    # All guesses wrong by same amount
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
    # Mixed differences
    assert module_0.compare([1, 5, 2], [4, 1, 5]) == [3, 4, 3]
    # Zeros
    assert module_0.compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]
    # Single element
    assert module_0.compare([10], [3]) == [7]
    assert module_0.compare([5], [5]) == [0]
    # Empty lists
    assert module_0.compare([], []) == []
    # Longer lists
    assert module_0.compare([3, 1, 4, 1, 5], [9, 2, 6, 5, 3]) == [6, 1, 2, 4, 2]
    # Negative values
    assert module_0.compare([-1, -2], [-4, 0]) == [3, 2]
    print("test_compare passed")

test_compare()

# Generated at 2026-11-02 10:33:26.421981
# Unit test for function compare
def test_compare():
    # Basic case: all guesses differ
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
    # Exact matches: all differences zero
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    # Mixed matches and mismatches
    assert module_0.compare([1, 2, 3, 4], [1, 5, 3, 8]) == [0, 3, 0, 4]
    # Guesses lower than game values
    assert module_0.compare([5, 10, 15], [0, 0, 0]) == [5, 10, 15]
    # Symmetric: order of arguments doesn't matter
    assert module_0.compare([0, 0, 0], [5, 10, 15]) == [5, 10, 15]
    # Single element
    assert module_0.compare([1], [1]) == [0]
    assert module_0.compare([7], [3]) == [4]
    # Empty lists
    assert module_0.compare([], []) == []
    # Negative numbers
    assert module_0.compare([-1, -2, -3], [-3, -4, -5]) == [2, 2, 2]
    # Mixed signs
    assert module_0.compare([-5, 5], [5, -5]) == [10, 10]
    # Larger lists
    assert module_0.compare([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == [4, 2, 0, 2, 4]

# Generated at 2026-11-02 10:34:21.309088
# Unit test for function compare
def test_compare():
    # Test case 1: Some matches, some differences
    assert module_0.compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

    # Test case 2: All differences
    assert module_0.compare([0, 5, 0, 5, 0, 5], [5, 0, 5, 0, 5, 0]) == [5, 5, 5, 5, 5, 5]

    # Test case 3: Perfect match, all zeros
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # Test case 4: Empty lists
    assert module_0.compare([], []) == []

    # Test case 5: Single element lists
    assert module_0.compare([10], [4]) == [6]

    # Test case 6: Negative numbers
    assert module_0.compare([-5, -3, 0], [5, 3, 0]) == [10, 6, 0]

    # Test case 7: Mixed order of abs differences
    assert module_0.compare([7, 1, 9], [3, 6, 2]) == [4, 5, 7]

    print("All test cases passed!")

if __name__ == "__main__":
    test_compare()

# Generated at 2026-11-02 10:35:23.005135
# Unit test for function compare
def test_compare():
    # Test case 1: exact matches return all zeros
    assert module_0.compare([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [0, 0, 0, 0, 0]

    # Test case 2: mixed matches and differences (including negative guess)
    assert module_0.compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 1, 3]

    # Test case 3: all guesses wrong
    assert module_0.compare([0, 5, 10], [3, 0, 4]) == [3, 5, 6]

    # Test case 4: negative numbers in both lists
    assert module_0.compare([-1, -5, -3], [-1, -2, -7]) == [0, 3, 4]

    # Test case 5: single element lists
    assert module_0.compare([7], [2]) == [5]

    # Test case 6: empty lists
    assert module_0.compare([], []) == []

# Generated at 2026-11-02 10:36:01.766456
# Unit test for function compare
def test_compare():
    # Basic case: all guesses differ from game values
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Exact matches: all differences are zero
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # Guess values less than game values (absolute value handles negatives)
    assert module_0.compare([5, 10, 15], [3, 7, 20]) == [2, 3, 5]

    # Mixed greater/less than differences
    assert module_0.compare([10, 2, 8], [3, 9, 1]) == [7, 7, 7]

    # Single element lists
    assert module_0.compare([5], [5]) == [0]
    assert module_0.compare([5], [2]) == [3]

    # Empty lists
    assert module_0.compare([], []) == []

    # Larger lists with symmetric differences
    assert module_0.compare([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == [4, 2, 0, 2, 4]

    # Lists containing zeros
    assert module_0.compare([0, 0], [0, 3]) == [0, 3]

    print("All tests passed!")


test_compare()