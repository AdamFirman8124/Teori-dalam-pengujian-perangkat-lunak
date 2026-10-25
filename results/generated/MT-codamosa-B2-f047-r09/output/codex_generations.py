

# Generated at 2026-10-25 03:43:36.037853
# Unit test for function median
def test_median():
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([4, 1, 3, 2]) == 2.5
    assert module_0.median([7]) == 7
    assert module_0.median([-5, -1, -3]) == -3
    assert module_0.median([-2, 0, 2, 4]) == 1.0

    # Verify that median does not modify the original list
    values = [3, 1, 2]
    module_0.median(values)
    assert values == [3, 1, 2]

# Generated at 2026-10-25 03:43:40.108776
# Unit test for function median
def test_median():
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([4, 1, 3, 2]) == 2.5
    assert module_0.median([-1, -3, -2]) == -2
    assert module_0.median([5]) == 5
    assert module_0.median([2, 2, 2, 2]) == 2.0

    # Ensure the original list is not modified
    values = [3, 1, 2]
    module_0.median(values)
    assert values == [3, 1, 2]

# Generated at 2026-10-25 03:43:45.571068
# Unit test for function median
def test_median():
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([4, 1, 3, 2]) == 2.5
    assert module_0.median([7]) == 7
    assert module_0.median([-1, -3, -2]) == -2
    assert module_0.median([1, 1, 2, 2]) == 1.5

# Generated at 2026-10-25 03:43:50.655549
# Unit test for function median
def test_median():
    assert module_0.median([1, 2, 3]) == 2
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([5, 1, 3]) == 3
    assert module_0.median([-5, -1, -3, -2]) == -2.5
    assert module_0.median([7]) == 7
    assert module_0.median([2, 2, 2, 2]) == 2.0

# Generated at 2026-10-25 03:43:57.622931
# Unit test for function median
def test_median():
    assert module_0.median([3, 1, 2]) == 2             # Odd number of elements
    assert module_0.median([4, 1, 3, 2]) == 2.5        # Even number of elements
    assert module_0.median([7]) == 7                   # Single element
    assert module_0.median([-5, -1, -3]) == -3         # Negative values
    assert module_0.median([1, 2, 2, 3]) == 2.0        # Duplicate values

    # Ensure the original list is not modified
    values = [3, 1, 2]
    module_0.median(values)
    assert values == [3, 1, 2]