

# Generated at 2026-10-24 12:55:22.093571
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []  # no evens
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([4, 2, 3]) == [2, 1]  # picks smallest even
    assert module_0.pluck([1, 2, 2, 4]) == [2, 1]  # first occurrence
    assert module_0.pluck([0, 1, 2]) == [0, 0]  # 0 is even
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]  # negatives
    assert module_0.pluck([5, 4, 3, 2, 1]) == [2, 3]

# Generated at 2026-10-24 12:55:23.484290
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []  # no evens
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([4, 2, 3]) == [2, 1]  # picks smallest even
    assert module_0.pluck([1, 2, 2, 4]) == [2, 1]  # first occurrence
    assert module_0.pluck([0, 1, 2]) == [0, 0]  # 0 is even
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]  # negatives
    assert module_0.pluck([5, 4, 3, 2, 1]) == [2, 3]

# Generated at 2026-10-24 12:55:40.523175
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []  # no evens
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([4, 2, 3]) == [2, 1]  # picks smallest even
    assert module_0.pluck([1, 2, 2, 4]) == [2, 1]  # first occurrence
    assert module_0.pluck([0, 1, 2]) == [0, 0]  # 0 is even
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]  # negatives
    assert module_0.pluck([5, 4, 3, 2, 1]) == [2, 3]

# Generated at 2026-10-24 12:55:43.799883
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []  # no evens
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([4, 2, 3]) == [2, 1]  # picks smallest even
    assert module_0.pluck([1, 2, 2, 4]) == [2, 1]  # first occurrence
    assert module_0.pluck([0, 1, 2]) == [0, 0]  # 0 is even
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]  # negatives
    assert module_0.pluck([5, 4, 3, 2, 1]) == [2, 3]

# Generated at 2026-10-24 12:55:46.573313
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []  # no evens
    assert module_0.pluck([2]) == [2, 0]
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([4, 2, 3]) == [2, 1]  # picks smallest even
    assert module_0.pluck([1, 2, 2, 4]) == [2, 1]  # first occurrence
    assert module_0.pluck([0, 1, 2]) == [0, 0]  # 0 is even
    assert module_0.pluck([-4, -2, 3]) == [-4, 0]  # negatives
    assert module_0.pluck([5, 4, 3, 2, 1]) == [2, 3]