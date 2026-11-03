

# Generated at 2026-11-02 22:03:52.358350
# Unit test for function monotonic
def test_monotonic():
    # Increasing sequences
    assert module_0.monotonic([1, 2, 4, 20]) == True
    assert module_0.monotonic([1, 20, 4, 10]) == False
    assert module_0.monotonic([4, 1, 1, 0, -10]) == True
    assert module_0.monotonic([1, 1, 1, 1]) == True
    assert module_0.monotonic([-1, 0, 1, 2]) == True
    assert module_0.monotonic([5, 4, 3, 2, 1]) == True
    assert module_0.monotonic([1, 3, 2]) == False
    assert module_0.monotonic([]) == True
    assert module_0.monotonic([42]) == True
    assert module_0.monotonic([2, 2, 3, 3]) == True
    assert module_0.monotonic([3, 3, 2, 2]) == True
    assert module_0.monotonic([1, 2, 3, 2]) == False
    assert module_0.monotonic([10, 9, 9, 8]) == True
    assert module_0.monotonic([0, -1, -2, -3]) == True
    assert module_0.monotonic([1.5, 2.5, 3.5]) == True
    assert module_0.monotonic([3.5, 2.5, 1.5]) == True
    assert module_0.monotonic([1.5, 3.5, 2.5]) == False

test_monotonic()

# Generated at 2026-11-02 22:07:08.043353
# Unit test for function monotonic
def test_monotonic():
    # Increasing lists
    assert module_0.monotonic([1, 2, 4, 20]) == True
    assert module_0.monotonic([1, 1, 2, 3]) == True  # non-strict increasing
    assert module_0.monotonic([0, 0, 0, 0]) == True  # all equal

    # Decreasing lists
    assert module_0.monotonic([20, 4, 2, 1]) == True
    assert module_0.monotonic([5, 5, 3, 1]) == True  # non-strict decreasing

    # Non-monotonic lists
    assert module_0.monotonic([1, 20, 4, 10]) == False
    assert module_0.monotonic([4, 1, 0, -10]) == True  # strictly decreasing
    assert module_0.monotonic([1, 3, 2]) == False
    assert module_0.monotonic([3, 1, 2]) == False

    # Edge cases
    assert module_0.monotonic([]) == True           # empty list
    assert module_0.monotonic([7]) == True          # single element
    assert module_0.monotonic([2, 2]) == True       # two equal elements
    assert module_0.monotonic([1, 2]) == True       # two increasing
    assert module_0.monotonic([2, 1]) == True       # two decreasing

    # Negative numbers and floats
    assert module_0.monotonic([-5, -3, 0, 2]) == True
    assert module_0.monotonic([-1, -5, -3]) == False
    assert module_0.monotonic([1.5, 2.5, 2.5, 3.0]) == True
    assert module_0.monotonic([3.0, 2.5, 2.5, 1.5]) == True
    assert module_0.monotonic([1.5, 3.0, 2.5]) == False

    # Strings
    assert module_0.monotonic(['a', 'b', 'c']) == True
    assert module_0.monotonic(['c', 'b', 'a']) == True
    assert module_0.monotonic(['a', 'c', 'b']) == False

# Generated at 2026-11-02 22:09:30.183300
# Unit test for function monotonic
def test_monotonic():
    # Monotonically increasing
    assert module_0.monotonic([1, 2, 4, 20]) == True
    # Monotonically decreasing
    assert module_0.monotonic([20, 4, 2, 1]) == True
    # Not monotonic
    assert module_0.monotonic([1, 20, 4, 10]) == False
    # Non-strict increasing (duplicates allowed)
    assert module_0.monotonic([1, 2, 2, 3]) == True
    # Non-strict decreasing (duplicates allowed)
    assert module_0.monotonic([5, 4, 4, 1]) == True
    # Empty list is monotonic
    assert module_0.monotonic([]) == True
    # Single element is monotonic
    assert module_0.monotonic([7]) == True
    # Two elements increasing
    assert module_0.monotonic([1, 2]) == True
    # Two elements decreasing
    assert module_0.monotonic([2, 1]) == True
    # All equal elements
    assert module_0.monotonic([3, 3, 3, 3]) == True
    # Negative numbers increasing
    assert module_0.monotonic([-5, -3, 0, 2]) == True
    # Negative numbers not monotonic
    assert module_0.monotonic([-1, -5, 0]) == False
    # Mixed with plateau then rise
    assert module_0.monotonic([1, 1, 2, 2, 3]) == True
    # Rise then fall is not monotonic
    assert module_0.monotonic([1, 2, 3, 2]) == False
    # Floats
    assert module_0.monotonic([1.5, 2.5, 2.5, 3.7]) == True
    assert module_0.monotonic([3.7, 2.5, 2.5, 1.5]) == True
    assert module_0.monotonic([1.5, 3.7, 2.5]) == False