

# Generated at 2026-10-24 12:46:13.280631
# Unit test for function common
def test_common():
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert module_0.common([1, 1, 2], [1, 1, 3]) == [1]
    assert module_0.common([1, 2], [3, 4]) == []
    assert module_0.common([], [1, 2]) == []
    assert module_0.common([], []) == []
    assert module_0.common([-3, -1, 2], [-1, 2, 5]) == [-1, 2]

# Generated at 2026-10-24 12:46:18.038291
# Unit test for function common
def test_common():
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert module_0.common([1, 1, 2, 3], [1, 1, 3]) == [1, 3]
    assert module_0.common([1, 2], [3, 4]) == []
    assert module_0.common([], [1, 2]) == []
    assert module_0.common([-3, -1, 0, 2], [-1, 0, 4]) == [-1, 0]

# Generated at 2026-10-24 12:46:27.059883
# Unit test for function common
def test_common():
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert module_0.common([3, 2, 1], [3, 2]) == [2, 3]  # sorted
    assert module_0.common([1, 2], [3, 4]) == []  # no overlap
    assert module_0.common([], [1, 2]) == []
    assert module_0.common([1, 2], []) == []
    assert module_0.common([], []) == []
    assert module_0.common([1, 1, 2, 2], [1, 1, 3]) == [1]  # deduplicated
    assert module_0.common(['a', 'b', 'c'], ['b', 'c', 'd']) == ['b', 'c']

# Generated at 2026-10-24 12:46:28.481798
# Unit test for function common
def test_common():
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert module_0.common([3, 2, 1], [3, 2]) == [2, 3]  # sorted
    assert module_0.common([1, 2], [3, 4]) == []  # no overlap
    assert module_0.common([], [1, 2]) == []
    assert module_0.common([1, 2], []) == []
    assert module_0.common([], []) == []
    assert module_0.common([1, 1, 2, 2], [1, 1, 3]) == [1]  # deduplicated
    assert module_0.common(['a', 'b', 'c'], ['b', 'c', 'd']) == ['b', 'c']

# Generated at 2026-10-24 12:46:30.124302
# Unit test for function common
def test_common():
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert module_0.common([3, 2, 1], [3, 2]) == [2, 3]  # sorted
    assert module_0.common([1, 2], [3, 4]) == []  # no overlap
    assert module_0.common([], [1, 2]) == []
    assert module_0.common([1, 2], []) == []
    assert module_0.common([], []) == []
    assert module_0.common([1, 1, 2, 2], [1, 1, 3]) == [1]  # deduplicated
    assert module_0.common(['a', 'b', 'c'], ['b', 'c', 'd']) == ['b', 'c']