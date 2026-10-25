

# Generated at 2026-10-25 02:23:54.137922
# Unit test for function monotonic

# Generated at 2026-10-25 02:23:56.554843
# Unit test for function monotonic

# Generated at 2026-10-25 02:23:59.125048
# Unit test for function monotonic

# Generated at 2026-10-25 02:24:01.539432
# Unit test for function monotonic

# Generated at 2026-10-25 02:24:03.954032
# Unit test for function monotonic

# Generated at 2026-10-25 02:24:06.540127
# Unit test for function monotonic

# Generated at 2026-10-25 02:24:08.954799
# Unit test for function monotonic

# Generated at 2026-10-25 02:24:11.368757
# Unit test for function monotonic

# Generated at 2026-10-25 02:24:13.916204
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

# Generated at 2026-10-25 02:24:15.235751
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

# Generated at 2026-10-25 02:24:16.556615
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