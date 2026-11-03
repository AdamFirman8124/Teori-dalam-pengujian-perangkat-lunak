

# Generated at 2026-11-03 03:46:31.915366
# Unit test for function compare
def test_compare():
    # Typical case: guesses differ from game scores
    assert module_0.compare([1, 2, 3, 4, 5, 1], [1, 1, 1, 1, 1, 1]) == [0, 1, 2, 3, 4, 0]
    # All guesses are zero
    assert module_0.compare([1, 2, 3, 4, 5, 1], [0, 0, 0, 0, 0, 0]) == [1, 2, 3, 4, 5, 1]
    # Mixed exact and off-by-one guesses
    assert module_0.compare([1, 2, 3, 4, 5, 1], [2, 2, 2, 2, 2, 2]) == [1, 0, 1, 2, 3, 1]
    # Perfect match
    assert module_0.compare([5, 5, 5], [5, 5, 5]) == [0, 0, 0]
    # Empty lists
    assert module_0.compare([], []) == []
    # Single element lists
    assert module_0.compare([0], [0]) == [0]
    assert module_0.compare([10], [0]) == [10]
    # Negative numbers
    assert module_0.compare([-1, -2], [1, 2]) == [2, 4]
    # Order of subtraction doesn't matter (absolute value)
    assert module_0.compare([3, 7], [7, 3]) == [4, 4]
    print("All tests passed!")

test_compare()

# Generated at 2026-11-03 03:47:34.774169
# Unit test for function compare
def test_compare():
    # nonce:ab0f5288
    assert module_0.compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert module_0.compare([0, 5, 0, 5, 0, 5], [0, 5, 0, 5, 0, 5]) == [0, 0, 0, 0, 0, 0]
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
    assert module_0.compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]
    assert module_0.compare([10], [3]) == [7]
    assert module_0.compare([-1, -2], [-4, -5]) == [3, 3]

# Generated at 2026-11-03 03:49:44.925723
# Unit test for function compare
def test_compare():
    # Test with identical lists
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # Test with different lists
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Test with mixed differences
    assert module_0.compare([1, 5, 3], [4, 2, 3]) == [3, 3, 0]

    # Test with empty lists
    assert module_0.compare([], []) == []

    # Test with negative numbers
    assert module_0.compare([-1, -2, -3], [-4, -5, -6]) == [3, 3, 3]

    # Test with mixed positive and negative numbers
    assert module_0.compare([-1, 2, -3], [1, -2, 3]) == [2, 4, 6]

    # Test with single element lists
    assert module_0.compare([0], [0]) == [0]
    assert module_0.compare([0], [10]) == [10]

    # Test with larger lists
    assert module_0.compare([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == [4, 2, 0, 2, 4]

    # Test with zeros
    assert module_0.compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]

    # Test with floats
    assert module_0.compare([1.5, 2.5], [1.0, 3.0]) == [0.5, 0.5]

    print("All tests passed!")

test_compare()

# Generated at 2026-11-03 03:51:36.441360
# Unit test for function compare
def test_compare():
    # All guesses exactly correct
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

    # All guesses wrong with same difference
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]

    # Mixed differences including negative guess values
    assert module_0.compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]

    # Negative numbers in both lists
    assert module_0.compare([-1, -2, -3], [-4, -5, -6]) == [3, 3, 3]

    # Single element lists
    assert module_0.compare([0], [5]) == [5]
    assert module_0.compare([5], [0]) == [5]

    # Empty lists
    assert module_0.compare([], []) == []

    # Float values
    assert module_0.compare([1.5, 2.5], [2.0, 1.0]) == [0.5, 1.5]

    # Order of arguments does not affect absolute difference
    assert module_0.compare([10, 20], [1, 2]) == module_0.compare([1, 2], [10, 20])

    print("All tests passed!")

# Generated at 2026-11-03 03:54:12.091947
# Unit test for function compare
def test_compare():
    assert module_0.compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]
    assert module_0.compare([1, 2, 3], [4, 5, 6]) == [3, 3, 3]
    assert module_0.compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]
    assert module_0.compare([-1, -2, -3], [1, 2, 3]) == [2, 4, 6]
    assert module_0.compare([10, 20, 30], [30, 20, 10]) == [20, 0, 20]
    assert module_0.compare([5], [3]) == [2]
    assert module_0.compare([], []) == []
    assert module_0.compare([2, 4, 6], [1, 2, 3]) == [1, 2, 3]