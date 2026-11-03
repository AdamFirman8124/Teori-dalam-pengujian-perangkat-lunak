

# Generated at 2026-11-02 15:15:11.611826
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Mixed positive and negative integers
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-5, -3, -1, 2, 4]) == (-1, 2)

    # Only negative integers
    assert module_0.largest_smallest_integers([-1, -2, -3]) == (-1, None)

    # Only positive integers
    assert module_0.largest_smallest_integers([1, 2, 3]) == (None, 1)

    # Empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # List with only zeros
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)

    # Single negative element
    assert module_0.largest_smallest_integers([-7]) == (-7, None)

    # Single positive element
    assert module_0.largest_smallest_integers([7]) == (None, 7)

    # Duplicates
    assert module_0.largest_smallest_integers([-3, -3, 5, 5]) == (-3, 5)

    # Unsorted input
    assert module_0.largest_smallest_integers([10, -100, 3, -5, 8]) == (-5, 3)

    # Zeros mixed with positives and negatives (zero ignored)
    assert module_0.largest_smallest_integers([0, -2, 4]) == (-2, 4)

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_smallest_integers()

# Generated at 2026-11-02 15:19:07.208171
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)

# Generated at 2026-11-02 15:21:54.477895
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Mixed positive and negative integers
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-5, -3, -1, 2, 4]) == (-1, 2)
    assert module_0.largest_smallest_integers([-10, -20, 10, 20]) == (-10, 10)

    # Only negative integers
    assert module_0.largest_smallest_integers([-1, -2, -3]) == (-1, None)
    assert module_0.largest_smallest_integers([-5]) == (-5, None)

    # Only positive integers
    assert module_0.largest_smallest_integers([1, 2, 3]) == (None, 1)
    assert module_0.largest_smallest_integers([7]) == (None, 7)

    # Empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # List containing only zero (zero is neither negative nor positive)
    assert module_0.largest_smallest_integers([0]) == (None, None)
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)

    # Zero mixed with negatives and positives
    assert module_0.largest_smallest_integers([0, -3, 5]) == (-3, 5)
    assert module_0.largest_smallest_integers([0, -1]) == (-1, None)
    assert module_0.largest_smallest_integers([0, 1]) == (None, 1)

    # Duplicates
    assert module_0.largest_smallest_integers([-2, -2, 3, 3]) == (-2, 3)
    assert module_0.largest_smallest_integers([-1, 1]) == (-1, 1)

    # Single element lists
    assert module_0.largest_smallest_integers([-100]) == (-100, None)
    assert module_0.largest_smallest_integers([100]) == (None, 100)

    # Negative and positive extremes
    assert module_0.largest_smallest_integers([-1000, 1000]) == (-1000, 1000)

    # Unsorted input
    assert module_0.largest_smallest_integers([5, -3, 8, -1, 2, -7]) == (-1, 2)