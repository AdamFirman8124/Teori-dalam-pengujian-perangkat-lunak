

# Generated at 2026-10-25 03:44:44.679056
# Unit test for function maximum

# Generated at 2026-10-25 03:44:46.053078
# Unit test for function maximum
def test_maximum():
    assert module_0.maximum([1, 2, 3, 4, 5], 3) == [3, 4, 5]
    assert module_0.maximum([5, 1, 3, 2, 4], 2) == [4, 5]
    assert module_0.maximum([-10, -5, -1, -20], 2) == [-5, -1]
    assert module_0.maximum([7], 1) == [7]
    assert module_0.maximum([3, 1, 2], 0) == []
    assert module_0.maximum([9, 9, 9, 9], 2) == [9, 9]
    assert module_0.maximum([10, 20, 30], 5) == [10, 20, 30]
    assert module_0.maximum([2.5, 1.5, 3.5], 1) == [3.5]

# Generated at 2026-10-25 03:44:51.173874
# Unit test for function maximum
def test_maximum():
    assert module_0.maximum([3, 1, 5, 2, 4], 2) == [4, 5]
    assert module_0.maximum([7, 2, 9], 0) == []
    assert module_0.maximum([4, 4, 2, 1], 2) == [4, 4]
    assert module_0.maximum([-5, -1, -3], 2) == [-3, -1]
    assert module_0.maximum([], 0) == []
    assert module_0.maximum([3, 1, 2], 5) == [1, 2, 3]

# Generated at 2026-10-25 03:44:56.810011
# Unit test for function maximum
def test_maximum():
    assert module_0.maximum([1, 4, 2, 3], 2) == [3, 4]
    assert module_0.maximum([5, 1, 5, 2], 3) == [2, 5, 5]
    assert module_0.maximum([-3, -1, -2], 2) == [-2, -1]
    assert module_0.maximum([1, 2, 3], 0) == []
    assert module_0.maximum([], 0) == []

# Generated at 2026-10-25 03:45:02.540320
# Unit test for function maximum
def test_maximum():
    assert module_0.maximum([1, 5, 2, 4, 3], 2) == [4, 5]
    assert module_0.maximum([7, 1, 7, 3], 2) == [7, 7]
    assert module_0.maximum([3, 2, 1], 0) == []
    assert module_0.maximum([3, 2, 1], 3) == [1, 2, 3]
    assert module_0.maximum([], 0) == []

# Generated at 2026-10-25 03:45:08.176545
# Unit test for function maximum
def test_maximum():
    assert module_0.maximum([1, 2, 3, 4, 5], 2) == [4, 5]
    assert module_0.maximum([-5, -1, -3, -2], 2) == [-2, -1]
    assert module_0.maximum([4, 4, 2, 1], 2) == [4, 4]
    assert module_0.maximum([3, 1, 2], 0) == []
    assert module_0.maximum([3, 1, 2], 3) == [1, 2, 3]