

# Generated at 2026-11-02 23:04:05.310187
# Unit test for function compare
def test_compare():
    # Test case: exact matches, all differences should be 0
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # Test case: all guesses wrong
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Test case: mixed correct and incorrect guesses
    assert module_0.compare([1, 2, 3, 4], [1, 5, 3, 7]) == [0, 3, 0, 3]

    # Test case: absolute value handles reversed differences
    assert module_0.compare([5, 3, 8], [2, 7, 1]) == [3, 4, 7]

    # Test case: single element lists
    assert module_0.compare([10], [3]) == [7]

    # Test case: negative numbers
    assert module_0.compare([-1, -2, -3], [1, 2, 3]) == [2, 4, 6]
    assert module_0.compare([-5, -5], [-5, -1]) == [0, 4]

    # Test case: empty lists
    assert module_0.compare([], []) == []

    # Test case: lists of different lengths (zip truncates to shortest)
    assert module_0.compare([1, 2, 3], [1, 2]) == [0, 0]
    assert module_0.compare([1], [1, 2, 3]) == [0]

    # Test case: zeros
    assert module_0.compare([0, 0], [0, 5]) == [0, 5]

    # Test case: large numbers
    assert module_0.compare([1000000, 999999], [1000000, 0]) == [0, 999999]

    print("All test cases passed!")

test_compare()

# Generated at 2026-11-02 23:06:17.752693
# Unit test for function compare
def test_compare():
    # Exact matches -> all zeros
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # All guesses wrong by 1
    assert module_0.compare([1, 2, 3], [2, 3, 4]) == [1, 1, 1]

    # Mixed differences
    assert module_0.compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

    # Absolute value handles guess > game and game > guess
    assert module_0.compare([5, 5, 5], [3, 7, 5]) == [2, 2, 0]

    # Single element
    assert module_0.compare([0], [5]) == [5]

    # Empty lists
    assert module_0.compare([], []) == []

    # Negative numbers
    assert module_0.compare([-1, -2, -3], [-1, -4, 0]) == [0, 2, 3]

    # Larger lists
    assert module_0.compare([10, 20, 30, 40], [15, 25, 30, 35]) == [5, 5, 0, 5]

    print("All test cases passed!")


if __name__ == "__main__":
    test_compare()

# Generated at 2026-11-02 23:09:15.909252
# Unit test for function compare
def test_compare():
    # Basic case with differences
    assert module_0.compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    # All guesses correct
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    # Negative numbers involved
    assert module_0.compare([0, 5, 0, 0, 0, 5], [0, 0, 0, 0, 0, -1]) == [0, 5, 0, 0, 0, 6]
    # Single element lists
    assert module_0.compare([7], [3]) == [4]
    # Empty lists
    assert module_0.compare([], []) == []
    # All wrong guesses
    assert module_0.compare([10, 20], [0, 0]) == [10, 20]
    # Absolute value handles reversed order
    assert module_0.compare([1, 2], [5, 8]) == [4, 6]
    print("All test cases passed!")

test_compare()

# Generated at 2026-11-02 23:11:19.961305
# Unit test for function compare
def test_compare():
    # Test with exact matches (all differences should be 0)
    assert module_0.compare([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == [0, 0, 0, 0, 0]

    # Test with all wrong guesses
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Test with mixed matches
    assert module_0.compare([1, 2, 3, 4], [1, 5, 3, 7]) == [0, 3, 0, 3]

    # Test with empty lists
    assert module_0.compare([], []) == []

    # Test with single element lists
    assert module_0.compare([5], [3]) == [2]
    assert module_0.compare([5], [5]) == [0]

    # Test with negative numbers
    assert module_0.compare([-1, -2, -3], [-1, -5, -3]) == [0, 3, 0]
    assert module_0.compare([-1, 2, -3], [1, -2, 3]) == [2, 4, 6]

    # Test with large numbers
    assert module_0.compare([1000000, 2000000], [999999, 2000002]) == [1, 2]

    # Test with zeros
    assert module_0.compare([0, 0, 0], [0, 1, 0]) == [0, 1, 0]

    # Test that result is absolute value (guess greater than game)
    assert module_0.compare([1, 1, 1], [10, 10, 10]) == [9, 9, 9]

    # Test that result is absolute value (game greater than guess)
    assert module_0.compare([10, 10, 10], [1, 1, 1]) == [9, 9, 9]

    # Test with floats
    assert module_0.compare([1.5, 2.5], [1.0, 3.0]) == [0.5, 0.5]

    # Test result is a list
    assert isinstance(module_0.compare([1, 2], [3, 4]), list)

    # Test result length matches input length
    assert len(module_0.compare([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])) == 5

    print("All test cases passed!")

if __name__ == "__main__":
    test_compare()