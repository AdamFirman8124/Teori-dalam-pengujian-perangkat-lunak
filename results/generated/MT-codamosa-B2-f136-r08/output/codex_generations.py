

# Generated at 2026-10-25 02:59:12.810112
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Mixed negatives and positives: largest negative, smallest positive
    assert module_0.largest_smallest_integers([-5, -2, 3, 1]) == (-2, 1)
    assert module_0.largest_smallest_integers([-1, -3, 5, 2]) == (-1, 2)
    assert module_0.largest_smallest_integers([-2, -2, 3, 3]) == (-2, 3)

    # Only negatives / only positives
    assert module_0.largest_smallest_integers([-10, -5, -9]) == (-5, None)
    assert module_0.largest_smallest_integers([10, 5, 9]) == (None, 5)

    # No negatives and no positives
    assert module_0.largest_smallest_integers([]) == (None, None)
    assert module_0.largest_smallest_integers([0, 0]) == (None, None)

    # Zero is ignored
    assert module_0.largest_smallest_integers([0, -4, 0, 7]) == (-4, 7)

    # Single element
    assert module_0.largest_smallest_integers([-3]) == (-3, None)
    assert module_0.largest_smallest_integers([3]) == (None, 3)

# Generated at 2026-10-25 02:59:14.127012
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Mixed negatives and positives: largest negative, smallest positive
    assert module_0.largest_smallest_integers([-5, -2, 3, 1]) == (-2, 1)
    assert module_0.largest_smallest_integers([-1, -3, 5, 2]) == (-1, 2)
    assert module_0.largest_smallest_integers([-2, -2, 3, 3]) == (-2, 3)

    # Only negatives / only positives
    assert module_0.largest_smallest_integers([-10, -5, -9]) == (-5, None)
    assert module_0.largest_smallest_integers([10, 5, 9]) == (None, 5)

    # No negatives and no positives
    assert module_0.largest_smallest_integers([]) == (None, None)
    assert module_0.largest_smallest_integers([0, 0]) == (None, None)

    # Zero is ignored
    assert module_0.largest_smallest_integers([0, -4, 0, 7]) == (-4, 7)

    # Single element
    assert module_0.largest_smallest_integers([-3]) == (-3, None)
    assert module_0.largest_smallest_integers([3]) == (None, 3)

# Generated at 2026-10-25 02:59:15.449987
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Mixed negatives and positives: largest negative, smallest positive
    assert module_0.largest_smallest_integers([-5, -2, 3, 1]) == (-2, 1)
    assert module_0.largest_smallest_integers([-1, -3, 5, 2]) == (-1, 2)
    assert module_0.largest_smallest_integers([-2, -2, 3, 3]) == (-2, 3)

    # Only negatives / only positives
    assert module_0.largest_smallest_integers([-10, -5, -9]) == (-5, None)
    assert module_0.largest_smallest_integers([10, 5, 9]) == (None, 5)

    # No negatives and no positives
    assert module_0.largest_smallest_integers([]) == (None, None)
    assert module_0.largest_smallest_integers([0, 0]) == (None, None)

    # Zero is ignored
    assert module_0.largest_smallest_integers([0, -4, 0, 7]) == (-4, 7)

    # Single element
    assert module_0.largest_smallest_integers([-3]) == (-3, None)
    assert module_0.largest_smallest_integers([3]) == (None, 3)

# Generated at 2026-10-25 02:59:16.829476
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Mixed negatives and positives: largest negative, smallest positive
    assert module_0.largest_smallest_integers([-5, -2, 3, 1]) == (-2, 1)
    assert module_0.largest_smallest_integers([-1, -3, 5, 2]) == (-1, 2)
    assert module_0.largest_smallest_integers([-2, -2, 3, 3]) == (-2, 3)

    # Only negatives / only positives
    assert module_0.largest_smallest_integers([-10, -5, -9]) == (-5, None)
    assert module_0.largest_smallest_integers([10, 5, 9]) == (None, 5)

    # No negatives and no positives
    assert module_0.largest_smallest_integers([]) == (None, None)
    assert module_0.largest_smallest_integers([0, 0]) == (None, None)

    # Zero is ignored
    assert module_0.largest_smallest_integers([0, -4, 0, 7]) == (-4, 7)

    # Single element
    assert module_0.largest_smallest_integers([-3]) == (-3, None)
    assert module_0.largest_smallest_integers([3]) == (None, 3)

# Generated at 2026-10-25 02:59:18.156371
# Unit test for function largest_smallest_integers
def test_largest_smallest_integers():
    # Mixed negatives and positives: largest negative, smallest positive
    assert module_0.largest_smallest_integers([-5, -2, 3, 1]) == (-2, 1)
    assert module_0.largest_smallest_integers([-1, -3, 5, 2]) == (-1, 2)
    assert module_0.largest_smallest_integers([-2, -2, 3, 3]) == (-2, 3)

    # Only negatives / only positives
    assert module_0.largest_smallest_integers([-10, -5, -9]) == (-5, None)
    assert module_0.largest_smallest_integers([10, 5, 9]) == (None, 5)

    # No negatives and no positives
    assert module_0.largest_smallest_integers([]) == (None, None)
    assert module_0.largest_smallest_integers([0, 0]) == (None, None)

    # Zero is ignored
    assert module_0.largest_smallest_integers([0, -4, 0, 7]) == (-4, 7)

    # Single element
    assert module_0.largest_smallest_integers([-3]) == (-3, None)
    assert module_0.largest_smallest_integers([3]) == (None, 3)