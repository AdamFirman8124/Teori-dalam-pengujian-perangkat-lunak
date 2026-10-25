

# Generated at 2026-10-24 22:02:59.132642
# Unit test for function maximum
def test_maximum():
    # k = 0
    assert module_0.maximum([], 0) == []
    assert module_0.maximum([1, 2, 3], 0) == []

    # basic cases
    assert module_0.maximum([1, 2, 3, 4, 5], 1) == [5]
    assert module_0.maximum([1, 2, 3, 4, 5], 2) == [4, 5]
    assert module_0.maximum([5, 4, 3, 2, 1], 3) == [3, 4, 5]

    # duplicates
    assert module_0.maximum([1, 1, 1, 1], 2) == [1, 1]

    # negative numbers
    assert module_0.maximum([-5, -1, -3, 0, 2], 2) == [0, 2]

    # k == len(arr)
    assert module_0.maximum([1, 2, 3], 3) == [1, 2, 3]

    # k > len(arr) returns whole sorted array
    assert module_0.maximum([1, 2], 5) == [1, 2]
    assert module_0.maximum([], 3) == []

# Generated at 2026-10-24 22:03:00.501858
# Unit test for function maximum
def test_maximum():
    # k = 0
    assert module_0.maximum([], 0) == []
    assert module_0.maximum([1, 2, 3], 0) == []

    # basic cases
    assert module_0.maximum([1, 2, 3, 4, 5], 1) == [5]
    assert module_0.maximum([1, 2, 3, 4, 5], 2) == [4, 5]
    assert module_0.maximum([5, 4, 3, 2, 1], 3) == [3, 4, 5]

    # duplicates
    assert module_0.maximum([1, 1, 1, 1], 2) == [1, 1]

    # negative numbers
    assert module_0.maximum([-5, -1, -3, 0, 2], 2) == [0, 2]

    # k == len(arr)
    assert module_0.maximum([1, 2, 3], 3) == [1, 2, 3]

    # k > len(arr) returns whole sorted array
    assert module_0.maximum([1, 2], 5) == [1, 2]
    assert module_0.maximum([], 3) == []

# Generated at 2026-10-24 22:03:01.868416
# Unit test for function maximum
def test_maximum():
    # k = 0
    assert module_0.maximum([], 0) == []
    assert module_0.maximum([1, 2, 3], 0) == []

    # basic cases
    assert module_0.maximum([1, 2, 3, 4, 5], 1) == [5]
    assert module_0.maximum([1, 2, 3, 4, 5], 2) == [4, 5]
    assert module_0.maximum([5, 4, 3, 2, 1], 3) == [3, 4, 5]

    # duplicates
    assert module_0.maximum([1, 1, 1, 1], 2) == [1, 1]

    # negative numbers
    assert module_0.maximum([-5, -1, -3, 0, 2], 2) == [0, 2]

    # k == len(arr)
    assert module_0.maximum([1, 2, 3], 3) == [1, 2, 3]

    # k > len(arr) returns whole sorted array
    assert module_0.maximum([1, 2], 5) == [1, 2]
    assert module_0.maximum([], 3) == []

# Generated at 2026-10-24 22:03:03.275065
# Unit test for function maximum
def test_maximum():
    # k = 0
    assert module_0.maximum([], 0) == []
    assert module_0.maximum([1, 2, 3], 0) == []

    # basic cases
    assert module_0.maximum([1, 2, 3, 4, 5], 1) == [5]
    assert module_0.maximum([1, 2, 3, 4, 5], 2) == [4, 5]
    assert module_0.maximum([5, 4, 3, 2, 1], 3) == [3, 4, 5]

    # duplicates
    assert module_0.maximum([1, 1, 1, 1], 2) == [1, 1]

    # negative numbers
    assert module_0.maximum([-5, -1, -3, 0, 2], 2) == [0, 2]

    # k == len(arr)
    assert module_0.maximum([1, 2, 3], 3) == [1, 2, 3]

    # k > len(arr) returns whole sorted array
    assert module_0.maximum([1, 2], 5) == [1, 2]
    assert module_0.maximum([], 3) == []

# Generated at 2026-10-24 22:03:04.661775
# Unit test for function maximum
def test_maximum():
    # k = 0
    assert module_0.maximum([], 0) == []
    assert module_0.maximum([1, 2, 3], 0) == []

    # basic cases
    assert module_0.maximum([1, 2, 3, 4, 5], 1) == [5]
    assert module_0.maximum([1, 2, 3, 4, 5], 2) == [4, 5]
    assert module_0.maximum([5, 4, 3, 2, 1], 3) == [3, 4, 5]

    # duplicates
    assert module_0.maximum([1, 1, 1, 1], 2) == [1, 1]

    # negative numbers
    assert module_0.maximum([-5, -1, -3, 0, 2], 2) == [0, 2]

    # k == len(arr)
    assert module_0.maximum([1, 2, 3], 3) == [1, 2, 3]

    # k > len(arr) returns whole sorted array
    assert module_0.maximum([1, 2], 5) == [1, 2]
    assert module_0.maximum([], 3) == []