

# Generated at 2026-10-24 21:41:38.514710
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 4, 2]) == [2, 1]
    assert module_0.pluck([8, 6, 4, 2]) == [2, 3]
    assert module_0.pluck([0, 1, 2]) == [0, 0]
    assert module_0.pluck([-1, -4, -2]) == [-4, 1]

# Generated at 2026-10-24 21:41:43.529499
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([4, 2, 8, 3, 2]) == [2, 1]
    assert module_0.pluck([1, 0, 3, 2]) == [0, 1]
    assert module_0.pluck([-3, -2, -4, 1]) == [-4, 2]
    assert module_0.pluck([7, 6, 5, 4, 3, 2]) == [2, 5]

# Generated at 2026-10-24 21:41:49.365618
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3, 0]) == [0, 3]
    assert module_0.pluck([6, 4, 4, 2, 2]) == [2, 3]
    assert module_0.pluck([-3, -4, -2, 1]) == [-4, 1]

# Generated at 2026-10-24 21:41:54.378600
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([4, 2, 8, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 4, 2]) == [2, 1]
    assert module_0.pluck([7, 6, 5, 4, 3, 2]) == [2, 5]
    assert module_0.pluck([0, 2, 4]) == [0, 0]
    assert module_0.pluck([-3, -2, -4, 1]) == [-4, 2]

# Generated at 2026-10-24 21:41:59.779675
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([1, 2, 3, 4]) == [2, 1]
    assert module_0.pluck([4, 2, 6, 2]) == [2, 1]  # First occurrence
    assert module_0.pluck([8]) == [8, 0]
    assert module_0.pluck([7, -4, -2, 3]) == [-4, 1]