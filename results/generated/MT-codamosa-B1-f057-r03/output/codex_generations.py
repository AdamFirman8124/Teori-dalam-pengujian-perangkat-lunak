

# Generated at 2026-10-24 04:02:58.019391
# Unit test for function monotonic
def test_monotonic():
    assert module_0.monotonic([]) is True
    assert module_0.monotonic([1]) is True
    assert module_0.monotonic([1, 2, 2, 3]) is True
    assert module_0.monotonic([4, 3, 2, 1]) is True
    assert module_0.monotonic([5, 5, 5]) is True
    assert module_0.monotonic([1, 3, 2]) is False
    assert module_0.monotonic([3, 1, 2]) is False

# Generated at 2026-10-24 04:03:02.584937
# Unit test for function monotonic
def test_monotonic():
    assert module_0.monotonic([1, 2, 3, 4]) is True
    assert module_0.monotonic([4, 3, 2, 1]) is True
    assert module_0.monotonic([1, 1, 2, 3]) is True
    assert module_0.monotonic([3, 2, 2, 1]) is True
    assert module_0.monotonic([1, 3, 2, 4]) is False
    assert module_0.monotonic([]) is True
    assert module_0.monotonic([5]) is True

# Generated at 2026-10-24 04:03:07.237975
# Unit test for function monotonic
def test_monotonic():
    assert module_0.monotonic([1, 2, 3, 4]) is True
    assert module_0.monotonic([4, 3, 2, 1]) is True
    assert module_0.monotonic([1, 1, 2, 2]) is True
    assert module_0.monotonic([2, 2, 1, 1]) is True
    assert module_0.monotonic([1, 3, 2]) is False
    assert module_0.monotonic([]) is True
    assert module_0.monotonic([1]) is True

# Generated at 2026-10-24 04:03:12.355467
# Unit test for function monotonic
def test_monotonic():
    assert module_0.monotonic([1, 2, 3, 4]) is True       # Increasing
    assert module_0.monotonic([4, 3, 2, 1]) is True       # Decreasing
    assert module_0.monotonic([1, 1, 2, 2]) is True       # Non-strictly increasing
    assert module_0.monotonic([2, 2, 1, 1]) is True       # Non-strictly decreasing
    assert module_0.monotonic([5]) is True                # Single element
    assert module_0.monotonic([]) is True                 # Empty list
    assert module_0.monotonic([1, 3, 2]) is False         # Not monotonic

# Generated at 2026-10-24 04:03:17.735156
# Unit test for function monotonic
def test_monotonic():
    assert module_0.monotonic([1, 2, 3, 4]) is True       # Increasing
    assert module_0.monotonic([4, 3, 2, 1]) is True       # Decreasing
    assert module_0.monotonic([1, 1, 2, 2]) is True       # Non-decreasing
    assert module_0.monotonic([3, 3, 2, 2]) is True       # Non-increasing
    assert module_0.monotonic([5, 5, 5]) is True          # Constant
    assert module_0.monotonic([1, 3, 2, 4]) is False      # Not monotonic
    assert module_0.monotonic([]) is True                 # Empty list
    assert module_0.monotonic([1]) is True                # Single element