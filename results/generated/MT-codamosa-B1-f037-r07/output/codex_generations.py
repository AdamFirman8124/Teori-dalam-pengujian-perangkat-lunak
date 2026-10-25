

# Generated at 2026-10-25 03:31:52.812666
# Unit test for function sort_even
def test_sort_even():
    # empty and single-element
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([1]) == [1]

    # odd length: only even indices 0,2,4... are sorted
    assert module_0.sort_even([3, 1, 2]) == [2, 1, 3]
    assert module_0.sort_even([5, 2, 4, 3, 1]) == [1, 2, 4, 3, 5]

    # even length
    assert module_0.sort_even([4, 1, 3, 2]) == [3, 1, 4, 2]

    # already sorted evens / duplicates
    assert module_0.sort_even([1, 9, 2, 8, 3]) == [1, 9, 2, 8, 3]
    assert module_0.sort_even([2, 1, 2, 1, 2]) == [2, 1, 2, 1, 2]

    # negatives
    assert module_0.sort_even([-1, 5, -3, 2, 0]) == [-3, 5, -1, 2, 0]

    # odd positions unchanged
    l = [5, 2, 4, 3, 1]
    res = module_0.sort_even(l)
    assert res[1::2] == l[1::2]
    assert sorted(res[::2]) == res[::2]

    # input not mutated
    assert l == [5, 2, 4, 3, 1]

# Generated at 2026-10-25 03:31:54.230204
# Unit test for function sort_even
def test_sort_even():
    # empty and single-element
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([1]) == [1]

    # odd length: only even indices 0,2,4... are sorted
    assert module_0.sort_even([3, 1, 2]) == [2, 1, 3]
    assert module_0.sort_even([5, 2, 4, 3, 1]) == [1, 2, 4, 3, 5]

    # even length
    assert module_0.sort_even([4, 1, 3, 2]) == [3, 1, 4, 2]

    # already sorted evens / duplicates
    assert module_0.sort_even([1, 9, 2, 8, 3]) == [1, 9, 2, 8, 3]
    assert module_0.sort_even([2, 1, 2, 1, 2]) == [2, 1, 2, 1, 2]

    # negatives
    assert module_0.sort_even([-1, 5, -3, 2, 0]) == [-3, 5, -1, 2, 0]

    # odd positions unchanged
    l = [5, 2, 4, 3, 1]
    res = module_0.sort_even(l)
    assert res[1::2] == l[1::2]
    assert sorted(res[::2]) == res[::2]

    # input not mutated
    assert l == [5, 2, 4, 3, 1]

# Generated at 2026-10-25 03:31:55.640595
# Unit test for function sort_even
def test_sort_even():
    # empty and single-element
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([1]) == [1]

    # odd length: only even indices 0,2,4... are sorted
    assert module_0.sort_even([3, 1, 2]) == [2, 1, 3]
    assert module_0.sort_even([5, 2, 4, 3, 1]) == [1, 2, 4, 3, 5]

    # even length
    assert module_0.sort_even([4, 1, 3, 2]) == [3, 1, 4, 2]

    # already sorted evens / duplicates
    assert module_0.sort_even([1, 9, 2, 8, 3]) == [1, 9, 2, 8, 3]
    assert module_0.sort_even([2, 1, 2, 1, 2]) == [2, 1, 2, 1, 2]

    # negatives
    assert module_0.sort_even([-1, 5, -3, 2, 0]) == [-3, 5, -1, 2, 0]

    # odd positions unchanged
    l = [5, 2, 4, 3, 1]
    res = module_0.sort_even(l)
    assert res[1::2] == l[1::2]
    assert sorted(res[::2]) == res[::2]

    # input not mutated
    assert l == [5, 2, 4, 3, 1]

# Generated at 2026-10-25 03:31:56.999703
# Unit test for function sort_even
def test_sort_even():
    # empty and single-element
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([1]) == [1]

    # odd length: only even indices 0,2,4... are sorted
    assert module_0.sort_even([3, 1, 2]) == [2, 1, 3]
    assert module_0.sort_even([5, 2, 4, 3, 1]) == [1, 2, 4, 3, 5]

    # even length
    assert module_0.sort_even([4, 1, 3, 2]) == [3, 1, 4, 2]

    # already sorted evens / duplicates
    assert module_0.sort_even([1, 9, 2, 8, 3]) == [1, 9, 2, 8, 3]
    assert module_0.sort_even([2, 1, 2, 1, 2]) == [2, 1, 2, 1, 2]

    # negatives
    assert module_0.sort_even([-1, 5, -3, 2, 0]) == [-3, 5, -1, 2, 0]

    # odd positions unchanged
    l = [5, 2, 4, 3, 1]
    res = module_0.sort_even(l)
    assert res[1::2] == l[1::2]
    assert sorted(res[::2]) == res[::2]

    # input not mutated
    assert l == [5, 2, 4, 3, 1]

# Generated at 2026-10-25 03:31:58.462181
# Unit test for function sort_even
def test_sort_even():
    # empty and single-element
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([1]) == [1]

    # odd length: only even indices 0,2,4... are sorted
    assert module_0.sort_even([3, 1, 2]) == [2, 1, 3]
    assert module_0.sort_even([5, 2, 4, 3, 1]) == [1, 2, 4, 3, 5]

    # even length
    assert module_0.sort_even([4, 1, 3, 2]) == [3, 1, 4, 2]

    # already sorted evens / duplicates
    assert module_0.sort_even([1, 9, 2, 8, 3]) == [1, 9, 2, 8, 3]
    assert module_0.sort_even([2, 1, 2, 1, 2]) == [2, 1, 2, 1, 2]

    # negatives
    assert module_0.sort_even([-1, 5, -3, 2, 0]) == [-3, 5, -1, 2, 0]

    # odd positions unchanged
    l = [5, 2, 4, 3, 1]
    res = module_0.sort_even(l)
    assert res[1::2] == l[1::2]
    assert sorted(res[::2]) == res[::2]

    # input not mutated
    assert l == [5, 2, 4, 3, 1]