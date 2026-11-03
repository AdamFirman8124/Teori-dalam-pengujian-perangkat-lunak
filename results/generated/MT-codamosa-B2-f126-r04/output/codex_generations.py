

# Generated at 2026-11-03 00:42:00.108307
# Unit test for function is_sorted
def test_is_sorted():
    # Sorted list with unique elements
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True
    # Empty list is considered sorted
    assert module_0.is_sorted([]) == True
    # Single element list
    assert module_0.is_sorted([1]) == True
    # Sorted list with one duplicate (allowed, max 2 occurrences)
    assert module_0.is_sorted([1, 2, 2, 3]) == True
    # Sorted list with two duplicates of same value (allowed)
    assert module_0.is_sorted([1, 2, 2, 3, 3]) == True
    # Element appearing three times even in sorted order -> False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    # Unsorted list -> False
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False
    # Partially unsorted list -> False
    assert module_0.is_sorted([1, 3, 2, 4, 5]) == False
    # Unsorted with triple occurrence -> False
    assert module_0.is_sorted([1, 1, 1, 2]) == False
    # Two equal elements -> True
    assert module_0.is_sorted([2, 2]) == True
    # Three equal elements -> False
    assert module_0.is_sorted([2, 2, 2]) == False
    # Negative numbers sorted -> True
    assert module_0.is_sorted([-5, -3, 0, 2]) == True
    # Negative numbers unsorted -> False
    assert module_0.is_sorted([-3, -5, 0]) == False
    # Duplicates at boundary: exactly two occurrences max, sorted -> True
    assert module_0.is_sorted([1, 1, 2, 2, 3, 3]) == True
    # One value appears three times, unsorted -> False
    assert module_0.is_sorted([3, 1, 1, 1]) == False
    # Non-decreasing with mixed duplicates -> True
    assert module_0.is_sorted([0, 0, 1]) == True

# Generated at 2026-11-03 00:43:53.055881
# Unit test for function is_sorted
def test_is_sorted():
    # Single element list is sorted
    assert module_0.is_sorted([5]) == True
    # Empty list is sorted
    assert module_0.is_sorted([]) == True
    # Sorted list with unique elements
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True
    # Sorted list with an element appearing twice
    assert module_0.is_sorted([1, 2, 2, 3, 3, 4]) == True
    # Sorted list with an element appearing three times
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    # Unsorted list
    assert module_0.is_sorted([1, 3, 2, 4, 5]) == False
    # Unsorted list (descending pair)
    assert module_0.is_sorted([2, 1]) == False
    # List with one element repeated three times
    assert module_0.is_sorted([2, 2, 2]) == False
    # List with element appearing three times even though sorted
    assert module_0.is_sorted([1, 2, 3, 3, 3, 4]) == False
    # Two identical elements
    assert module_0.is_sorted([1, 1]) == True
    # Negative numbers sorted
    assert module_0.is_sorted([-3, -2, -1, 0]) == True
    # Negative numbers unsorted
    assert module_0.is_sorted([-1, -3, -2]) == False
    # Sorted with duplicates at start
    assert module_0.is_sorted([0, 0, 1, 2]) == True
    # Unsorted with duplicate exceeding limit
    assert module_0.is_sorted([1, 5, 5, 5, 2]) == False
    # Large sorted list
    assert module_0.is_sorted(list(range(100))) == True
    # Large unsorted list
    lst = list(range(100))
    lst[50], lst[51] = lst[51], lst[50]
    assert module_0.is_sorted(lst) == False
    print("All tests passed!")


test_is_sorted()

# Generated at 2026-11-03 00:44:58.739885
# Unit test for function is_sorted
def test_is_sorted():
    # Single element list is sorted
    assert module_0.is_sorted([5]) == True

    # Empty list is sorted
    assert module_0.is_sorted([]) == True

    # Sorted lists with unique elements
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True
    assert module_0.is_sorted([1, 2, 3, 4, 5, 6, 7]) == True

    # Sorted lists with duplicates (each appearing at most twice)
    assert module_0.is_sorted([1, 2, 2, 3, 3, 4]) == True
    assert module_0.is_sorted([1, 2, 2, 3]) == True
    assert module_0.is_sorted([1, 1]) == True

    # Unsorted lists
    assert module_0.is_sorted([1, 3, 2, 4, 5]) == False
    assert module_0.is_sorted([2, 1]) == False
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False
    assert module_0.is_sorted([1, 2, 3, 2]) == False

    # Lists with an element appearing more than twice
    assert module_0.is_sorted([1, 2, 2, 2, 3, 4]) == False
    assert module_0.is_sorted([1, 1, 1]) == False
    assert module_0.is_sorted([1, 2, 3, 3, 3, 4]) == False
    assert module_0.is_sorted([2, 2, 2, 2]) == False

    # Duplicates appearing more than twice even if list not sorted
    assert module_0.is_sorted([3, 3, 3, 1, 2]) == False

    # Negative numbers
    assert module_0.is_sorted([-3, -2, -1, 0, 1]) == True
    assert module_0.is_sorted([-1, -2, -3]) == False
    assert module_0.is_sorted([-1, -1, -1]) == False

    print("All tests passed!")


if __name__ == "__main__":
    test_is_sorted()

# Generated at 2026-11-03 00:46:12.050922
# Unit test for function is_sorted
def test_is_sorted():
    # Sorted lists should return True
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True
    assert module_0.is_sorted([1, 2, 2, 3, 4]) == True  # duplicates allowed up to 2
    assert module_0.is_sorted([1, 1, 2, 2, 3]) == True  # each duplicate appears twice
    assert module_0.is_sorted([5, 5, 5]) == False       # element appears 3 times
    assert module_0.is_sorted([1, 3, 2, 4, 5]) == False # not sorted
    assert module_0.is_sorted([]) == True               # empty list is sorted
    assert module_0.is_sorted([1]) == True              # single element is sorted
    assert module_0.is_sorted([2, 1]) == False          # descending pair
    assert module_0.is_sorted([1, 1]) == True           # two equal elements
    assert module_0.is_sorted([1, 1, 1]) == False       # three equal elements
    assert module_0.is_sorted([3, 3, 3, 3]) == False    # four equal elements
    assert module_0.is_sorted([1, 2, 3, 4, 3]) == False # dips at the end
    assert module_0.is_sorted([10, 20, 30]) == True     # larger values
    assert module_0.is_sorted([-3, -2, -1]) == True     # negative numbers
    assert module_0.is_sorted([0, 0, 1, 1, 2]) == True  # multiple pairs
    assert module_0.is_sorted([2, 2, 2, 1]) == False    # too many duplicates and unsorted

# Generated at 2026-11-03 00:47:43.561415
# Unit test for function is_sorted
def test_is_sorted():
    # Already sorted lists
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True
    assert module_0.is_sorted([1, 2, 2, 3]) == True      # duplicate allowed up to twice
    assert module_0.is_sorted([1, 1, 2, 2, 3]) == True
    assert module_0.is_sorted([1, 1]) == True
    assert module_0.is_sorted([1]) == True
    assert module_0.is_sorted([]) == True                # empty list is considered sorted

    # Not sorted
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False
    assert module_0.is_sorted([1, 3, 2]) == False
    assert module_0.is_sorted([2, 2, 1]) == False

    # More than two occurrences of any element
    assert module_0.is_sorted([1, 1, 1]) == False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    assert module_0.is_sorted([1, 2, 3, 3, 3, 4]) == False

    # Mixed cases
    assert module_0.is_sorted([1, 2, 2, 1]) == False     # sorted but not non-decreasing at end
    assert module_0.is_sorted([10, 20, 20, 30]) == True
    assert module_0.is_sorted([0, 0, 0, 1]) == False     # three zeros