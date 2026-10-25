

# Generated at 2026-10-25 00:40:56.601293
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    assert module_0.largest_smallest_integers([-5, -2, 0, 3, 7]) == (-2, 3)
    assert module_0.largest_smallest_integers([1, 2, 3]) == (None, 1)
    assert module_0.largest_smallest_integers([-3, -2, -1]) == (-1, None)
    assert module_0.largest_smallest_integers([0]) == (None, None)
    assert module_0.largest_smallest_integers([]) == (None, None)

# Generated at 2026-10-25 00:41:01.706379
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    assert module_0.largest_smallest_integers([-5, -3, -1, 0, 2, 4]) == (-1, 2)
    assert module_0.largest_smallest_integers([-10, -2, -7]) == (-2, None)
    assert module_0.largest_smallest_integers([3, 8, 1, 5]) == (None, 1)
    assert module_0.largest_smallest_integers([0, 0]) == (None, None)
    assert module_0.largest_smallest_integers([]) == (None, None)
    assert module_0.largest_smallest_integers([-1, -1, 1, 1]) == (-1, 1)

# Generated at 2026-10-25 00:41:06.636381
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-1, -3, -5, -6]) == (-1, None)
    assert module_0.largest_smallest_integers([-1, -3, -5, 2, 4, 6]) == (-1, 2)
    assert module_0.largest_smallest_integers([0, 0]) == (None, None)
    assert module_0.largest_smallest_integers([]) == (None, None)
    assert module_0.largest_smallest_integers([-10, 0, 8, -2, 3]) == (-2, 3)


test_largest_smallest_integers()

# Generated at 2026-10-25 00:41:11.755689
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    assert module_0.largest_smallest_integers([-5, -2, 0, 3, 7]) == (-2, 3)
    assert module_0.largest_smallest_integers([-8, -3, -1]) == (-1, None)
    assert module_0.largest_smallest_integers([2, 4, 9]) == (None, 2)
    assert module_0.largest_smallest_integers([0, 0]) == (None, None)
    assert module_0.largest_smallest_integers([]) == (None, None)
    assert module_0.largest_smallest_integers([-2, -2, 5, 5]) == (-2, 5)

# Generated at 2026-10-25 00:41:16.670781
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([-2, -4, -1, -3, -5]) == (-1, None)
    assert module_0.largest_smallest_integers([-5, 3, -2, 8, 1]) == (-2, 1)
    assert module_0.largest_smallest_integers([0, -4, 2, 0]) == (-4, 2)
    assert module_0.largest_smallest_integers([0, 0]) == (None, None)
    assert module_0.largest_smallest_integers([]) == (None, None)