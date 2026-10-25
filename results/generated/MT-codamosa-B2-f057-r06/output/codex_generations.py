

# Generated at 2026-10-25 01:20:03.189910
# Unit test for function monotonic

# Generated at 2026-10-25 01:20:05.606111
# Unit test for function monotonic

# Generated at 2026-10-25 01:20:08.020064
# Unit test for function monotonic

# Generated at 2026-10-25 01:20:10.433757
# Unit test for function monotonic

# Generated at 2026-10-25 01:20:12.848586
# Unit test for function monotonic

# Generated at 2026-10-25 01:20:15.262537
# Unit test for function monotonic

# Generated at 2026-10-25 01:20:17.677830
# Unit test for function monotonic

# Generated at 2026-10-25 01:20:20.091461
# Unit test for function monotonic

# Generated at 2026-10-25 01:20:25.684070
# Unit test for function monotonic
def test_monotonic():
    # Increasing
    assert module_0.monotonic([1, 2, 4, 20]) == True
    # Decreasing
    assert module_0.monotonic([20, 4, 2, 1]) == True
    # Non-monotonic
    assert module_0.monotonic([1, 20, 4, 10]) == False
    # Non-strict (equal adjacent values) increasing
    assert module_0.monotonic([1, 1, 2, 3]) == True
    # Non-strict (equal adjacent values) decreasing
    assert module_0.monotonic([5, 4, 4, 1]) == True
    # Single element
    assert module_0.monotonic([7]) == True
    # Empty list
    assert module_0.monotonic([]) == True
    # Two equal elements
    assert module_0.monotonic([3, 3]) == True

# Generated at 2026-10-25 01:20:35.690288
# Unit test for function monotonic
def test_monotonic():
    assert module_0.monotonic([1, 2, 3, 4, 5])
    assert module_0.monotonic([5, 4, 3, 2, 1])
    assert module_0.monotonic([1, 2, 2, 3])
    assert module_0.monotonic([3, 2, 2, 1])
    assert module_0.monotonic([1, 1, 1])
    assert module_0.monotonic([])
    assert module_0.monotonic([42])
    assert not module_0.monotonic([1, 3, 2])
    assert not module_0.monotonic([5, 1, 4])
    assert not module_0.monotonic([1, 2, 3, 2, 5])

# Generated at 2026-10-25 01:20:37.008786
# Unit test for function monotonic
def test_monotonic():
    assert module_0.monotonic([1, 2, 3, 4, 5])
    assert module_0.monotonic([5, 4, 3, 2, 1])
    assert module_0.monotonic([1, 2, 2, 3])
    assert module_0.monotonic([3, 2, 2, 1])
    assert module_0.monotonic([1, 1, 1])
    assert module_0.monotonic([])
    assert module_0.monotonic([42])
    assert not module_0.monotonic([1, 3, 2])
    assert not module_0.monotonic([5, 1, 4])
    assert not module_0.monotonic([1, 2, 3, 2, 5])