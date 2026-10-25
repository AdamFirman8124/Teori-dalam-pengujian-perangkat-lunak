

# Generated at 2026-10-24 20:53:24.859644
# Unit test for function smallest_change

# Generated at 2026-10-24 20:53:27.275112
# Unit test for function smallest_change

# Generated at 2026-10-24 20:53:29.694132
# Unit test for function smallest_change

# Generated at 2026-10-24 20:53:32.108500
# Unit test for function smallest_change

# Generated at 2026-10-24 20:53:34.523391
# Unit test for function smallest_change

# Generated at 2026-10-24 20:53:36.940564
# Unit test for function smallest_change

# Generated at 2026-10-24 20:53:46.078861
# Unit test for function smallest_change
def test_smallest_change():
    assert module_0.smallest_change([1, 2, 3, 5, 4, 7, 9, 6]) == 4
    assert module_0.smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    assert module_0.smallest_change([1, 2, 3, 2, 1]) == 0
    assert module_0.smallest_change([]) == 0
    assert module_0.smallest_change([1]) == 0
    assert module_0.smallest_change([1, 1]) == 0
    assert module_0.smallest_change([1, 2]) == 1
    assert module_0.smallest_change([1, 2, 3, 4]) == 2
    assert module_0.smallest_change([5, 5, 5, 5]) == 0

# Generated at 2026-10-24 20:53:47.400527
# Unit test for function smallest_change
def test_smallest_change():
    # Already a palindrome
    assert module_0.smallest_change([1, 2, 3, 2, 1]) == 0
    assert module_0.smallest_change([1, 2, 2, 1]) == 0
    assert module_0.smallest_change([]) == 0
    assert module_0.smallest_change([7]) == 0

    # One mismatch
    assert module_0.smallest_change([1, 2, 3, 5, 1]) == 1
    assert module_0.smallest_change([1, 2, 3, 4, 3, 5]) == 1

    # All pairs mismatched
    assert module_0.smallest_change([1, 2, 3, 4, 5, 6]) == 3
    assert module_0.smallest_change([1, 2, 3]) == 1

    # Mixed
    assert module_0.smallest_change([1, 2, 3, 2, 1, 4]) == 1
    assert module_0.smallest_change([2, 3, 4, 3, 2]) == 0

    print("All tests passed!")


test_smallest_change()

# Generated at 2026-10-24 20:53:48.721452
# Unit test for function smallest_change
def test_smallest_change():
    # Already a palindrome
    assert module_0.smallest_change([1, 2, 3, 2, 1]) == 0
    assert module_0.smallest_change([1, 2, 2, 1]) == 0
    assert module_0.smallest_change([]) == 0
    assert module_0.smallest_change([7]) == 0

    # One mismatch
    assert module_0.smallest_change([1, 2, 3, 5, 1]) == 1
    assert module_0.smallest_change([1, 2, 3, 4, 3, 5]) == 1

    # All pairs mismatched
    assert module_0.smallest_change([1, 2, 3, 4, 5, 6]) == 3
    assert module_0.smallest_change([1, 2, 3]) == 1

    # Mixed
    assert module_0.smallest_change([1, 2, 3, 2, 1, 4]) == 1
    assert module_0.smallest_change([2, 3, 4, 3, 2]) == 0

    print("All tests passed!")


test_smallest_change()