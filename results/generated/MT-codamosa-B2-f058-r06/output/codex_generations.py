

# Generated at 2026-10-25 02:10:03.129749
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

# Generated at 2026-10-25 02:10:04.569441
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

# Generated at 2026-10-25 02:10:06.005329
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

# Generated at 2026-10-25 02:10:08.557321
# Unit test for function common

# Generated at 2026-10-25 02:10:11.087015
# Unit test for function common

# Generated at 2026-10-25 02:10:13.502841
# Unit test for function common

# Generated at 2026-10-25 02:10:15.918080
# Unit test for function common

# Generated at 2026-10-25 02:10:18.509936
# Unit test for function common

# Generated at 2026-10-25 02:10:20.925061
# Unit test for function common