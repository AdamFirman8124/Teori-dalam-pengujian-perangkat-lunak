

# Generated at 2026-10-25 10:45:59.322425
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

# Generated at 2026-10-25 10:46:00.755257
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

# Generated at 2026-10-25 10:46:03.314544
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

# Generated at 2026-10-25 10:46:04.850156
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

# Generated at 2026-10-25 10:46:59.532450
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