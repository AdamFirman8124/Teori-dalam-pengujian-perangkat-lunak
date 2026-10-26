

# Generated at 2026-10-25 06:53:29.812163
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

# Generated at 2026-10-25 06:53:32.421878
# Unit test for function next_smallest

# Generated at 2026-10-25 06:53:34.841392
# Unit test for function next_smallest

# Generated at 2026-10-25 06:53:37.256445
# Unit test for function next_smallest

# Generated at 2026-10-25 06:53:39.672952
# Unit test for function next_smallest

# Generated at 2026-10-25 06:53:42.276453
# Unit test for function next_smallest

# Generated at 2026-10-25 06:53:44.693938
# Unit test for function next_smallest

# Generated at 2026-10-25 06:53:47.269272
# Unit test for function next_smallest

# Generated at 2026-10-25 06:53:49.687653
# Unit test for function next_smallest

# Generated at 2026-10-25 06:53:52.197756
# Unit test for function next_smallest

# Generated at 2026-10-25 06:53:54.528149
# Unit test for function next_smallest

# Generated at 2026-10-25 06:53:56.943656
# Unit test for function next_smallest

# Generated at 2026-10-25 06:53:59.357990
# Unit test for function next_smallest