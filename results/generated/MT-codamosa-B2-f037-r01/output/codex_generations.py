

# Generated at 2026-10-25 01:56:33.659967
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

# Generated at 2026-10-25 01:56:36.188703
# Unit test for function sort_even

# Generated at 2026-10-25 01:56:38.603549
# Unit test for function sort_even

# Generated at 2026-10-25 01:56:41.018852
# Unit test for function sort_even

# Generated at 2026-10-25 01:56:43.433736
# Unit test for function sort_even

# Generated at 2026-10-25 01:56:49.124088
# Unit test for function sort_even
def test_sort_even():
    assert module_0.sort_even([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert module_0.sort_even([4, 1, 2, 3, 0]) == [0, 1, 2, 3, 4]
    assert module_0.sort_even([]) == []
    assert module_0.sort_even([7]) == [7]
    assert module_0.sort_even([9, 8]) == [9, 8]
    assert module_0.sort_even([10, 1, 5, 2, 3, 4]) == [3, 1, 5, 2, 10, 4]
    assert module_0.sort_even([2, 2, 2, 2]) == [2, 2, 2, 2]

# Generated at 2026-10-25 01:56:50.510964
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

# Generated at 2026-10-25 01:56:51.878031
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