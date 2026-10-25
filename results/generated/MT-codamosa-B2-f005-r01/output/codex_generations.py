

# Generated at 2026-10-23 19:44:18.435845
# Unit test for function intersperse
def test_intersperse():
    assert module_0.intersperse([], 0) == []
    assert module_0.intersperse([1], 0) == [1]
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert module_0.intersperse([10, 20, 30], -1) == [10, -1, 20, -1, 30]
    assert module_0.intersperse([-2, 0, 2], 99) == [-2, 99, 0, 99, 2]

# Generated at 2026-10-23 19:44:31.144414
# Unit test for function intersperse
def test_intersperse():
    assert module_0.intersperse([], 0) == []
    assert module_0.intersperse([1], 0) == [1]
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]

# Generated at 2026-10-23 19:44:42.510391
# Unit test for function intersperse
def test_intersperse():
    assert module_0.intersperse([], 0) == []
    assert module_0.intersperse([1], 0) == [1]
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]
    assert module_0.intersperse([-2, 0, 5], 99) == [-2, 99, 0, 99, 5]

# Generated at 2026-10-23 19:44:53.003878
# Unit test for function intersperse
def test_intersperse():
    assert module_0.intersperse([], 0) == []
    assert module_0.intersperse([1], 0) == [1]
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert module_0.intersperse([1, 2, 3], -1) == [1, -1, 2, -1, 3]
    assert module_0.intersperse([5, 5], 5) == [5, 5, 5]

# Generated at 2026-10-23 19:45:03.511854
# Unit test for function intersperse
def test_intersperse():
    assert module_0.intersperse([], 0) == []
    assert module_0.intersperse([1], 0) == [1]
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert module_0.intersperse([-1, 5, 10], 99) == [-1, 99, 5, 99, 10]