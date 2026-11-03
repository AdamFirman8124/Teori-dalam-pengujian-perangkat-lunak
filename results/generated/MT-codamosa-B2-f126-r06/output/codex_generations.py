

# Generated at 2026-11-02 19:12:12.829703
# Unit test for function is_sorted
def test_is_sorted():
    # Sorted lists
    assert module_0.is_sorted([1, 2, 3, 4]) == True
    assert module_0.is_sorted([1, 2, 2, 3]) == True  # duplicates up to 2 allowed
    assert module_0.is_sorted([1, 1, 2, 2]) == True
    assert module_0.is_sorted([]) == True            # empty list is sorted
    assert module_0.is_sorted([5]) == True           # single element
    assert module_0.is_sorted([-3, -1, 0, 2]) == True  # negative numbers
    assert module_0.is_sorted([0, 0, 1, 1, 2]) == True

    # Unsorted lists
    assert module_0.is_sorted([1, 3, 2]) == False
    assert module_0.is_sorted([2, 1]) == False
    assert module_0.is_sorted([3, 2, 1]) == False
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False

    # More than 2 occurrences of any element -> False
    assert module_0.is_sorted([1, 1, 1]) == False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    assert module_0.is_sorted([1, 1, 2, 3, 3, 3]) == False
    assert module_0.is_sorted([1, 1, 1, 2, 3]) == False

    # Exactly two occurrences allowed
    assert module_0.is_sorted([1, 1, 2, 3]) == True
    assert module_0.is_sorted([4, 4, 5, 6]) == True

    # Mixed cases
    assert module_0.is_sorted([1, 2, 3, 2]) == False
    assert module_0.is_sorted([10, 20, 20, 30, 30]) == True

    print("All tests passed!")

test_is_sorted()

# Generated at 2026-11-02 19:14:40.009082
# Unit test for function is_sorted
def test_is_sorted():
# nonce:975cdc40
    # Basic sorted list without duplicates
    assert module_0.is_sorted([1, 2, 3, 4]) == True
    assert module_0.is_sorted([5]) == True
    assert module_0.is_sorted([]) == True

    # Sorted list with at most two duplicates
    assert module_0.is_sorted([1, 2, 2, 3]) == True
    assert module_0.is_sorted([1, 1, 2, 3]) == True
    assert module_0.is_sorted([1, 2, 3, 3]) == True
    assert module_0.is_sorted([1, 1, 2, 2, 3, 3]) == True

    # Sorted but an element occurs more than twice
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    assert module_0.is_sorted([1, 1, 1]) == False
    assert module_0.is_sorted([1, 2, 3, 3, 3]) == False

    # Unsorted lists
    assert module_0.is_sorted([3, 2, 1]) == False
    assert module_0.is_sorted([1, 3, 2]) == False
    assert module_0.is_sorted([5, 4]) == False
    assert module_0.is_sorted([2, 1, 2, 2, 2]) == False

    # Unsorted with too many duplicates
    assert module_0.is_sorted([1, 1, 2, 1]) == False

    # Negative numbers and mixed values
    assert module_0.is_sorted([-3, -1, 0, 2]) == True
    assert module_0.is_sorted([-1, -1, -1]) == False
    assert module_0.is_sorted([-2, -2, 0, 1]) == True

    # Two-element edge cases
    assert module_0.is_sorted([1, 2]) == True
    assert module_0.is_sorted([2, 2]) == True
    assert module_0.is_sorted([2, 1]) == False

    # Equal adjacent elements are allowed (non-decreasing)
    assert module_0.is_sorted([0, 0, 1, 1, 2]) == True

# Generated at 2026-11-02 19:16:15.163534
# Unit test for function is_sorted
def test_is_sorted():
    # Simple sorted lists
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True
    assert module_0.is_sorted([1, 2, 2, 3, 4]) == True  # duplicate allowed up to 2
    assert module_0.is_sorted([1, 1, 2, 2, 3]) == True  # two duplicates of each allowed
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False  # descending
    assert module_0.is_sorted([1, 3, 2, 4, 5]) == False  # not sorted
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False  # more than 2 duplicates
    assert module_0.is_sorted([1, 1, 1]) == False  # three identical elements
    assert module_0.is_sorted([1, 1]) == True  # two identical elements
    assert module_0.is_sorted([1]) == True  # single element
    assert module_0.is_sorted([]) == True  # empty list
    assert module_0.is_sorted([2, 1]) == False  # two elements unsorted
    assert module_0.is_sorted([1, 2]) == True  # two elements sorted
    assert module_0.is_sorted([-5, -3, 0, 2, 10]) == True  # negative numbers
    assert module_0.is_sorted([-1, -1, 0, 0, 1, 1]) == True  # duplicates with negatives
    assert module_0.is_sorted([3, 3, 3, 2]) == False  # too many duplicates and unsorted
    assert module_0.is_sorted([0, 0, 0]) == False  # three zeros

# Generated at 2026-11-02 19:16:57.422086
# Unit test for function is_sorted
def test_is_sorted():
    # Sorted list with unique elements
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True
    # Sorted list with one element appearing twice
    assert module_0.is_sorted([1, 2, 2, 3, 4]) == True
    # Sorted list with an element appearing three times
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False
    # Unsorted list
    assert module_0.is_sorted([5, 3, 1]) == False
    # Descending list
    assert module_0.is_sorted([4, 3, 2, 1]) == False
    # Empty list is considered sorted
    assert module_0.is_sorted([]) == True
    # Single element list
    assert module_0.is_sorted([1]) == True
    # Two equal elements (allowed, at most two occurrences)
    assert module_0.is_sorted([2, 2]) == True
    # Three equal elements (more than two occurrences)
    assert module_0.is_sorted([3, 3, 3]) == False
    # Unsorted list with duplicates
    assert module_0.is_sorted([1, 3, 2, 3]) == False
    # Sorted list with multiple duplicate pairs
    assert module_0.is_sorted([1, 1, 2, 2, 3, 3]) == True
    # Sorted list where a duplicate pair appears three times total
    assert module_0.is_sorted([1, 1, 2, 2, 2]) == False
    # Negative numbers, sorted
    assert module_0.is_sorted([-3, -2, -1, 0]) == True

# Generated at 2026-11-02 19:17:34.220770
# Unit test for function is_sorted
def test_is_sorted():
    # Test 1: Sorted list with unique elements
    assert module_0.is_sorted([1, 2, 3, 4, 5]) == True

    # Test 2: Sorted list with an element appearing exactly twice
    assert module_0.is_sorted([1, 2, 2, 3, 4]) == True

    # Test 3: Unsorted list
    assert module_0.is_sorted([3, 1, 2]) == False

    # Test 4: List with an element appearing more than twice (even if sorted)
    assert module_0.is_sorted([1, 2, 2, 2, 3]) == False

    # Test 5: Element appearing more than twice in unsorted list
    assert module_0.is_sorted([1, 3, 3, 3, 2]) == False

    # Test 6: Empty list is considered sorted
    assert module_0.is_sorted([]) == True

    # Test 7: Single element list
    assert module_0.is_sorted([1]) == True

    # Test 8: Two identical elements
    assert module_0.is_sorted([5, 5]) == True

    # Test 9: Descending list
    assert module_0.is_sorted([5, 4, 3, 2, 1]) == False

    # Test 10: Sorted list with duplicates spread out
    assert module_0.is_sorted([1, 1, 2, 3, 3]) == True

    # Test 11: Negative numbers sorted
    assert module_0.is_sorted([-3, -2, -1, 0]) == True

    # Test 12: Negative numbers unsorted
    assert module_0.is_sorted([-1, -3, -2]) == False

    # Test 13: Duplicates at the end sorted
    assert module_0.is_sorted([1, 2, 3, 3]) == True

    # Test 14: Nearly sorted but one violation
    assert module_0.is_sorted([1, 2, 5, 3, 4]) == False