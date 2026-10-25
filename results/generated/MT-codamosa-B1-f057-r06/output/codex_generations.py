

# Generated at 2026-10-24 21:42:54.905258
# Unit test for function monotonic
def test_monotonic():
    # strictly increasing
    assert module_0.monotonic([1, 2, 3, 4, 5]) == True
    # strictly decreasing
    assert module_0.monotonic([5, 4, 3, 2, 1]) == True
    # non-decreasing with duplicates
    assert module_0.monotonic([1, 2, 2, 3, 4]) == True
    # non-increasing with duplicates
    assert module_0.monotonic([5, 4, 4, 2, 1]) == True
    # all equal - both increasing and decreasing
    assert module_0.monotonic([2, 2, 2, 2]) == True
    # not monotonic
    assert module_0.monotonic([1, 3, 2, 4]) == False
    assert module_0.monotonic([1, 2, 5, 3, 4]) == False
    # edge cases
    assert module_0.monotonic([]) == True
    assert module_0.monotonic([1]) == True
    assert module_0.monotonic([1, 1]) == True
    # negatives and floats
    assert module_0.monotonic([-3, -2, -1, 0]) == True
    assert module_0.monotonic([3.5, 2.1, 0.5]) == True

# Generated at 2026-10-24 21:42:57.325556
# Unit test for function monotonic

# Generated at 2026-10-24 21:42:59.740268
# Unit test for function monotonic

# Generated at 2026-10-24 21:43:02.157044
# Unit test for function monotonic

# Generated at 2026-10-24 21:43:04.574132
# Unit test for function monotonic

# Generated at 2026-10-24 21:43:06.990950
# Unit test for function monotonic

# Generated at 2026-10-24 21:43:09.409217
# Unit test for function monotonic

# Generated at 2026-10-24 21:43:11.826577
# Unit test for function monotonic

# Generated at 2026-10-24 21:43:14.246643
# Unit test for function monotonic

# Generated at 2026-10-24 21:43:16.664883
# Unit test for function monotonic

# Generated at 2026-10-24 21:43:19.083653
# Unit test for function monotonic

# Generated at 2026-10-24 21:43:21.500328
# Unit test for function monotonic

# Generated at 2026-10-24 21:43:23.917261
# Unit test for function monotonic