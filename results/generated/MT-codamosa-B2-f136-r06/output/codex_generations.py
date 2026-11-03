

# Generated at 2026-11-02 11:24:50.738926
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Test with both negative and positive integers
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-5, -3, -1, 2, 4]) == (-1, 2)
    assert module_0.largest_smallest_integers([-10, -20, 10, 20]) == (-10, 10)

    # Test with only negative integers
    assert module_0.largest_smallest_integers([-1, -2, -3]) == (-1, None)

    # Test with only positive integers
    assert module_0.largest_smallest_integers([1, 2, 3]) == (None, 1)

    # Test with empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # Test with list containing only zeros
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)

    # Test with single element lists
    assert module_0.largest_smallest_integers([5]) == (None, 5)
    assert module_0.largest_smallest_integers([-5]) == (-5, None)
    assert module_0.largest_smallest_integers([0]) == (None, None)

    # Test with mixed values including zero
    assert module_0.largest_smallest_integers([-3, 0, 3]) == (-3, 3)

    # Test with duplicates
    assert module_0.largest_smallest_integers([-2, -2, 4, 4]) == (-2, 4)

    # Test with large numbers
    assert module_0.largest_smallest_integers([-1000000, 1000000]) == (-1000000, 1000000)

    # Test verifying closest-to-zero semantics
    assert module_0.largest_smallest_integers([-5, -4, -3, 3, 4, 5]) == (-3, 3)

    print("All tests passed!")

# Generated at 2026-11-02 11:27:00.390279
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Both negative and positive numbers present
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-6, -4, -2, -8]) == (-2, None)
    assert module_0.largest_smallest_integers([-6, -4, -1, 3, 5, 7]) == (-1, 3)
    assert module_0.largest_smallest_integers([-6, -4, -1, 1, 5, 7]) == (-1, 1)

    # Empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # Only negatives
    assert module_0.largest_smallest_integers([-3, -1, -7]) == (-1, None)

    # Only positives
    assert module_0.largest_smallest_integers([3, 1, 7]) == (None, 1)

    # Zero only (zero is neither negative nor positive)
    assert module_0.largest_smallest_integers([0]) == (None, None)
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)

    # Mixed with zero
    assert module_0.largest_smallest_integers([-5, 0, 5]) == (-5, 5)

    # Single elements
    assert module_0.largest_smallest_integers([-1]) == (-1, None)
    assert module_0.largest_smallest_integers([1]) == (None, 1)

    # Duplicates
    assert module_0.largest_smallest_integers([-2, -2, 3, 3]) == (-2, 3)
    assert module_0.largest_smallest_integers([-10, -2, 2, 10]) == (-2, 2)

    # Negative numbers closer to zero win (max of negatives)
    assert module_0.largest_smallest_integers([-100, -1, 100, 1]) == (-1, 1)

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_smallest_integers()

# Generated at 2026-11-02 11:29:26.943398
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Test with both negative and positive integers
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-5, -3, -1, 2, 4]) == (-1, 2)

    # Test with only negative integers
    assert module_0.largest_smallest_integers([-10, -20, -30]) == (-10, None)

    # Test with only positive integers
    assert module_0.largest_smallest_integers([10, 20, 30]) == (None, 10)

    # Test with empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # Test with zero (zero is neither negative nor positive)
    assert module_0.largest_smallest_integers([0]) == (None, None)
    assert module_0.largest_smallest_integers([0, -1, 1]) == (-1, 1)

    # Test with single element
    assert module_0.largest_smallest_integers([-7]) == (-7, None)
    assert module_0.largest_smallest_integers([7]) == (None, 7)

    # Test with mixed values and duplicates
    assert module_0.largest_smallest_integers([-2, -2, 3, 3]) == (-2, 3)

    # Test with negative and positive mixed, checking largest negative
    # (closest to zero) and smallest positive (closest to zero)
    assert module_0.largest_smallest_integers([-100, -1, -50, 100, 1, 50]) == (-1, 1)

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_smallest_integers()