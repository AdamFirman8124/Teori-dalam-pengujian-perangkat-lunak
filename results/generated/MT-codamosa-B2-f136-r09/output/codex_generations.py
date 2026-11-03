

# Generated at 2026-11-02 19:16:29.095146
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Test with mixed positive and negative numbers
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-1, -3, -5, -7]) == (-1, None)
    assert module_0.largest_smallest_integers([-2, -4, 1, 3, 5]) == (-2, 1)

    # Test with typical mixed list
    assert module_0.largest_smallest_integers([-5, -3, 2, 8]) == (-3, 2)
    assert module_0.largest_smallest_integers([-10, -1, 100, 50]) == (-1, 50)

    # Test with only negatives
    assert module_0.largest_smallest_integers([-1, -2, -3]) == (-1, None)

    # Test with only positives
    assert module_0.largest_smallest_integers([1, 2, 3]) == (None, 1)

    # Test with empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # Test with zeros (neither positive nor negative)
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)
    assert module_0.largest_smallest_integers([0, -3, 0, 5]) == (-3, 5)

    # Test with single element
    assert module_0.largest_smallest_integers([7]) == (None, 7)
    assert module_0.largest_smallest_integers([-7]) == (-7, None)

    # Test with duplicates
    assert module_0.largest_smallest_integers([-2, -2, 3, 3]) == (-2, 3)

    # Test with large numbers
    assert module_0.largest_smallest_integers([-1000000, 1000000]) == (-1000000, 1000000)

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_smallest_integers()

# Generated at 2026-11-02 19:17:05.117361
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Mixed negative and positive integers
    assert module_0.largest_smallest_integers([2, -4, 1, -7, 5]) == (-4, 1)
    # Only negative integers
    assert module_0.largest_smallest_integers([-3, -1, -5]) == (-1, None)
    # Only positive integers
    assert module_0.largest_smallest_integers([3, 1, 5]) == (None, 1)
    # Empty list
    assert module_0.largest_smallest_integers([]) == (None, None)
    # List with zeros only (neither negative nor positive)
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)
    # Single negative element
    assert module_0.largest_smallest_integers([-5]) == (-5, None)
    # Single positive element
    assert module_0.largest_smallest_integers([5]) == (None, 5)
    # Zeros ignored, mixed values
    assert module_0.largest_smallest_integers([0, -2, 0, 3]) == (-2, 3)
    # Duplicates
    assert module_0.largest_smallest_integers([-1, -1, 2, 2]) == (-1, 2)
    print("All tests passed!")

# Run tests
test_largest_smallest_integers()

# Generated at 2026-11-02 19:18:02.549869
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Mixed positive and negative integers
    assert module_0.largest_smallest_integers([-1, 2, -4, 5, 6]) == (-1, 2)
    assert module_0.largest_smallest_integers([3, -2, 1, -5, 4]) == (-2, 1)

    # Only negatives -> largest negative, None for positive
    assert module_0.largest_smallest_integers([-1, -2, -3, -4]) == (-1, None)
    assert module_0.largest_smallest_integers([-10, -20, -30]) == (-10, None)

    # Only positives -> None for negative, smallest positive
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([10, 20, 30]) == (None, 10)

    # Empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # Zero is neither positive nor negative
    assert module_0.largest_smallest_integers([0]) == (None, None)
    assert module_0.largest_smallest_integers([0, 3, 5]) == (None, 3)
    assert module_0.largest_smallest_integers([0, -3, -5]) == (-3, None)
    assert module_0.largest_smallest_integers([0, -3, 5]) == (-3, 5)

    # Single element lists
    assert module_0.largest_smallest_integers([5]) == (None, 5)
    assert module_0.largest_smallest_integers([-5]) == (-5, None)

    # Duplicate values
    assert module_0.largest_smallest_integers([-2, -2, 3, 3]) == (-2, 3)

    print("All tests passed!")


test_largest_smallest_integers()

# Generated at 2026-11-02 19:19:00.949201
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Test with a typical list containing both negative and positive integers
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-5, -3, -1, -2, -4]) == (-1, None)
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7, 0, -2, -3]) == (-2, 1)
    assert module_0.largest_smallest_integers([1]) == (None, 1)
    assert module_0.largest_smallest_integers([-1]) == (-1, None)
    assert module_0.largest_smallest_integers([0]) == (None, None)
    assert module_0.largest_smallest_integers([]) == (None, None)
    assert module_0.largest_smallest_integers([-3, -2, -1, 1, 2, 3]) == (-1, 1)
    assert module_0.largest_smallest_integers([-10, -20, -30, 10, 20, 30]) == (-10, 10)
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)
    assert module_0.largest_smallest_integers([-1, -2, -3, 0]) == (-1, None)
    assert module_0.largest_smallest_integers([0, 1, 2, 3]) == (None, 1)
    assert module_0.largest_smallest_integers([-100, 100]) == (-100, 100)
    assert module_0.largest_smallest_integers([7, 3, 9, 2]) == (None, 2)
    assert module_0.largest_smallest_integers([-7, -3, -9, -2]) == (-2, None)
    print("All tests passed!")


test_largest_smallest_integers()

# Generated at 2026-11-02 19:19:33.344759
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Mixed negative and positive values
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-6, -4, -2, 2, 4, 6]) == (-2, 2)
    assert module_0.largest_smallest_integers([-1, 5, -3, 8, 0]) == (-1, 5)

    # Only negatives -> largest positive is None
    assert module_0.largest_smallest_integers([-1, -3, -5]) == (-1, None)
    assert module_0.largest_smallest_integers([-10, -20, -30]) == (-10, None)

    # Only positives -> smallest negative is None
    assert module_0.largest_smallest_integers([1, 3, 5]) == (None, 1)
    assert module_0.largest_smallest_integers([10, 20, 30]) == (None, 10)

    # Empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # Zero is neither negative nor positive
    assert module_0.largest_smallest_integers([0]) == (None, None)
    assert module_0.largest_smallest_integers([0, -1, 1]) == (-1, 1)

    # Single element lists
    assert module_0.largest_smallest_integers([-7]) == (-7, None)
    assert module_0.largest_smallest_integers([7]) == (None, 7)

    # Duplicates
    assert module_0.largest_smallest_integers([-2, -2, 3, 3]) == (-2, 3)

    print("All tests passed!")


test_largest_smallest_integers()