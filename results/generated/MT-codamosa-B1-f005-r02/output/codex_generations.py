

# Generated at 2026-10-23 19:15:00.271945
# Unit test for function intersperse
def test_intersperse():
    assert module_0.intersperse([], 0) == []
    assert module_0.intersperse([1], 0) == [1]
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert module_0.intersperse([-1, 5, 10], 99) == [-1, 99, 5, 99, 10]

# Generated at 2026-10-23 19:15:12.004546
# Unit test for function intersperse
def test_intersperse():
    assert module_0.intersperse([], 0) == []
    assert module_0.intersperse([1], 0) == [1]
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert module_0.intersperse([5, 10, 15], -1) == [5, -1, 10, -1, 15]
    assert module_0.intersperse([-2, 0, 2], 99) == [-2, 99, 0, 99, 2]

# Generated at 2026-10-23 19:15:23.063421
# Unit test for function intersperse
def test_intersperse():
    assert module_0.intersperse([], 0) == []
    assert module_0.intersperse([1], 0) == [1]
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert module_0.intersperse([1, 2, 3], 99) == [1, 99, 2, 99, 3]
    assert module_0.intersperse([-1, 0, 1], -5) == [-1, -5, 0, -5, 1]

# Generated at 2026-10-23 19:15:37.298843
# Unit test for function intersperse
def test_intersperse():
    assert module_0.intersperse([], 0) == []
    assert module_0.intersperse([1], 0) == [1]
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert module_0.intersperse([5, 10, 15], -1) == [5, -1, 10, -1, 15]

# Generated at 2026-10-23 19:15:50.303008
# Unit test for function intersperse
def test_intersperse():
    assert module_0.intersperse([], 0) == []
    assert module_0.intersperse([1], 0) == [1]
    assert module_0.intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert module_0.intersperse([10, 20], -1) == [10, -1, 20]