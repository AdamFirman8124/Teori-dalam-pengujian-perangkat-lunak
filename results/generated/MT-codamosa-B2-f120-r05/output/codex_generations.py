

# Generated at 2026-10-25 02:34:53.062245
# Unit test for function maximum
def test_maximum():
    assert module_0.maximum([1, 5, 3, 2, 4], 2) == [4, 5]
    assert module_0.maximum([-5, -1, -3], 2) == [-3, -1]
    assert module_0.maximum([3, 3, 1, 2], 2) == [3, 3]
    assert module_0.maximum([1, 2, 3], 0) == []
    assert module_0.maximum([], 0) == []
    assert module_0.maximum([3, 1, 2], 3) == [1, 2, 3]

# Generated at 2026-10-25 02:34:58.693497
# Unit test for function maximum
def test_maximum():
    assert module_0.maximum([1, 3, 2, 5, 4], 3) == [3, 4, 5]
    assert module_0.maximum([7, 2, 9], 1) == [9]
    assert module_0.maximum([4, 4, 2, 4], 2) == [4, 4]
    assert module_0.maximum([-5, -1, -3], 2) == [-3, -1]
    assert module_0.maximum([1, 2, 3], 0) == []
    assert module_0.maximum([], 0) == []

# Generated at 2026-10-25 02:35:04.429048
# Unit test for function maximum
def test_maximum():
    assert module_0.maximum([1, 3, 2, 5, 4], 3) == [3, 4, 5]
    assert module_0.maximum([4, 1, 4, 2], 2) == [4, 4]
    assert module_0.maximum([-5, -1, -3], 2) == [-3, -1]
    assert module_0.maximum([1, 2, 3], 0) == []
    assert module_0.maximum([], 0) == []
    assert module_0.maximum([7], 1) == [7]

# Generated at 2026-10-25 02:35:09.957936
# Unit test for function maximum
def test_maximum():
    assert module_0.maximum([1, 5, 2, 4, 3], 3) == [3, 4, 5]
    assert module_0.maximum([7, 2, 9], 1) == [9]
    assert module_0.maximum([4, 1, 3], 0) == []
    assert module_0.maximum([-5, -1, -3], 2) == [-3, -1]
    assert module_0.maximum([2, 2, 1], 2) == [2, 2]

# Generated at 2026-10-25 02:35:14.778088
# Unit test for function maximum
def test_maximum():
    assert module_0.maximum([1, 3, 2, 5, 4], 3) == [3, 4, 5]
    assert module_0.maximum([7, 2, 7, 1], 2) == [7, 7]
    assert module_0.maximum([4, 1, 3], 0) == []
    assert module_0.maximum([-5, -1, -3], 2) == [-3, -1]
    assert module_0.maximum([2, 1], 5) == [1, 2]