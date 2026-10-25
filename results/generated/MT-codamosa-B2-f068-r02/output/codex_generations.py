

# Generated at 2026-10-24 06:20:38.887046
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([1, 2, 3, 4]) == [2, 1]
    assert module_0.pluck([4, 2, 8, 2]) == [2, 1]  # First occurrence
    assert module_0.pluck([7, 6, 5, 4, 3, 2, 1]) == [2, 5]
    assert module_0.pluck([-1, -4, -2, 3]) == [-4, 1]
    assert module_0.pluck([0, 1, 2]) == [0, 0]

# Generated at 2026-10-24 06:20:44.719367
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3, 2]) == [2, 1]
    assert module_0.pluck([5, 0, 2]) == [0, 1]
    assert module_0.pluck([-3, -4, -2]) == [-4, 1]

# Generated at 2026-10-24 06:20:50.103702
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([4, 2, 8, 2]) == [2, 1]
    assert module_0.pluck([7, 0, 4, 2]) == [0, 1]
    assert module_0.pluck([-3, -4, -2, 1]) == [-4, 1]
    assert module_0.pluck([2]) == [2, 0]

# Generated at 2026-10-24 06:20:55.372630
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([4, 2, 8, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 2, 4]) == [0, 1]
    assert module_0.pluck([6, 4, 4, 2, 2]) == [2, 3]
    assert module_0.pluck([-3, -4, -2, 1]) == [-4, 1]
    assert module_0.pluck([1, 8, 3, 8]) == [8, 1]

# Generated at 2026-10-24 06:21:02.536702
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([4, 2, 8, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 2, 0]) == [0, 1]
    assert module_0.pluck([7, -2, 4, -6]) == [-6, 3]
    assert module_0.pluck([2, 2, 4]) == [2, 0]