

# Generated at 2026-10-24 06:20:32.415909
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # examples from spec
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([]) == (None, None)
    assert module_0.largest_smallest_integers([0]) == (None, None)

    # mixed negatives and positives
    assert module_0.largest_smallest_integers([-1, -2, -3, 1, 2, 3]) == (-1, 1)
    assert module_0.largest_smallest_integers([0, -1, 1]) == (-1, 1)
    assert module_0.largest_smallest_integers([-10, 0, 10, -1, 1]) == (-1, 1)

    # only negatives
    assert module_0.largest_smallest_integers([-5, -1, -10]) == (-1, None)
    assert module_0.largest_smallest_integers([-5]) == (-5, None)
    assert module_0.largest_smallest_integers([-3, -2, -1, 0]) == (-1, None)

    # only positives
    assert module_0.largest_smallest_integers([5, 1, 10]) == (None, 1)
    assert module_0.largest_smallest_integers([5]) == (None, 5)
    assert module_0.largest_smallest_integers([0, 1, 2, 3]) == (None, 1)

    # zeros are neither negative nor positive
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)

# Generated at 2026-10-24 06:20:33.824359
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # examples from spec
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([]) == (None, None)
    assert module_0.largest_smallest_integers([0]) == (None, None)

    # mixed negatives and positives
    assert module_0.largest_smallest_integers([-1, -2, -3, 1, 2, 3]) == (-1, 1)
    assert module_0.largest_smallest_integers([0, -1, 1]) == (-1, 1)
    assert module_0.largest_smallest_integers([-10, 0, 10, -1, 1]) == (-1, 1)

    # only negatives
    assert module_0.largest_smallest_integers([-5, -1, -10]) == (-1, None)
    assert module_0.largest_smallest_integers([-5]) == (-5, None)
    assert module_0.largest_smallest_integers([-3, -2, -1, 0]) == (-1, None)

    # only positives
    assert module_0.largest_smallest_integers([5, 1, 10]) == (None, 1)
    assert module_0.largest_smallest_integers([5]) == (None, 5)
    assert module_0.largest_smallest_integers([0, 1, 2, 3]) == (None, 1)

    # zeros are neither negative nor positive
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)

# Generated at 2026-10-24 06:20:35.166610
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # examples from spec
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([]) == (None, None)
    assert module_0.largest_smallest_integers([0]) == (None, None)

    # mixed negatives and positives
    assert module_0.largest_smallest_integers([-1, -2, -3, 1, 2, 3]) == (-1, 1)
    assert module_0.largest_smallest_integers([0, -1, 1]) == (-1, 1)
    assert module_0.largest_smallest_integers([-10, 0, 10, -1, 1]) == (-1, 1)

    # only negatives
    assert module_0.largest_smallest_integers([-5, -1, -10]) == (-1, None)
    assert module_0.largest_smallest_integers([-5]) == (-5, None)
    assert module_0.largest_smallest_integers([-3, -2, -1, 0]) == (-1, None)

    # only positives
    assert module_0.largest_smallest_integers([5, 1, 10]) == (None, 1)
    assert module_0.largest_smallest_integers([5]) == (None, 5)
    assert module_0.largest_smallest_integers([0, 1, 2, 3]) == (None, 1)

    # zeros are neither negative nor positive
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)

# Generated at 2026-10-24 06:20:36.520580
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # examples from spec
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([]) == (None, None)
    assert module_0.largest_smallest_integers([0]) == (None, None)

    # mixed negatives and positives
    assert module_0.largest_smallest_integers([-1, -2, -3, 1, 2, 3]) == (-1, 1)
    assert module_0.largest_smallest_integers([0, -1, 1]) == (-1, 1)
    assert module_0.largest_smallest_integers([-10, 0, 10, -1, 1]) == (-1, 1)

    # only negatives
    assert module_0.largest_smallest_integers([-5, -1, -10]) == (-1, None)
    assert module_0.largest_smallest_integers([-5]) == (-5, None)
    assert module_0.largest_smallest_integers([-3, -2, -1, 0]) == (-1, None)

    # only positives
    assert module_0.largest_smallest_integers([5, 1, 10]) == (None, 1)
    assert module_0.largest_smallest_integers([5]) == (None, 5)
    assert module_0.largest_smallest_integers([0, 1, 2, 3]) == (None, 1)

    # zeros are neither negative nor positive
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)

# Generated at 2026-10-24 06:20:37.923412
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # examples from spec
    assert module_0.largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    assert module_0.largest_smallest_integers([]) == (None, None)
    assert module_0.largest_smallest_integers([0]) == (None, None)

    # mixed negatives and positives
    assert module_0.largest_smallest_integers([-1, -2, -3, 1, 2, 3]) == (-1, 1)
    assert module_0.largest_smallest_integers([0, -1, 1]) == (-1, 1)
    assert module_0.largest_smallest_integers([-10, 0, 10, -1, 1]) == (-1, 1)

    # only negatives
    assert module_0.largest_smallest_integers([-5, -1, -10]) == (-1, None)
    assert module_0.largest_smallest_integers([-5]) == (-5, None)
    assert module_0.largest_smallest_integers([-3, -2, -1, 0]) == (-1, None)

    # only positives
    assert module_0.largest_smallest_integers([5, 1, 10]) == (None, 1)
    assert module_0.largest_smallest_integers([5]) == (None, 5)
    assert module_0.largest_smallest_integers([0, 1, 2, 3]) == (None, 1)

    # zeros are neither negative nor positive
    assert module_0.largest_smallest_integers([0, 0, 0]) == (None, None)