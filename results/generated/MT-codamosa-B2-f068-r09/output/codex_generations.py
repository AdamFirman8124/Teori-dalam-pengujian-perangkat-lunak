

# Generated at 2026-10-24 19:59:20.245754
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([4, 2, 8, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 3, 2]) == [0, 1]
    assert module_0.pluck([6, 4, 4, 8]) == [4, 1]  # First occurrence
    assert module_0.pluck([-3, -2, -4, 1]) == [-4, 2]

# Generated at 2026-10-24 19:59:25.140240
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([4, 2, 8, 6]) == [2, 1]
    assert module_0.pluck([1, 2, 3, 2]) == [2, 1]
    assert module_0.pluck([5, 0, 2, 4]) == [0, 1]
    assert module_0.pluck([-3, -4, -2, 1]) == [-4, 1]
    assert module_0.pluck([8]) == [8, 0]


test_pluck()
print("All tests passed.")

# Generated at 2026-10-24 19:59:30.671109
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([4, 2, 8, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 2, 0]) == [0, 1]
    assert module_0.pluck([7, -2, 4, -6]) == [-6, 3]
    assert module_0.pluck([2, 2, 4]) == [2, 0]


test_pluck()
print("All tests passed.")

# Generated at 2026-10-24 19:59:35.656635
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5]) == []
    assert module_0.pluck([4, 2, 3]) == [2, 1]
    assert module_0.pluck([1, 2, 2, 4]) == [2, 1]
    assert module_0.pluck([7, 6, 5, 4, 2]) == [2, 4]
    assert module_0.pluck([-1, -4, -2, 3]) == [-4, 1]
    assert module_0.pluck([0, 3, 2]) == [0, 0]

# Generated at 2026-10-24 19:59:40.596798
# Unit test for function pluck
def test_pluck():
    assert module_0.pluck([]) == []
    assert module_0.pluck([1, 3, 5, 7]) == []
    assert module_0.pluck([4, 2, 8, 3]) == [2, 1]
    assert module_0.pluck([5, 0, 3, 2]) == [0, 1]
    assert module_0.pluck([6, 3, 6, 2, 2]) == [2, 3]
    assert module_0.pluck([-3, -4, -2, 1]) == [-4, 1]