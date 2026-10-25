

# Generated at 2026-10-25 00:29:54.993729
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 3, 2]) == [2, 1]
    assert module_0.pluck([6, 4, 8, 2]) == [2, 3]
    assert module_0.pluck([0, 1, 2]) == [0, 0]
    assert module_0.pluck([-3, -4, -2]) == [-4, 1]
    assert module_0.pluck([2]) == [2, 0]

# Generated at 2026-10-25 00:29:57.512422
# Unit test for function pluck

# Generated at 2026-10-25 00:29:59.929774
# Unit test for function pluck

# Generated at 2026-10-25 00:30:11.570866
# Unit test for function pluck
def test_pluck():assert module_0.pluck([4, 2, 3]) == [2, 1]

# Generated at 2026-10-25 00:30:17.244420
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([4, 2, 8, 2]) == [2, 1]
    assert module_0.pluck([1, 6, 4, 7]) == [4, 2]
    assert module_0.pluck([0, 3, 2]) == [0, 0]
    assert module_0.pluck([-3, -4, -2, 5]) == [-4, 1]
    assert module_0.pluck([7, 8, 5, 8]) == [8, 1]

# Generated at 2026-10-25 00:30:21.820543
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([1, 2, 3]) == [2, 1]
    assert module_0.pluck([4, 2, 8, 3]) == [2, 1]
    assert module_0.pluck([5, 4, 2, 2, 7]) == [2, 2]  # First occurrence
    assert module_0.pluck([0, 1, 2]) == [0, 0]
    assert module_0.pluck([-1, -4, -2, 3]) == [-4, 1]

# Generated at 2026-10-25 00:30:26.632684
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([4, 2, 8, 3]) == [2, 1]
    assert module_0.pluck([5, 4, 3, 2, 1]) == [2, 3]
    assert module_0.pluck([6, 2, 4, 2]) == [2, 1]  # First occurrence
    assert module_0.pluck([-3, -4, -2, 1]) == [-4, 1]