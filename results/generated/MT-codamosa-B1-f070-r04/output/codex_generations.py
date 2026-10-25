

# Generated at 2026-10-24 12:21:07.065767
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # basic alternation
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 1, 3, 2, 4]) == [1, 5, 2, 4, 3]

    # edge cases
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([7]) == [7]

    # duplicates: min/max picks still alternate correctly
    assert module_0.strange_sort_list([1, 1, 2, 2, 3]) == [1, 3, 1, 2, 2]

    # negatives and mixed types of numbers
    assert module_0.strange_sort_list([-3, 0, -1, 2]) == [-3, 2, -1, 0]

    # works on any orderable elements
    assert module_0.strange_sort_list(["b", "a", "c"]) == ["a", "c", "b"]

    # invariant: same length, same multiset as input
    data = [9, 4, 7, 1, 4]
    out = module_0.strange_sort_list(data[:])
    assert len(out) == len(data)
    assert sorted(out) == sorted(data)

    # documented side effect: input list is consumed
    src = [1, 2]
    module_0.strange_sort_list(src)
    assert src == []

# Generated at 2026-10-24 12:21:08.450979
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # basic alternation
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 1, 3, 2, 4]) == [1, 5, 2, 4, 3]

    # edge cases
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([7]) == [7]

    # duplicates: min/max picks still alternate correctly
    assert module_0.strange_sort_list([1, 1, 2, 2, 3]) == [1, 3, 1, 2, 2]

    # negatives and mixed types of numbers
    assert module_0.strange_sort_list([-3, 0, -1, 2]) == [-3, 2, -1, 0]

    # works on any orderable elements
    assert module_0.strange_sort_list(["b", "a", "c"]) == ["a", "c", "b"]

    # invariant: same length, same multiset as input
    data = [9, 4, 7, 1, 4]
    out = module_0.strange_sort_list(data[:])
    assert len(out) == len(data)
    assert sorted(out) == sorted(data)

    # documented side effect: input list is consumed
    src = [1, 2]
    module_0.strange_sort_list(src)
    assert src == []

# Generated at 2026-10-24 12:21:09.884936
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # basic alternation
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 1, 3, 2, 4]) == [1, 5, 2, 4, 3]

    # edge cases
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([7]) == [7]

    # duplicates: min/max picks still alternate correctly
    assert module_0.strange_sort_list([1, 1, 2, 2, 3]) == [1, 3, 1, 2, 2]

    # negatives and mixed types of numbers
    assert module_0.strange_sort_list([-3, 0, -1, 2]) == [-3, 2, -1, 0]

    # works on any orderable elements
    assert module_0.strange_sort_list(["b", "a", "c"]) == ["a", "c", "b"]

    # invariant: same length, same multiset as input
    data = [9, 4, 7, 1, 4]
    out = module_0.strange_sort_list(data[:])
    assert len(out) == len(data)
    assert sorted(out) == sorted(data)

    # documented side effect: input list is consumed
    src = [1, 2]
    module_0.strange_sort_list(src)
    assert src == []

# Generated at 2026-10-24 12:21:11.521069
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # basic alternation
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 1, 3, 2, 4]) == [1, 5, 2, 4, 3]

    # edge cases
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([7]) == [7]

    # duplicates: min/max picks still alternate correctly
    assert module_0.strange_sort_list([1, 1, 2, 2, 3]) == [1, 3, 1, 2, 2]

    # negatives and mixed types of numbers
    assert module_0.strange_sort_list([-3, 0, -1, 2]) == [-3, 2, -1, 0]

    # works on any orderable elements
    assert module_0.strange_sort_list(["b", "a", "c"]) == ["a", "c", "b"]

    # invariant: same length, same multiset as input
    data = [9, 4, 7, 1, 4]
    out = module_0.strange_sort_list(data[:])
    assert len(out) == len(data)
    assert sorted(out) == sorted(data)

    # documented side effect: input list is consumed
    src = [1, 2]
    module_0.strange_sort_list(src)
    assert src == []

# Generated at 2026-10-24 12:21:13.004715
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # basic alternation
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 1, 3, 2, 4]) == [1, 5, 2, 4, 3]

    # edge cases
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([7]) == [7]

    # duplicates: min/max picks still alternate correctly
    assert module_0.strange_sort_list([1, 1, 2, 2, 3]) == [1, 3, 1, 2, 2]

    # negatives and mixed types of numbers
    assert module_0.strange_sort_list([-3, 0, -1, 2]) == [-3, 2, -1, 0]

    # works on any orderable elements
    assert module_0.strange_sort_list(["b", "a", "c"]) == ["a", "c", "b"]

    # invariant: same length, same multiset as input
    data = [9, 4, 7, 1, 4]
    out = module_0.strange_sort_list(data[:])
    assert len(out) == len(data)
    assert sorted(out) == sorted(data)

    # documented side effect: input list is consumed
    src = [1, 2]
    module_0.strange_sort_list(src)
    assert src == []