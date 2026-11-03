

# Generated at 2026-11-03 00:42:53.058262
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Mixed positive and negative numbers
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-2, -4, -1, -3, -5, -7]) == (-1, None)
    assert module_0.largest_smallest_integers([-2, -4, 1, 3, 5, 7]) == (-2, 1)
    assert module_0.largest_smallest_integers([-1, 1]) == (-1, 1)

    # Empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # All zeros (neither positive nor negative)
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)

    # Single element cases
    assert module_0.largest_smallest_integers([5]) == (None, 5)
    assert module_0.largest_smallest_integers([-5]) == (-5, None)
    assert module_0.largest_smallest_integers([0]) == (None, None)

    # Duplicates
    assert module_0.largest_smallest_integers([3, 3, 3]) == (None, 3)
    assert module_0.largest_smallest_integers([-3, -3, -3]) == (-3, None)

    # Mixed with zeros
    assert module_0.largest_smallest_integers([0, -10, 10, 0]) == (-10, 10)

    # Multiple negatives and positives - should return closest to zero
    assert module_0.largest_smallest_integers([-100, -1, -50, 2, 200, 50]) == (-1, 2)

    # Order shouldn't matter
    assert module_0.largest_smallest_integers([7, 1, -3, -8]) == (-3, 1)

    print("All tests passed!")

test_largest_smallest_integers()

# Generated at 2026-11-03 00:44:30.223707
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Mixed positive and negative integers
    assert module_0.largest_smallest_integers([-2, -4, -6, 3]) == (-2, 3)
    assert module_0.largest_smallest_integers([-5, -1, -10, 2, 8, 3]) == (-1, 2)
    assert module_0.largest_smallest_integers([-1, 0, 1]) == (-1, 1)
    assert module_0.largest_smallest_integers([-100, 100]) == (-100, 100)

    # Only negative integers -> no smallest positive
    assert module_0.largest_smallest_integers([-1, -3, -5, -7]) == (-1, None)
    assert module_0.largest_smallest_integers([-42]) == (-42, None)

    # Only positive integers -> no largest negative
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([99]) == (None, 99)

    # Zeros are neither positive nor negative
    assert module_0.largest_smallest_integers([0]) == (None, None)
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)
    assert module_0.largest_smallest_integers([0, 5, -5]) == (-5, 5)

    # Empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # Duplicates
    assert module_0.largest_smallest_integers([-3, -3, 7, 7]) == (-3, 7)

    # Result types should match expected (int or None)
    result = module_0.largest_smallest_integers([-2, 3])
    assert isinstance(result, tuple) and len(result) == 2

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_smallest_integers()

# Generated at 2026-11-03 00:45:36.683409
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Mixed negative and positive integers
    assert module_0.largest_smallest_integers([-5, -3, 2, 4]) == (-3, 2)
    assert module_0.largest_smallest_integers([-10, -2, 7, 15]) == (-2, 7)
    assert module_0.largest_smallest_integers([-1, 1]) == (-1, 1)

    # Only negative integers -> largest negative, no positive
    assert module_0.largest_smallest_integers([-1, -3, -5, -7]) == (-1, None)
    assert module_0.largest_smallest_integers([-2, -4, -6]) == (-2, None)
    assert module_0.largest_smallest_integers([-1]) == (-1, None)

    # Only positive integers -> no negative, smallest positive
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([3, 1, 5]) == (None, 1)
    assert module_0.largest_smallest_integers([1]) == (None, 1)

    # Empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # Zero is neither positive nor negative
    assert module_0.largest_smallest_integers([0]) == (None, None)
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)
    assert module_0.largest_smallest_integers([0, -2, 3]) == (-2, 3)
    assert module_0.largest_smallest_integers([-1, 0, 1]) == (-1, 1)

    # Duplicates and extremes
    assert module_0.largest_smallest_integers([-3, -1, -1, 1, 3]) == (-1, 1)
    assert module_0.largest_smallest_integers([-100, -50, 50, 100]) == (-50, 50)
    assert module_0.largest_smallest_integers([-7, -7, -7]) == (-7, None)
    assert module_0.largest_smallest_integers([7, 7, 7]) == (None, 7)

    # Unsorted input order shouldn't matter
    assert module_0.largest_smallest_integers([4, -8, 2, -6, 9]) == (-6, 2)

    print("All tests passed!")


test_largest_smallest_integers()

# Generated at 2026-11-03 00:46:44.265981
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Both negative and positive integers present
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-2, -4, -1, -3, -5, -7]) == (-1, None)
    assert module_0.largest_smallest_integers([-2, -4, 1, 3, 5, 7]) == (-2, 1)
    assert module_0.largest_smallest_integers([-6, -4, -2, 4, 6, 8]) == (-2, 4)

    # Mixed with zero (zero is neither positive nor negative)
    assert module_0.largest_smallest_integers([0, -3, 5]) == (-3, 5)
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)

    # Only negative numbers
    assert module_0.largest_smallest_integers([-1, -2, -3]) == (-1, None)

    # Only positive numbers
    assert module_0.largest_smallest_integers([1, 2, 3]) == (None, 1)

    # Empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # Single element lists
    assert module_0.largest_smallest_integers([5]) == (None, 5)
    assert module_0.largest_smallest_integers([-5]) == (-5, None)
    assert module_0.largest_smallest_integers([0]) == (None, None)

    # Duplicates
    assert module_0.largest_smallest_integers([-3, -3, 2, 2]) == (-3, 2)
    assert module_0.largest_smallest_integers([-1, -1, -1]) == (-1, None)

    # Larger range values
    assert module_0.largest_smallest_integers([-100, -50, 50, 100]) == (-50, 50)
    assert module_0.largest_smallest_integers([-1, 1]) == (-1, 1)

    print("All tests passed!")


test_largest_smallest_integers()

# Generated at 2026-11-03 00:48:01.377192
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Mixed positive and negative integers
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-5, -3, -1, 2, 4]) == (-1, 2)
    assert module_0.largest_smallest_integers([-10, -20, -30]) == (-10, None)
    assert module_0.largest_smallest_integers([10, 20, 30]) == (None, 10)

    # Empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # List with only zeros
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)

    # Single element lists
    assert module_0.largest_smallest_integers([5]) == (None, 5)
    assert module_0.largest_smallest_integers([-5]) == (-5, None)
    assert module_0.largest_smallest_integers([0]) == (None, None)

    # Duplicates
    assert module_0.largest_smallest_integers([-1, -1, 1, 1]) == (-1, 1)
    assert module_0.largest_smallest_integers([-3, -3, 2, 2]) == (-3, 2)

    # Negative and positive with zero included
    assert module_0.largest_smallest_integers([0, -2, 3]) == (-2, 3)

    # Larger values
    assert module_0.largest_smallest_integers([-100, -50, 1000, 500]) == (-50, 500)

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_smallest_integers()