

# Generated at 2026-10-24 20:24:23.049043
# Unit test for function common
def test_common():
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert module_0.common([1, 2, 2, 3], [2, 2, 4]) == [2]
    assert module_0.common([1, 2], [3, 4]) == []
    assert module_0.common([], [1, 2]) == []
    assert module_0.common([3, 1, 2], [2, 3, 1]) == [1, 2, 3]

# Generated at 2026-10-24 20:24:33.198444
# Unit test for function common
def test_common():
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert module_0.common([1, 1, 2, 3], [1, 3, 3]) == [1, 3]
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([5, 2, 1], [3, 2, 1]) == [1, 2]

# Generated at 2026-10-24 20:24:43.323972
# Unit test for function common
def test_common():
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert module_0.common([1, 1, 2, 3], [2, 3, 3]) == [2, 3]
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2], []) == []
    assert module_0.common([1, 2], [3, 4]) == []

# Generated at 2026-10-24 20:24:52.539888
# Unit test for function common
def test_common():
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert module_0.common([1, 1, 2, 3], [1, 2, 2]) == [1, 2]
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([5, 4, 3], [3, 4, 5]) == [3, 4, 5]

# Generated at 2026-10-24 20:25:03.189982
# Unit test for function common
def test_common():
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert module_0.common([1, 1, 2, 3], [1, 3, 3]) == [1, 3]
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common(["b", "a"], ["a", "c"]) == ["a"]