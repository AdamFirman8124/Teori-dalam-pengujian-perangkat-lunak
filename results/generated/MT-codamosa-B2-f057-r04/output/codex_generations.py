

# Generated at 2026-10-25 11:58:44.663061
# Unit test for function monotonic
def test_monotonic():
    # Increasing
    assert module_0.monotonic([1, 2, 4, 20]) is True
    # Decreasing
    assert module_0.monotonic([5, 4, 3, 1]) is True
    # Non-decreasing (duplicates allowed)
    assert module_0.monotonic([1, 2, 2, 3]) is True
    # Non-increasing (duplicates allowed)
    assert module_0.monotonic([4, 4, 3, 1]) is True
    # Not monotonic
    assert module_0.monotonic([1, 3, 2, 4]) is False
    assert module_0.monotonic([5, 1, 5]) is False
    # Edge cases
    assert module_0.monotonic([]) is True            # empty list
    assert module_0.monotonic([7]) is True           # single element
    assert module_0.monotonic([2, 2, 2]) is True     # all equal
    assert module_0.monotonic([1, 2, 1]) is False    # up then down

# Generated at 2026-10-25 11:58:46.822572
# Unit test for function monotonic
def test_monotonic():
    # Increasing
    assert module_0.monotonic([1, 2, 4, 20]) is True
    # Decreasing
    assert module_0.monotonic([5, 4, 3, 1]) is True
    # Non-decreasing (duplicates allowed)
    assert module_0.monotonic([1, 2, 2, 3]) is True
    # Non-increasing (duplicates allowed)
    assert module_0.monotonic([4, 4, 3, 1]) is True
    # Not monotonic
    assert module_0.monotonic([1, 3, 2, 4]) is False
    assert module_0.monotonic([5, 1, 5]) is False
    # Edge cases
    assert module_0.monotonic([]) is True            # empty list
    assert module_0.monotonic([7]) is True           # single element
    assert module_0.monotonic([2, 2, 2]) is True     # all equal
    assert module_0.monotonic([1, 2, 1]) is False    # up then down

# Generated at 2026-10-25 11:58:48.284455
# Unit test for function monotonic
def test_monotonic():
    # Increasing
    assert module_0.monotonic([1, 2, 4, 20]) is True
    # Decreasing
    assert module_0.monotonic([5, 4, 3, 1]) is True
    # Non-decreasing (duplicates allowed)
    assert module_0.monotonic([1, 2, 2, 3]) is True
    # Non-increasing (duplicates allowed)
    assert module_0.monotonic([4, 4, 3, 1]) is True
    # Not monotonic
    assert module_0.monotonic([1, 3, 2, 4]) is False
    assert module_0.monotonic([5, 1, 5]) is False
    # Edge cases
    assert module_0.monotonic([]) is True            # empty list
    assert module_0.monotonic([7]) is True           # single element
    assert module_0.monotonic([2, 2, 2]) is True     # all equal
    assert module_0.monotonic([1, 2, 1]) is False    # up then down

# Generated at 2026-10-25 11:58:49.698426
# Unit test for function monotonic
def test_monotonic():
    # Increasing
    assert module_0.monotonic([1, 2, 4, 20]) is True
    # Decreasing
    assert module_0.monotonic([5, 4, 3, 1]) is True
    # Non-decreasing (duplicates allowed)
    assert module_0.monotonic([1, 2, 2, 3]) is True
    # Non-increasing (duplicates allowed)
    assert module_0.monotonic([4, 4, 3, 1]) is True
    # Not monotonic
    assert module_0.monotonic([1, 3, 2, 4]) is False
    assert module_0.monotonic([5, 1, 5]) is False
    # Edge cases
    assert module_0.monotonic([]) is True            # empty list
    assert module_0.monotonic([7]) is True           # single element
    assert module_0.monotonic([2, 2, 2]) is True     # all equal
    assert module_0.monotonic([1, 2, 1]) is False    # up then down

# Generated at 2026-10-25 11:58:51.217702
# Unit test for function monotonic
def test_monotonic():
    # Increasing
    assert module_0.monotonic([1, 2, 4, 20]) is True
    # Decreasing
    assert module_0.monotonic([5, 4, 3, 1]) is True
    # Non-decreasing (duplicates allowed)
    assert module_0.monotonic([1, 2, 2, 3]) is True
    # Non-increasing (duplicates allowed)
    assert module_0.monotonic([4, 4, 3, 1]) is True
    # Not monotonic
    assert module_0.monotonic([1, 3, 2, 4]) is False
    assert module_0.monotonic([5, 1, 5]) is False
    # Edge cases
    assert module_0.monotonic([]) is True            # empty list
    assert module_0.monotonic([7]) is True           # single element
    assert module_0.monotonic([2, 2, 2]) is True     # all equal
    assert module_0.monotonic([1, 2, 1]) is False    # up then down