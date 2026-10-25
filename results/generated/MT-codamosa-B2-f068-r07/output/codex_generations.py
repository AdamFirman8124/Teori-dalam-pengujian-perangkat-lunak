

# Generated at 2026-10-24 22:37:43.904425
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 3, 0]) == [0, 1]
    assert module_0.pluck([-3, -4, -2, 1]) == [-4, 1]
    assert module_0.pluck([2, 2, 4]) == [2, 0]

# Generated at 2026-10-24 22:37:49.331350
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([1, 2, 3, 4]) == [2, 1]
    assert module_0.pluck([4, 2, 8, 2]) == [2, 1]
    assert module_0.pluck([5, 0, 2, 4]) == [0, 1]
    assert module_0.pluck([-1, -4, -2, 3]) == [-4, 1]
    assert module_0.pluck([2]) == [2, 0]

# Generated at 2026-10-24 22:37:55.890118
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3, 0]) == [0, 3]
    assert module_0.pluck([1, 2, 2, 3]) == [2, 1]
    assert module_0.pluck([-1, -4, -2, 3]) == [-4, 1]

# Generated at 2026-10-24 22:38:00.903214
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([4, 2, 8, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3, 2]) == [2, 1]  # First occurrence
    assert module_0.pluck([7, -4, 2, -6]) == [-6, 3]
    assert module_0.pluck([0, 3, 2]) == [0, 0]
    assert module_0.pluck([8]) == [8, 0]

# Generated at 2026-10-24 22:38:07.046904
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([4, 2, 3, 1, 5]) == [2, 1]
    assert module_0.pluck([1, 2, 4, 2]) == [2, 1]
    assert module_0.pluck([7, 8, 5, 6, 4]) == [4, 4]
    assert module_0.pluck([0, 2, 4]) == [0, 0]
    assert module_0.pluck([-3, -4, -2, 1]) == [-4, 1]