

# Generated at 2026-11-02 17:30:17.961772
# Unit test for function is_sorted
def test_is_sorted():
    # Sorted list with unique elements
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True
    # Sorted list with an element appearing twice
    assert module_0.is_sorted([1, 2, 2, 3, 4]) == True
    # Sorted list with an element appearing three times
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    # Unsorted list
    assert module_0.is_sorted([5, 3, 1, 2]) == False
    # Unsorted list with duplicates
    assert module_0.is_sorted([1, 3, 2, 2]) == False
    # Empty list is sorted
    assert module_0.is_sorted([]) == True
    # Single element list
    assert module_0.is_sorted([7]) == True
    # Two equal elements
    assert module_0.is_sorted([4, 4]) == True
    # Three equal elements (exceeds duplicate limit)
    assert module_0.is_sorted([4, 4, 4]) == False
    # Non-decreasing with multiple pairs of duplicates
    assert module_0.is_sorted([1, 1, 2, 2, 3]) == True
    # Negative numbers sorted
    assert module_0.is_sorted([-3, -2, -1, 0]) == True
    # Negative numbers unsorted
    assert module_0.is_sorted([-1, -3, -2]) == False
    # Descending list
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False
    # Duplicates elsewhere but list unsorted
    assert module_0.is_sorted([2, 2, 1]) == False
    # Large sorted list with max two duplicates each
    assert module_0.is_sorted([1, 1, 2, 2, 3, 3, 4, 4]) == True
    # One element repeated three times breaks rule even at end
    assert module_0.is_sorted([1, 2, 3, 3, 3]) == False

    print("All tests passed!")


test_is_sorted()

# Generated at 2026-11-02 17:31:42.005267
# Unit test for function is_sorted
def test_is_sorted():
    # Sorted list with unique elements
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True
    # Sorted list with elements appearing at most twice
    assert module_0.is_sorted([1, 2, 2, 3, 3, 4]) == True
    # Sorted list but an element appears more than twice
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    # Unsorted list
    assert module_0.is_sorted([1, 3, 2, 4, 5]) == False
    # Descending list
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False
    # Empty list is considered sorted
    assert module_0.is_sorted([]) == True
    # Single element list
    assert module_0.is_sorted([1]) == True
    # Duplicate appearing exactly twice, still sorted
    assert module_0.is_sorted([1, 1]) == True
    # Same element appearing three times
    assert module_0.is_sorted([1, 1, 1]) == False
    # Sorted with mixed duplicates at limit
    assert module_0.is_sorted([1, 1, 2, 2, 3, 3]) == True
    # Sorted but duplicates exceed limit at the end
    assert module_0.is_sorted([1, 2, 3, 3, 3]) == False
    # Negative numbers sorted
    assert module_0.is_sorted([-3, -2, -1, 0, 1]) == True
    # Not sorted due to one out-of-place element
    assert module_0.is_sorted([1, 2, 5, 3, 4]) == False

# Generated at 2026-11-02 17:33:05.303712
# Unit test for function is_sorted
def test_is_sorted():
    # nonce:5a167ea1
    # Sorted lists with no duplicates
    assert module_0.is_sorted([1, 2, 3, 4]) == True
    assert module_0.is_sorted([5]) == True
    assert module_0.is_sorted([]) == True

    # Sorted lists with at most one duplicate of each element
    assert module_0.is_sorted([1, 2, 2, 3, 4]) == True
    assert module_0.is_sorted([1, 1, 2, 3, 4]) == True
    assert module_0.is_sorted([1, 2, 3, 4, 4]) == True
    assert module_0.is_sorted([1, 1, 2, 2, 3, 3]) == True

    # Sorted but with an element appearing more than twice
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    assert module_0.is_sorted([1, 1, 1]) == False
    assert module_0.is_sorted([2, 2, 2, 3, 4]) == False

    # Not sorted
    assert module_0.is_sorted([1, 3, 2, 4]) == False
    assert module_0.is_sorted([2, 1]) == False
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False

    # Not sorted and duplicate constraint violated
    assert module_0.is_sorted([1, 2, 2, 1]) == False

    # Negative numbers
    assert module_0.is_sorted([-3, -2, -1, 0]) == True
    assert module_0.is_sorted([-1, -1, -2]) == False

    print("All tests passed!")


test_is_sorted()

# Generated at 2026-11-02 17:34:25.709236
# Unit test for function is_sorted
def test_is_sorted():
    # nonce:120d3d59
    # Sorted lists with at most 2 duplicates of any number
    assert module_0.is_sorted([1, 2, 3, 4]) == True
    assert module_0.is_sorted([1, 2, 2, 3]) == True
    assert module_0.is_sorted([1, 1]) == True
    assert module_0.is_sorted([0, 0, 1, 1, 2]) == True
    assert module_0.is_sorted([5]) == True
    assert module_0.is_sorted([]) == True
    assert module_0.is_sorted([-2, -1, 0, 1, 2]) == True

    # More than 2 duplicates of any number -> False
    assert module_0.is_sorted([1, 1, 1]) == False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    assert module_0.is_sorted([3, 3, 3, 3]) == False
    assert module_0.is_sorted([1, 1, 2, 2, 2]) == False
    assert module_0.is_sorted([100, 100, 100]) == False

    # Not sorted -> False
    assert module_0.is_sorted([2, 1]) == False
    assert module_0.is_sorted([1, 3, 2]) == False
    assert module_0.is_sorted([1, 2, 3, 2]) == False
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False
    assert module_0.is_sorted([1, 2, 2, 2, 1]) == False
    assert module_0.is_sorted([1, 1, 1, 2]) == False

    # Edge cases
    assert module_0.is_sorted([0]) == True
    assert module_0.is_sorted([100, 100]) == True
    assert module_0.is_sorted([7, 7, 8, 8, 9]) == True

    print("All tests passed!")


if __name__ == "__main__":
    test_is_sorted()

# Generated at 2026-11-02 17:35:50.679750
# Unit test for function is_sorted
def test_is_sorted():
    # Sorted lists with no element appearing more than twice
    assert module_0.is_sorted([1, 2, 3]) == True
    assert module_0.is_sorted([1, 2, 2, 3]) == True
    assert module_0.is_sorted([1, 1, 2]) == True
    assert module_0.is_sorted([5]) == True
    assert module_0.is_sorted([]) == True
    assert module_0.is_sorted([1, 1]) == True

    # Sorted but an element appears more than twice
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    assert module_0.is_sorted([1, 1, 1]) == False
    assert module_0.is_sorted([2, 2, 2, 3, 4]) == False

    # Not sorted
    assert module_0.is_sorted([3, 2, 1]) == False
    assert module_0.is_sorted([1, 3, 2]) == False
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False
    assert module_0.is_sorted([2, 1]) == False

    # Duplicates plus unsorted
    assert module_0.is_sorted([1, 2, 2, 1]) == False

    # Negative numbers and mixed values
    assert module_0.is_sorted([-3, -2, -1, 0]) == True
    assert module_0.is_sorted([-1, -1, 0, 1]) == True
    assert module_0.is_sorted([-1, -1, -1, 0]) == False
    assert module_0.is_sorted([0, -1, 1]) == False

    # Non-integer values (works with comparables)
    assert module_0.is_sorted(['a', 'b', 'c']) == True
    assert module_0.is_sorted(['b', 'a']) == False
    assert module_0.is_sorted([1.5, 2.5, 2.5]) == True
    assert module_0.is_sorted([1.5, 2.5, 2.5, 2.5]) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_is_sorted()