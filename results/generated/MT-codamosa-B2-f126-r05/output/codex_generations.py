

# Generated at 2026-10-24 19:47:57.620708
# Unit test for function is_sorted
def test_is_sorted():
    # Empty and single-element lists
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True

    # Sorted lists
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    # Unsorted lists
    assert module_0.is_sorted([2, 1]) is False
    assert module_0.is_sorted([1, 3, 2, 4]) is False

    # A value occurring more than twice is invalid
    assert module_0.is_sorted([1, 1, 1, 2, 3]) is False

    # Negative values
    assert module_0.is_sorted([-3, -2, -2, -1]) is True

# Generated at 2026-10-24 19:48:02.534980
# Unit test for function is_sorted
def test_is_sorted():
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([1]) is True
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True

    assert module_0.is_sorted([1, 1, 1, 2, 3]) is False  # More than two duplicates
    assert module_0.is_sorted([3, 2, 1]) is False        # Descending order
    assert module_0.is_sorted([1, 3, 2, 4]) is False     # Unsorted
    assert module_0.is_sorted([2, 2, 1]) is False

    print("All tests passed.")


test_is_sorted()

# Generated at 2026-10-24 19:48:07.505019
# Unit test for function is_sorted
def test_is_sorted():
    # Sorted lists
    assert module_0.is_sorted([1, 2, 3, 4]) is True
    assert module_0.is_sorted([1, 1, 2, 2, 3]) is True
    assert module_0.is_sorted([-3, -1, 0, 2]) is True

    # Unsorted lists
    assert module_0.is_sorted([3, 2, 1]) is False
    assert module_0.is_sorted([1, 3, 2, 4]) is False

    # A value appearing more than twice is rejected
    assert module_0.is_sorted([1, 1, 1, 2]) is False
    assert module_0.is_sorted([1, 2, 2, 2, 3]) is False

    # Edge cases
    assert module_0.is_sorted([]) is True
    assert module_0.is_sorted([5]) is True
    assert module_0.is_sorted([5, 5]) is True

# Generated at 2026-10-24 19:48:10.046196
# Unit test for function is_sorted

# Generated at 2026-10-24 19:48:12.554444
# Unit test for function is_sorted

# Generated at 2026-10-24 19:48:14.977792
# Unit test for function is_sorted

# Generated at 2026-10-24 19:48:17.492078
# Unit test for function is_sorted

# Generated at 2026-10-24 19:48:19.911627
# Unit test for function is_sorted

# Generated at 2026-10-24 19:48:22.330506
# Unit test for function is_sorted