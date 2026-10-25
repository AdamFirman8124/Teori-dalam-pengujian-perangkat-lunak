

# Generated at 2026-10-24 12:19:32.924662
# Unit test for function monotonic
def test_monotonic():
    # Increasing
    assert module_0.monotonic([1, 2, 4, 20]) == True
    # Decreasing
    assert module_0.monotonic([4, 1, 1, 0, -10]) == True
    # Increasing with duplicates
    assert module_0.monotonic([1, 1, 1, 1]) == True
    # Not monotonic
    assert module_0.monotonic([1, 2, 3, 2, 1]) == False
    # Empty list
    assert module_0.monotonic([]) == True
    # Single element
    assert module_0.monotonic([5]) == True
    # Two elements
    assert module_0.monotonic([3, 7]) == True
    assert module_0.monotonic([7, 3]) == True
    # Negative numbers
    assert module_0.monotonic([-5, -3, -1]) == True
    assert module_0.monotonic([-1, -5, -3]) == False
    print("All tests passed!")

# Generated at 2026-10-24 12:19:35.350774
# Unit test for function monotonic

# Generated at 2026-10-24 12:19:48.166865
# Unit test for function monotonic
def test_monotonic():assert module_0.monotonic([1, 2, 3]) == True

# Generated at 2026-10-24 12:19:49.600817
# Unit test for function monotonic
def test_monotonic():
    # Increasing
    assert module_0.monotonic([1, 2, 4, 20]) == True
    # Decreasing
    assert module_0.monotonic([4, 1, 1, 0, -10]) == True
    # Increasing with duplicates
    assert module_0.monotonic([1, 1, 1, 1]) == True
    # Not monotonic
    assert module_0.monotonic([1, 2, 3, 2, 1]) == False
    # Empty list
    assert module_0.monotonic([]) == True
    # Single element
    assert module_0.monotonic([5]) == True
    # Two elements
    assert module_0.monotonic([3, 7]) == True
    assert module_0.monotonic([7, 3]) == True
    # Negative numbers
    assert module_0.monotonic([-5, -3, -1]) == True
    assert module_0.monotonic([-1, -5, -3]) == False
    print("All tests passed!")

# Generated at 2026-10-24 12:19:50.916959
# Unit test for function monotonic
def test_monotonic():
    # Increasing
    assert module_0.monotonic([1, 2, 4, 20]) == True
    # Decreasing
    assert module_0.monotonic([4, 1, 1, 0, -10]) == True
    # Increasing with duplicates
    assert module_0.monotonic([1, 1, 1, 1]) == True
    # Not monotonic
    assert module_0.monotonic([1, 2, 3, 2, 1]) == False
    # Empty list
    assert module_0.monotonic([]) == True
    # Single element
    assert module_0.monotonic([5]) == True
    # Two elements
    assert module_0.monotonic([3, 7]) == True
    assert module_0.monotonic([7, 3]) == True
    # Negative numbers
    assert module_0.monotonic([-5, -3, -1]) == True
    assert module_0.monotonic([-1, -5, -3]) == False
    print("All tests passed!")

# Generated at 2026-10-24 12:19:52.295961
# Unit test for function monotonic
def test_monotonic():
    # Increasing
    assert module_0.monotonic([1, 2, 4, 20]) == True
    # Decreasing
    assert module_0.monotonic([4, 1, 1, 0, -10]) == True
    # Increasing with duplicates
    assert module_0.monotonic([1, 1, 1, 1]) == True
    # Not monotonic
    assert module_0.monotonic([1, 2, 3, 2, 1]) == False
    # Empty list
    assert module_0.monotonic([]) == True
    # Single element
    assert module_0.monotonic([5]) == True
    # Two elements
    assert module_0.monotonic([3, 7]) == True
    assert module_0.monotonic([7, 3]) == True
    # Negative numbers
    assert module_0.monotonic([-5, -3, -1]) == True
    assert module_0.monotonic([-1, -5, -3]) == False
    print("All tests passed!")