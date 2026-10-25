

# Generated at 2026-10-25 03:43:23.018313
# Unit test for function common
def test_common():
    # basic overlap, sorted output
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    # no overlap -> empty list
    assert module_0.common([1, 2], [3, 4]) == []
    # duplicates in inputs collapse to one
    assert module_0.common([1, 1, 2, 2], [2, 2, 3]) == [2]
    # empty inputs
    assert module_0.common([], [1, 2]) == []
    assert module_0.common([1, 2], []) == []
    assert module_0.common([], []) == []
    # result is sorted regardless of input order
    assert module_0.common([3, 1, 2], [2, 3, 1]) == [1, 2, 3]
    # strings work too
    assert module_0.common(["a", "b"], ["b", "c"]) == ["b"]

# Generated at 2026-10-25 03:43:24.346814
# Unit test for function common
def test_common():
    # basic overlap, sorted output
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    # no overlap -> empty list
    assert module_0.common([1, 2], [3, 4]) == []
    # duplicates in inputs collapse to one
    assert module_0.common([1, 1, 2, 2], [2, 2, 3]) == [2]
    # empty inputs
    assert module_0.common([], [1, 2]) == []
    assert module_0.common([1, 2], []) == []
    assert module_0.common([], []) == []
    # result is sorted regardless of input order
    assert module_0.common([3, 1, 2], [2, 3, 1]) == [1, 2, 3]
    # strings work too
    assert module_0.common(["a", "b"], ["b", "c"]) == ["b"]

# Generated at 2026-10-25 03:43:25.677169
# Unit test for function common
def test_common():
    # basic overlap, sorted output
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    # no overlap -> empty list
    assert module_0.common([1, 2], [3, 4]) == []
    # duplicates in inputs collapse to one
    assert module_0.common([1, 1, 2, 2], [2, 2, 3]) == [2]
    # empty inputs
    assert module_0.common([], [1, 2]) == []
    assert module_0.common([1, 2], []) == []
    assert module_0.common([], []) == []
    # result is sorted regardless of input order
    assert module_0.common([3, 1, 2], [2, 3, 1]) == [1, 2, 3]
    # strings work too
    assert module_0.common(["a", "b"], ["b", "c"]) == ["b"]

# Generated at 2026-10-25 03:43:27.000798
# Unit test for function common
def test_common():
    # basic overlap, sorted output
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    # no overlap -> empty list
    assert module_0.common([1, 2], [3, 4]) == []
    # duplicates in inputs collapse to one
    assert module_0.common([1, 1, 2, 2], [2, 2, 3]) == [2]
    # empty inputs
    assert module_0.common([], [1, 2]) == []
    assert module_0.common([1, 2], []) == []
    assert module_0.common([], []) == []
    # result is sorted regardless of input order
    assert module_0.common([3, 1, 2], [2, 3, 1]) == [1, 2, 3]
    # strings work too
    assert module_0.common(["a", "b"], ["b", "c"]) == ["b"]

# Generated at 2026-10-25 03:43:28.333821
# Unit test for function common
def test_common():
    # basic overlap, sorted output
    assert module_0.common([1, 2, 3], [2, 3, 4]) == [2, 3]
    # no overlap -> empty list
    assert module_0.common([1, 2], [3, 4]) == []
    # duplicates in inputs collapse to one
    assert module_0.common([1, 1, 2, 2], [2, 2, 3]) == [2]
    # empty inputs
    assert module_0.common([], [1, 2]) == []
    assert module_0.common([1, 2], []) == []
    assert module_0.common([], []) == []
    # result is sorted regardless of input order
    assert module_0.common([3, 1, 2], [2, 3, 1]) == [1, 2, 3]
    # strings work too
    assert module_0.common(["a", "b"], ["b", "c"]) == ["b"]