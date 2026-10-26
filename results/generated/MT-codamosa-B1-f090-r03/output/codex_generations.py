

# Generated at 2026-10-25 06:58:47.855864
# Unit test for function next_smallest
def test_next_smallest():
    assert module_0.next_smallest([1, 2, 3, 4]) == 2          # basic
    assert module_0.next_smallest([5, 1, 4, 2, 3]) == 2      # unsorted input
    assert module_0.next_smallest([1, 1, 2, 3]) == 2         # duplicates collapse
    assert module_0.next_smallest([2, 2, 2]) is None         # all duplicates
    assert module_0.next_smallest([]) is None                # empty
    assert module_0.next_smallest([7]) is None               # single element
    assert module_0.next_smallest([-5, -1, -3]) == -3        # negatives
    assert module_0.next_smallest([0, -1, 1]) == 0           # mixed sign
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5    # floats
    print("all tests passed")

# Generated at 2026-10-25 06:58:50.477812
# Unit test for function next_smallest

# Generated at 2026-10-25 06:58:52.890703
# Unit test for function next_smallest

# Generated at 2026-10-25 06:58:55.304522
# Unit test for function next_smallest

# Generated at 2026-10-25 06:58:57.892583
# Unit test for function next_smallest

# Generated at 2026-10-25 06:59:00.306580
# Unit test for function next_smallest

# Generated at 2026-10-25 06:59:02.719533
# Unit test for function next_smallest

# Generated at 2026-10-25 06:59:07.729843
# Unit test for function next_smallest
def test_next_smallest():
    assert module_0.next_smallest([1, 2, 3, 4, 5]) == 2
    assert module_0.next_smallest([5, 1, 4, 3, 2]) == 2
    assert module_0.next_smallest([]) is None
    assert module_0.next_smallest([42]) is None
    assert module_0.next_smallest([7, 7, 7]) is None
    assert module_0.next_smallest([1, 1, 2, 2, 3]) == 2
    assert module_0.next_smallest([-5, -1, -3]) == -3
    assert module_0.next_smallest([2, 1]) == 2
    assert module_0.next_smallest([1.5, 0.5, 2.5]) == 1.5
    assert module_0.next_smallest([0, -1, 0]) == 0
    print("All tests passed!")

# Generated at 2026-10-25 06:59:09.164987
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