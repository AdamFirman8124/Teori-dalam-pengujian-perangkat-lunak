

# Generated at 2026-10-24 20:41:53.576141
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

# Generated at 2026-10-24 20:41:55.325425
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

# Generated at 2026-10-24 20:41:59.627489
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

# Generated at 2026-10-24 20:42:01.052167
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

# Generated at 2026-10-24 20:42:02.411621
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