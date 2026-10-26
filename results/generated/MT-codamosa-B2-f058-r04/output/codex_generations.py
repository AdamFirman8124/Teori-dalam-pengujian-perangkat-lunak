

# Generated at 2026-10-25 09:52:58.126616
# Unit test for function common

# Generated at 2026-10-25 09:53:00.540311
# Unit test for function common

# Generated at 2026-10-25 09:53:02.957272
# Unit test for function common

# Generated at 2026-10-25 09:53:05.370817
# Unit test for function common

# Generated at 2026-10-25 09:53:07.785282
# Unit test for function common

# Generated at 2026-10-25 09:53:20.804697
# Unit test for function common
def test_common():assert module_0.common([1, 2, 2, 3], [2, 3, 4]) == [2, 3]

# Generated at 2026-10-25 09:53:53.040820
# Unit test for function common
def test_common():
    assert module_0.common([], []) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert module_0.common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert module_0.common([3, 2, 1], [1, 2]) == [1, 2]  # sorted result
    assert module_0.common([1, 1, 2, 2, 3], [2, 2, 3, 3, 4]) == [2, 3]  # deduplicated
    assert module_0.common(['a', 'b', 'c'], ['b', 'c', 'd']) == ['b', 'c']

# Generated at 2026-10-25 09:54:11.056374
# Unit test for function common
def test_common():
    assert module_0.common([], []) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert module_0.common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert module_0.common([3, 2, 1], [1, 2]) == [1, 2]  # sorted result
    assert module_0.common([1, 1, 2, 2, 3], [2, 2, 3, 3, 4]) == [2, 3]  # deduplicated
    assert module_0.common(['a', 'b', 'c'], ['b', 'c', 'd']) == ['b', 'c']

# Generated at 2026-10-25 09:54:29.795748
# Unit test for function common
def test_common():
    assert module_0.common([], []) == []
    assert module_0.common([1, 2, 3], []) == []
    assert module_0.common([], [1, 2, 3]) == []
    assert module_0.common([1, 2, 3], [4, 5, 6]) == []
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert module_0.common([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert module_0.common([3, 2, 1], [1, 2]) == [1, 2]  # sorted result
    assert module_0.common([1, 1, 2, 2, 3], [2, 2, 3, 3, 4]) == [2, 3]  # deduplicated
    assert module_0.common(['a', 'b', 'c'], ['b', 'c', 'd']) == ['b', 'c']