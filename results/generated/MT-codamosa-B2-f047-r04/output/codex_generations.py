

# Generated at 2026-10-24 06:30:44.072865
# Unit test for function median
def test_median():
    assert module_0.median([1, 2, 3]) == 2
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([4, 1, 3, 2]) == 2.5
    assert module_0.median([5]) == 5
    assert module_0.median([-3, -1, -2]) == -2

# Generated at 2026-10-24 06:30:49.188867
# Unit test for function median
def test_median():
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([4, 1, 3, 2]) == 2.5
    assert module_0.median([7]) == 7
    assert module_0.median([-5, -1, -3]) == -3
    assert module_0.median([2, 2, 2, 2]) == 2.0

# Generated at 2026-10-24 06:30:55.790946
# Unit test for function median
def test_median():
    assert module_0.median([1, 2, 3]) == 2
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([5]) == 5
    assert module_0.median([7, 1, 3]) == 3
    assert module_0.median([-5, -1, -3, -2]) == -2.5
    assert module_0.median([2, 2, 2, 2]) == 2.0

# Generated at 2026-10-24 06:31:00.841061
# Unit test for function median
def test_median():
    assert module_0.median([3, 1, 2]) == 2
    assert module_0.median([4, 1, 3, 2]) == 2.5
    assert module_0.median([5]) == 5
    assert module_0.median([-1, -3, -2]) == -2
    assert module_0.median([1.5, 2.5]) == 2.0

# Generated at 2026-10-24 06:31:05.881284
# Unit test for function median
def test_median():
    assert module_0.median([1, 2, 3]) == 2
    assert module_0.median([1, 2, 3, 4]) == 2.5
    assert module_0.median([5, 1, 3]) == 3
    assert module_0.median([-5, -1, -3, -2]) == -2.5
    assert module_0.median([7]) == 7
    assert module_0.median([2, 2, 2, 2]) == 2.0