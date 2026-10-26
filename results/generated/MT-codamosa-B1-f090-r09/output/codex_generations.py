

# Generated at 2026-10-25 11:37:44.111624
# Unit test for function next_smallest
def test_next_smallest():
    # empty / too short -> None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([1]) is None
    assert module_0.next_smallest([7, 7, 7]) is None

    # basic two-element cases
    assert module_0.next_smallest([1, 2]) == 2
    assert module_0.next_smallest([2, 1]) == 2

    # normal cases
    assert module_0.next_smallest([1, 2, 3]) == 2
    assert module_0.next_smallest([3, 2, 1]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2

    # duplicates should be ignored (distinct values only)
    assert module_0.next_smallest([1, 1, 2]) == 2
    assert module_0.next_smallest([1, 2, 2, 3, 3]) == 2
    assert module_0.next_smallest([5, 5, 4, 4, 3]) == 4

    # negatives and floats
    assert module_0.next_smallest([-5, -2, 0, 3]) == -2
    assert module_0.next_smallest([1.5, 1.2, 1.8]) == 1.5

# Generated at 2026-10-25 11:37:45.749159
# Unit test for function next_smallest
def test_next_smallest():
    # empty / too short -> None
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([1]) is None
    assert module_0.next_smallest([7, 7, 7]) is None

    # basic two-element cases
    assert module_0.next_smallest([1, 2]) == 2
    assert module_0.next_smallest([2, 1]) == 2

    # normal cases
    assert module_0.next_smallest([1, 2, 3]) == 2
    assert module_0.next_smallest([3, 2, 1]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2

    # duplicates should be ignored (distinct values only)
    assert module_0.next_smallest([1, 1, 2]) == 2
    assert module_0.next_smallest([1, 2, 2, 3, 3]) == 2
    assert module_0.next_smallest([5, 5, 4, 4, 3]) == 4

    # negatives and floats
    assert module_0.next_smallest([-5, -2, 0, 3]) == -2
    assert module_0.next_smallest([1.5, 1.2, 1.8]) == 1.5

# Generated at 2026-10-25 11:37:48.644692
# Unit test for function next_smallest

# Generated at 2026-10-25 11:37:51.061119
# Unit test for function next_smallest

# Generated at 2026-10-25 11:37:53.677283
# Unit test for function next_smallest

# Generated at 2026-10-25 11:37:56.091419
# Unit test for function next_smallest

# Generated at 2026-10-25 11:37:58.504981
# Unit test for function next_smallest

# Generated at 2026-10-25 11:38:00.922746
# Unit test for function next_smallest

# Generated at 2026-10-25 11:38:03.396931
# Unit test for function next_smallest

# Generated at 2026-10-25 11:38:06.024019
# Unit test for function next_smallest

# Generated at 2026-10-25 11:38:08.434240
# Unit test for function next_smallest