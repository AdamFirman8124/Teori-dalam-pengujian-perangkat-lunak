

# Generated at 2026-11-02 15:11:47.490181
# Unit test for function is_sorted
def test_is_sorted():
    # Sorted list with unique elements
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True
    assert module_0.is_sorted([1, 2, 3]) == True

    # Sorted list with at most 2 duplicates
    assert module_0.is_sorted([1, 2, 2, 3, 4]) == True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) == True
    assert module_0.is_sorted([5, 5]) == True

    # Sorted list with more than 2 duplicates -> False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    assert module_0.is_sorted([1, 1, 1]) == False
    assert module_0.is_sorted([4, 4, 4, 4]) == False

    # Unsorted lists -> False
    assert module_0.is_sorted([3, 1, 2]) == False
    assert module_0.is_sorted([2, 1]) == False
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False

    # Unsorted with duplicates -> False
    assert module_0.is_sorted([1, 3, 2, 2]) == False
    assert module_0.is_sorted([2, 2, 1]) == False

    # Edge cases: empty list and single element
    assert module_0.is_sorted([]) == True
    assert module_0.is_sorted([7]) == True

    # Negative numbers and mixed values
    assert module_0.is_sorted([-3, -1, 0, 2]) == True
    assert module_0.is_sorted([-1, -1, -1]) == False
    assert module_0.is_sorted([0, -1, 1]) == False

    print("All tests passed!")


test_is_sorted()

# Generated at 2026-11-02 15:13:48.947954
# Unit test for function is_sorted
def test_is_sorted():
    # Sorted list with unique elements
    assert module_0.is_sorted([1, 2, 3, 4]) == True
    # Sorted list with an element appearing twice
    assert module_0.is_sorted([1, 2, 2, 3]) == True
    # Sorted list with an element appearing three times
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    # Unsorted list
    assert module_0.is_sorted([1, 3, 2]) == False
    # Empty list is sorted
    assert module_0.is_sorted([]) == True
    # Single element list
    assert module_0.is_sorted([1]) == True
    # Two identical elements
    assert module_0.is_sorted([1, 1]) == True
    # Three identical elements
    assert module_0.is_sorted([1, 1, 1]) == False
    # Descending list
    assert module_0.is_sorted([5, 4, 3, 2]) == False
    # Sorted with multiple duplicates of two
    assert module_0.is_sorted([1, 2, 2, 3, 3]) == True
    # Not sorted even though counts are fine
    assert module_0.is_sorted([2, 1]) == False
    # Duplicates appearing more than twice even if sorted
    assert module_0.is_sorted([1, 1, 1, 2]) == False
    # Sorted list with zeros
    assert module_0.is_sorted([0, 0, 1, 2]) == True
    # Large sorted list
    assert module_0.is_sorted(list(range(100))) == True
    # Large sorted list with triple duplicate
    assert module_0.is_sorted(list(range(10)) + [9, 9]) == False

# Generated at 2026-11-02 15:15:44.247528
# Unit test for function is_sorted
def test_is_sorted():
    # Basic sorted lists
    assert module_0.is_sorted([1, 2, 3, 4]) == True
    assert module_0.is_sorted([1, 2, 2, 3]) == True
    assert module_0.is_sorted([1, 1]) == True
    assert module_0.is_sorted([5]) == True
    assert module_0.is_sorted([]) == True

    # Duplicates exceeding limit (more than 2 occurrences)
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    assert module_0.is_sorted([1, 1, 1]) == False
    assert module_0.is_sorted([4, 4, 4, 4]) == False

    # Unsorted lists
    assert module_0.is_sorted([1, 3, 2]) == False
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False
    assert module_0.is_sorted([2, 2, 1]) == False
    assert module_0.is_sorted([1, 2, 2, 1]) == False

    # Negative numbers and mixed values
    assert module_0.is_sorted([-3, -1, 0, 2]) == True
    assert module_0.is_sorted([-1, -1, -1]) == False
    assert module_0.is_sorted([0, -1, 1]) == False

    # Floats
    assert module_0.is_sorted([1.5, 2.5, 2.5]) == True
    assert module_0.is_sorted([2.5, 1.5]) == False

    print("All tests passed!")


test_is_sorted()

# Generated at 2026-11-02 15:18:14.682433
# Unit test for function is_sorted
def test_is_sorted():
    # Sorted lists (should return True)
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True
    assert module_0.is_sorted([1, 2, 2, 3]) == True          # duplicates allowed up to 2
    assert module_0.is_sorted([1, 1, 2, 2, 3, 3]) == True
    assert module_0.is_sorted([5]) == True                    # single element
    assert module_0.is_sorted([]) == True                     # empty list
    assert module_0.is_sorted([-3, -1, 0, 2, 7]) == True      # negative numbers
    assert module_0.is_sorted([0, 0, 1]) == True              # zeros with duplicate

    # Sorted but element appears more than twice (should return False)
    assert module_0.is_sorted([1, 1, 1]) == False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    assert module_0.is_sorted([1, 1, 2, 2, 2, 3]) == False
    assert module_0.is_sorted([0, 0, 0, 1]) == False

    # Not sorted (should return False)
    assert module_0.is_sorted([3, 2, 1]) == False
    assert module_0.is_sorted([1, 3, 2]) == False
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False
    assert module_0.is_sorted([1, 2, 3, 2]) == False
    assert module_0.is_sorted([2, 1]) == False

    # Not sorted AND too many duplicates (should return False)
    assert module_0.is_sorted([2, 1, 1, 1]) == False
    assert module_0.is_sorted([3, 3, 3, 2]) == False

    print("All test_is_sorted tests passed!")


test_is_sorted()

# Generated at 2026-11-02 15:20:00.888330
# Unit test for function is_sorted
def test_is_sorted():
    # Sorted lists - should return True
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True
    assert module_0.is_sorted([5]) == True
    assert module_0.is_sorted([]) == True
    assert module_0.is_sorted([1, 1, 2, 3, 4]) == True  # duplicates up to 2 allowed
    assert module_0.is_sorted([1, 1, 2, 2, 3]) == True
    assert module_0.is_sorted([1, 1, 1, 2, 2]) == False  # more than 2 duplicates
    assert module_0.is_sorted([1, 1, 1, 1, 1]) == False  # too many duplicates
    assert module_0.is_sorted([1, 2, 3, 3, 3]) == False  # too many duplicates

    # Unsorted lists - should return False
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False
    assert module_0.is_sorted([1, 3, 2]) == False
    assert module_0.is_sorted([2, 1, 2]) == False
    assert module_0.is_sorted([3, 1, 2, 4, 5]) == False

    # Mixed duplicates and unsorted
    assert module_0.is_sorted([1, 2, 2, 1]) == False

    # Negative numbers
    assert module_0.is_sorted([-3, -2, -1, 0]) == True
    assert module_0.is_sorted([-1, -2, -3]) == False

    # Duplicates with negative numbers
    assert module_0.is_sorted([-1, -1, 0, 1]) == True
    assert module_0.is_sorted([-1, -1, -1]) == False

    print("All test cases passed!")


# Run the tests
if __name__ == "__main__":
    test_is_sorted()