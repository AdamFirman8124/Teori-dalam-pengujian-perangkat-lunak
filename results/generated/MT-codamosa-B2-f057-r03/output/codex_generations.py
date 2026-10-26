

# Generated at 2026-10-25 12:17:06.271065
# Unit test for function monotonic

# Generated at 2026-10-25 12:17:14.788667
# Unit test for function monotonic
def test_monotonic():assert module_0.monotonic([1, 2, 3, 4]) == True

# Generated at 2026-10-25 12:17:23.602517
# Unit test for function monotonic
def test_monotonic():
    # strictly increasing
    assert module_0.monotonic([1, 2, 3, 4, 5]) == True
    # strictly decreasing
    assert module_0.monotonic([5, 4, 3, 2, 1]) == True
    # non-strictly increasing with duplicates
    assert module_0.monotonic([1, 2, 2, 3, 4]) == True
    # non-strictly decreasing with duplicates
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
    assert module_0.monotonic([2, 1]) == True
    # negative numbers and floats
    assert module_0.monotonic([-3, -2, -1, 0]) == True
    assert module_0.monotonic([3.5, 2.1, 0.5]) == True
    assert module_0.monotonic([1.1, 2.2, 1.1]) == False

# Generated at 2026-10-25 12:18:11.296158
# Unit test for function monotonic

# Generated at 2026-10-25 12:18:13.709852
# Unit test for function monotonic

# Generated at 2026-10-25 12:19:01.472561
# Unit test for function monotonic

# Generated at 2026-10-25 12:19:03.129001
# Unit test for function monotonic
def test_monotonic():
    # strictly increasing
    assert module_0.monotonic([1, 2, 3, 4, 5]) == True
    # strictly decreasing
    assert module_0.monotonic([5, 4, 3, 2, 1]) == True
    # non-strictly increasing with duplicates
    assert module_0.monotonic([1, 2, 2, 3, 4]) == True
    # non-strictly decreasing with duplicates
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
    assert module_0.monotonic([2, 1]) == True
    # negative numbers and floats
    assert module_0.monotonic([-3, -2, -1, 0]) == True
    assert module_0.monotonic([3.5, 2.1, 0.5]) == True
    assert module_0.monotonic([1.1, 2.2, 1.1]) == False

# Generated at 2026-10-25 12:19:04.667613
# Unit test for function monotonic
def test_monotonic():
    # strictly increasing
    assert module_0.monotonic([1, 2, 3, 4, 5]) == True
    # strictly decreasing
    assert module_0.monotonic([5, 4, 3, 2, 1]) == True
    # non-strictly increasing with duplicates
    assert module_0.monotonic([1, 2, 2, 3, 4]) == True
    # non-strictly decreasing with duplicates
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
    assert module_0.monotonic([2, 1]) == True
    # negative numbers and floats
    assert module_0.monotonic([-3, -2, -1, 0]) == True
    assert module_0.monotonic([3.5, 2.1, 0.5]) == True
    assert module_0.monotonic([1.1, 2.2, 1.1]) == False