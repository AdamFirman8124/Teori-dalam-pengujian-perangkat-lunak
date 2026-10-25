

# Generated at 2026-10-24 12:56:03.130005
# Unit test for function double_the_difference
def test_double_the_difference():
    # empty list
    assert module_0.double_the_difference([]) == 0

    # only positive odd integers are squared and summed
    assert module_0.double_the_difference([1, 3, 2, 0]) == 1 + 9  # = 10
    assert module_0.double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25  # = 35
    assert module_0.double_the_difference([9, -2]) == 81
    assert module_0.double_the_difference([1]) == 1
    assert module_0.double_the_difference([5]) == 25

    # negatives, zeros and evens are ignored
    assert module_0.double_the_difference([-1, -2, 0]) == 0
    assert module_0.double_the_difference([0]) == 0
    assert module_0.double_the_difference([2, 4, 6]) == 0
    assert module_0.double_the_difference([-3, -5, 1]) == 1

    # floats are not integers -> ignored, even if whole value
    assert module_0.double_the_difference([1.5, 2.5, 3]) == 9
    assert module_0.double_the_difference([3.0, 1, 5]) == 1 + 25  #

# Generated at 2026-10-24 12:56:04.491953
# Unit test for function double_the_difference
def test_double_the_difference():
    # empty list
    assert module_0.double_the_difference([]) == 0

    # only positive odd integers are squared and summed
    assert module_0.double_the_difference([1, 3, 2, 0]) == 1 + 9  # = 10
    assert module_0.double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25  # = 35
    assert module_0.double_the_difference([9, -2]) == 81
    assert module_0.double_the_difference([1]) == 1
    assert module_0.double_the_difference([5]) == 25

    # negatives, zeros and evens are ignored
    assert module_0.double_the_difference([-1, -2, 0]) == 0
    assert module_0.double_the_difference([0]) == 0
    assert module_0.double_the_difference([2, 4, 6]) == 0
    assert module_0.double_the_difference([-3, -5, 1]) == 1

    # floats are not integers -> ignored, even if whole value
    assert module_0.double_the_difference([1.5, 2.5, 3]) == 9
    assert module_0.double_the_difference([3.0, 1, 5]) == 1 + 25  #

# Generated at 2026-10-24 12:56:06.174529
# Unit test for function double_the_difference
def test_double_the_difference():
    # empty list
    assert module_0.double_the_difference([]) == 0

    # only positive odd integers are squared and summed
    assert module_0.double_the_difference([1, 3, 2, 0]) == 1 + 9  # = 10
    assert module_0.double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25  # = 35
    assert module_0.double_the_difference([9, -2]) == 81
    assert module_0.double_the_difference([1]) == 1
    assert module_0.double_the_difference([5]) == 25

    # negatives, zeros and evens are ignored
    assert module_0.double_the_difference([-1, -2, 0]) == 0
    assert module_0.double_the_difference([0]) == 0
    assert module_0.double_the_difference([2, 4, 6]) == 0
    assert module_0.double_the_difference([-3, -5, 1]) == 1

    # floats are not integers -> ignored, even if whole value
    assert module_0.double_the_difference([1.5, 2.5, 3]) == 9
    assert module_0.double_the_difference([3.0, 1, 5]) == 1 + 25  #

# Generated at 2026-10-24 12:56:08.171611
# Unit test for function double_the_difference
def test_double_the_difference():
    # empty list
    assert module_0.double_the_difference([]) == 0

    # only positive odd integers are squared and summed
    assert module_0.double_the_difference([1, 3, 2, 0]) == 1 + 9  # = 10
    assert module_0.double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25  # = 35
    assert module_0.double_the_difference([9, -2]) == 81
    assert module_0.double_the_difference([1]) == 1
    assert module_0.double_the_difference([5]) == 25

    # negatives, zeros and evens are ignored
    assert module_0.double_the_difference([-1, -2, 0]) == 0
    assert module_0.double_the_difference([0]) == 0
    assert module_0.double_the_difference([2, 4, 6]) == 0
    assert module_0.double_the_difference([-3, -5, 1]) == 1

    # floats are not integers -> ignored, even if whole value
    assert module_0.double_the_difference([1.5, 2.5, 3]) == 9
    assert module_0.double_the_difference([3.0, 1, 5]) == 1 + 25  #

# Generated at 2026-10-24 12:56:13.610332
# Unit test for function double_the_difference
def test_double_the_difference():
    # empty list
    assert module_0.double_the_difference([]) == 0

    # only positive odd integers are squared and summed
    assert module_0.double_the_difference([1, 3, 2, 0]) == 1 + 9  # = 10
    assert module_0.double_the_difference([1, 2, 3, 4, 5]) == 1 + 9 + 25  # = 35
    assert module_0.double_the_difference([9, -2]) == 81
    assert module_0.double_the_difference([1]) == 1
    assert module_0.double_the_difference([5]) == 25

    # negatives, zeros and evens are ignored
    assert module_0.double_the_difference([-1, -2, 0]) == 0
    assert module_0.double_the_difference([0]) == 0
    assert module_0.double_the_difference([2, 4, 6]) == 0
    assert module_0.double_the_difference([-3, -5, 1]) == 1

    # floats are not integers -> ignored, even if whole value
    assert module_0.double_the_difference([1.5, 2.5, 3]) == 9
    assert module_0.double_the_difference([3.0, 1, 5]) == 1 + 25  #