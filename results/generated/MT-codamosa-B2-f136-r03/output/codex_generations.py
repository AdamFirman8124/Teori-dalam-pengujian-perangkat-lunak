

# Generated at 2026-11-02 14:36:51.074016
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Mixed list with both negative and positive integers
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-6, -4, -2, -1]) == (-1, None)
    assert module_0.largest_smallest_integers([-6, -4, -2, 1, 3, 5]) == (-2, 1)
    assert module_0.largest_smallest_integers([1, 2, 3, -1, -2, -3]) == (-1, 1)
    assert module_0.largest_smallest_integers([-3, -2, -1, 1, 2, 3]) == (-1, 1)

    # List with only positive integers
    assert module_0.largest_smallest_integers([5, 3, 8, 1]) == (None, 1)

    # List with only negative integers
    assert module_0.largest_smallest_integers([-5, -3, -8, -1]) == (-1, None)

    # Empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # List containing only zero
    assert module_0.largest_smallest_integers([0]) == (None, None)
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)

    # List containing zero along with negatives and positives
    assert module_0.largest_smallest_integers([-1, 0, 1]) == (-1, 1)

    # Single-element lists
    assert module_0.largest_smallest_integers([7]) == (None, 7)
    assert module_0.largest_smallest_integers([-7]) == (-7, None)

    # Duplicates
    assert module_0.largest_smallest_integers([-2, -2, 2, 2]) == (-2, 2)
    assert module_0.largest_smallest_integers([-10, -5, 5, 10]) == (-5, 5)

# Generated at 2026-11-02 14:37:50.042057
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Test with mixed positive and negative integers
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-5, -3, -1, 2, 4]) == (-1, 2)
    assert module_0.largest_smallest_integers([-10, -20, -30, 10, 20, 30]) == (-10, 10)

    # Test with only negative integers
    assert module_0.largest_smallest_integers([-1, -2, -3]) == (-1, None)
    assert module_0.largest_smallest_integers([-100]) == (-100, None)

    # Test with only positive integers
    assert module_0.largest_smallest_integers([1, 2, 3]) == (None, 1)
    assert module_0.largest_smallest_integers([100]) == (None, 100)

    # Test with empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # Test with zero only (zero is neither negative nor positive)
    assert module_0.largest_smallest_integers([0]) == (None, None)
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)

    # Test with zero mixed in
    assert module_0.largest_smallest_integers([-1, 0, 1]) == (-1, 1)
    assert module_0.largest_smallest_integers([0, -5]) == (-5, None)
    assert module_0.largest_smallest_integers([0, 5]) == (None, 5)

    # Test with duplicates
    assert module_0.largest_smallest_integers([-2, -2, 2, 2]) == (-2, 2)
    assert module_0.largest_smallest_integers([3, 3, 3]) == (None, 3)

    # Test with single elements
    assert module_0.largest_smallest_integers([-7]) == (-7, None)
    assert module_0.largest_smallest_integers([7]) == (None, 7)

    # Test with extreme values
    assert module_0.largest_smallest_integers([float('inf')]) == (None, float('inf'))
    assert module_0.largest_smallest_integers([float('-inf')]) == (float('-inf'), None)

    # Test unsorted input
    assert module_0.largest_smallest_integers([5, -3, 8, -1, 2]) == (-1, 2)

    print("All tests passed!")


test_largest_smallest_integers()

# Generated at 2026-11-02 14:40:18.761306
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Mixed positive and negative numbers
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-1, -3, -5, -7]) == (-1, None)
    assert module_0.largest_smallest_integers([2, -4, 1, -3, 5, -7]) == (-3, 1)

    # Contains zero (zero is neither positive nor negative)
    assert module_0.largest_smallest_integers([0]) == (None, None)
    assert module_0.largest_smallest_integers([-2, 0, 3]) == (-2, 3)

    # Empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # Only negatives
    assert module_0.largest_smallest_integers([-10, -20, -3]) == (-3, None)

    # Only positives
    assert module_0.largest_smallest_integers([10, 20, 3]) == (None, 3)

    # Duplicates
    assert module_0.largest_smallest_integers([-1, -1, 2, 2]) == (-1, 2)

    # Single element
    assert module_0.largest_smallest_integers([-5]) == (-5, None)
    assert module_0.largest_smallest_integers([5]) == (None, 5)

    # Large values
    assert module_0.largest_smallest_integers([-1000000, 1000000]) == (-1000000, 1000000)

    print("All tests passed!")

# Generated at 2026-11-02 14:41:58.878575
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Test with both negative and positive integers
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-5, -3, -1, 2, 4, 6]) == (-1, 2)
    assert module_0.largest_smallest_integers([-10, -20, -30, 10, 20, 30]) == (-10, 10)

    # Test with only negative integers
    assert module_0.largest_smallest_integers([-1, -2, -3]) == (-1, None)
    assert module_0.largest_smallest_integers([-5]) == (-5, None)

    # Test with only positive integers
    assert module_0.largest_smallest_integers([1, 2, 3]) == (None, 1)
    assert module_0.largest_smallest_integers([5]) == (None, 5)

    # Test with empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # Test with list containing zero (zero is neither negative nor positive)
    assert module_0.largest_smallest_integers([0]) == (None, None)
    assert module_0.largest_smallest_integers([0, -1, 1]) == (-1, 1)
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)

    # Test with unsorted input
    assert module_0.largest_smallest_integers([3, -7, 1, -2, 5, -9]) == (-2, 1)

    # Test with duplicate values
    assert module_0.largest_smallest_integers([-3, -3, 4, 4]) == (-3, 4)

    # Test with single negative and single positive
    assert module_0.largest_smallest_integers([-1, 1]) == (-1, 1)

    # Test with large values
    assert module_0.largest_smallest_integers([-1000000, 1000000]) == (-1000000, 1000000)

    print("All tests passed!")


# Run the tests
test_largest_smallest_integers()

# Generated at 2026-11-02 14:44:47.456364
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Mixed positive and negative numbers
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-5, -3, -1, 2, 4]) == (-1, 2)
    assert module_0.largest_smallest_integers([-10, -20, 30, 40]) == (-10, 30)

    # Only negative numbers
    assert module_0.largest_smallest_integers([-1, -2, -3]) == (-1, None)
    assert module_0.largest_smallest_integers([-7]) == (-7, None)

    # Only positive numbers
    assert module_0.largest_smallest_integers([1, 2, 3]) == (None, 1)
    assert module_0.largest_smallest_integers([9]) == (None, 9)

    # Empty list
    assert module_0.largest_smallest_integers([]) == (None, None)

    # List with only zeros (zeros are neither positive nor negative)
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)
    assert module_0.largest_smallest_integers([0]) == (None, None)

    # Mixed with zeros
    assert module_0.largest_smallest_integers([-4, 0, 6]) == (-4, 6)
    assert module_0.largest_smallest_integers([0, -1]) == (-1, None)
    assert module_0.largest_smallest_integers([0, 1]) == (None, 1)

    # Duplicates
    assert module_0.largest_smallest_integers([-2, -2, 3, 3]) == (-2, 3)
    assert module_0.largest_smallest_integers([5, 5, 5]) == (None, 5)

    # Negative closest to zero is returned as smallest
    assert module_0.largest_smallest_integers([-100, -1, 100, 1]) == (-1, 1)

    # Single element lists
    assert module_0.largest_smallest_integers([-3]) == (-3, None)
    assert module_0.largest_smallest_integers([3]) == (None, 3)

    print("All tests passed!")


if __name__ == "__main__":
    test_largest_smallest_integers()