

# Generated at 2026-10-25 02:46:28.361837
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

# Generated at 2026-10-25 02:46:30.779445
# Unit test for function largest_smallest_integers

# Generated at 2026-10-25 02:46:33.353679
# Unit test for function largest_smallest_integers

# Generated at 2026-10-25 02:46:35.770624
# Unit test for function largest_smallest_integers

# Generated at 2026-10-25 02:46:38.184750
# Unit test for function largest_smallest_integers

# Generated at 2026-10-25 02:46:40.598915
# Unit test for function largest_smallest_integers

# Generated at 2026-10-25 02:46:43.014879
# Unit test for function largest_smallest_integers

# Generated at 2026-10-25 02:46:45.430582
# Unit test for function largest_smallest_integers

# Generated at 2026-10-25 02:46:47.850034
# Unit test for function largest_smallest_integers

# Generated at 2026-10-25 02:46:50.260699
# Unit test for function largest_smallest_integers

# Generated at 2026-10-25 02:46:52.676687
# Unit test for function largest_smallest_integers

# Generated at 2026-10-25 02:46:55.104526
# Unit test for function largest_smallest_integers

# Generated at 2026-10-25 02:46:57.519432
# Unit test for function largest_smallest_integers