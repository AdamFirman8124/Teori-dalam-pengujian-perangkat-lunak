

# Generated at 2026-10-24 04:02:36.926620
# Unit test for function monotonic
def test_monotonic():
    assert module_0.monotonic([1, 2, 3, 4]) is True       # Increasing
    assert module_0.monotonic([4, 3, 2, 1]) is True       # Decreasing
    assert module_0.monotonic([1, 2, 2, 3]) is True       # Non-decreasing
    assert module_0.monotonic([3, 2, 2, 1]) is True       # Non-increasing
    assert module_0.monotonic([1, 3, 2, 4]) is False      # Not monotonic
    assert module_0.monotonic([]) is True                 # Empty list
    assert module_0.monotonic([5]) is True                # Single element
    assert module_0.monotonic([2, 2, 2]) is True          # All equal

# Generated at 2026-10-24 04:02:41.737679
# Unit test for function monotonic
def test_monotonic():
    assert module_0.monotonic([1, 2, 3, 4]) is True
    assert module_0.monotonic([4, 3, 2, 1]) is True
    assert module_0.monotonic([1, 1, 2, 3]) is True
    assert module_0.monotonic([3, 2, 2, 1]) is True
    assert module_0.monotonic([5, 5, 5]) is True
    assert module_0.monotonic([1]) is True
    assert module_0.monotonic([]) is True

    assert module_0.monotonic([1, 3, 2, 4]) is False
    assert module_0.monotonic([4, 2, 3, 1]) is False

# Generated at 2026-10-24 04:02:46.549754
# Unit test for function monotonic
def test_monotonic():
    assert module_0.monotonic([1, 2, 3, 4]) is True       # Increasing
    assert module_0.monotonic([4, 3, 2, 1]) is True       # Decreasing
    assert module_0.monotonic([1, 1, 2, 2]) is True       # Non-decreasing
    assert module_0.monotonic([3, 3, 2, 2]) is True       # Non-increasing
    assert module_0.monotonic([1, 3, 2]) is False         # Neither
    assert module_0.monotonic([]) is True                  # Empty list
    assert module_0.monotonic([5]) is True                 # Single element

# Generated at 2026-10-24 04:02:56.965898
# Unit test for function monotonic
def test_monotonic():
    assert module_0.monotonic([1, 2, 3, 4]) is True       # Increasing
    assert module_0.monotonic([4, 3, 2, 1]) is True       # Decreasing
    assert module_0.monotonic([1, 1, 2, 2]) is True       # Non-decreasing
    assert module_0.monotonic([3, 3, 2, 1]) is True       # Non-increasing
    assert module_0.monotonic([5, 5, 5]) is True          # All equal
    assert module_0.monotonic([1]) is True                # Single element
    assert module_0.monotonic([]) is True                 # Empty list
    assert module_0.monotonic([1, 3, 2]) is False         # Not monotonic
    assert module_0.monotonic([3, 1, 2]) is False         # Not monotonic

# Generated at 2026-10-24 04:03:01.295037
# Unit test for function monotonic
def test_monotonic():
    assert module_0.monotonic([1, 2, 3, 4]) is True
    assert module_0.monotonic([4, 3, 2, 1]) is True
    assert module_0.monotonic([1, 1, 2, 3]) is True
    assert module_0.monotonic([3, 2, 2, 1]) is True
    assert module_0.monotonic([1, 3, 2, 4]) is False
    assert module_0.monotonic([]) is True
    assert module_0.monotonic([1]) is True