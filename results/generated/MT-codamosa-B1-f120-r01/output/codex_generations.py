

# Generated at 2026-10-25 01:01:19.850923
# Unit test for function maximum

# Generated at 2026-10-25 01:01:22.266729
# Unit test for function maximum

# Generated at 2026-10-25 01:01:24.681527
# Unit test for function maximum

# Generated at 2026-10-25 01:01:27.098000
# Unit test for function maximum

# Generated at 2026-10-25 01:01:29.513139
# Unit test for function maximum

# Generated at 2026-10-25 01:01:31.927347
# Unit test for function maximum

# Generated at 2026-10-25 01:01:34.342008
# Unit test for function maximum

# Generated at 2026-10-25 01:01:36.756076
# Unit test for function maximum

# Generated at 2026-10-25 01:01:42.710967
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

# Generated at 2026-10-25 01:01:48.548017
# Unit test for function maximum
def test_maximum():
    assert module_0.maximum([1, 5, 3, 2, 4], 3) == [3, 4, 5]
    assert module_0.maximum([-5, -1, -3], 2) == [-3, -1]
    assert module_0.maximum([4, 1, 4, 2], 3) == [2, 4, 4]
    assert module_0.maximum([1, 2, 3], 0) == []
    assert module_0.maximum([], 0) == []

# Generated at 2026-10-25 01:01:54.180685
# Unit test for function maximum
def test_maximum():
    assert module_0.maximum([3, 1, 5, 2, 4], 3) == [3, 4, 5]
    assert module_0.maximum([10, 7, 8], 1) == [10]
    assert module_0.maximum([4, 2, 4, 1], 2) == [4, 4]
    assert module_0.maximum([1, 2, 3], 0) == []