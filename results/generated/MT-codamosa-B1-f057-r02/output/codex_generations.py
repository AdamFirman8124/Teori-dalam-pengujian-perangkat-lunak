

# Generated at 2026-10-25 12:50:39.958771
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

# Generated at 2026-10-25 12:50:42.640871
# Unit test for function monotonic

# Generated at 2026-10-25 12:50:45.054634
# Unit test for function monotonic

# Generated at 2026-10-25 12:50:47.468325
# Unit test for function monotonic

# Generated at 2026-10-25 12:50:50.082910
# Unit test for function monotonic

# Generated at 2026-10-25 12:50:52.500992
# Unit test for function monotonic

# Generated at 2026-10-25 12:50:54.911708
# Unit test for function monotonic

# Generated at 2026-10-25 12:50:57.325718
# Unit test for function monotonic

# Generated at 2026-10-25 12:50:59.742605
# Unit test for function monotonic

# Generated at 2026-10-25 12:51:02.159048
# Unit test for function monotonic

# Generated at 2026-10-25 12:51:04.974413
# Unit test for function monotonic

# Generated at 2026-10-25 12:51:07.395649
# Unit test for function monotonic

# Generated at 2026-10-25 12:51:09.809917
# Unit test for function monotonic