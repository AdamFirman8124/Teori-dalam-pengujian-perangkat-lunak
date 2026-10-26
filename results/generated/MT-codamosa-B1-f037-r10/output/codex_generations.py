

# Generated at 2026-10-25 10:45:37.600504
# Unit test for function sort_even

# Generated at 2026-10-25 10:45:40.015427
# Unit test for function sort_even

# Generated at 2026-10-25 10:45:50.715476
# Unit test for function sort_even
def test_sort_even():assert module_0.sort_even([5, 2, 3, 4, 1]) == [1, 2, 3, 4, 5]

# Generated at 2026-10-25 10:46:05.401162
# Unit test for function sort_even
def test_sort_even():
    # even-index elements get sorted; odd-index elements stay in place
    assert module_0.sort_even([4, 3, 2, 1]) == [2, 3, 4, 1]

    # already sorted input is unchanged
    assert module_0.sort_even([1, 2, 3, 4]) == [1, 2, 3, 4]

    # odd length: extra even-index element stays at the end
    assert module_0.sort_even([3, 1, 2]) == [2, 1, 3]

    # single element / empty list
    assert module_0.sort_even([5]) == [5]
    assert module_0.sort_even([]) == []

    # duplicates and negatives
    assert module_0.sort_even([0, 9, -3, 7, 0]) == [-3, 9, 0, 7, 0]

# Generated at 2026-10-25 10:46:10.046917
# Unit test for function sort_even
def test_sort_even():
    # even-index elements get sorted; odd-index elements stay in place
    assert module_0.sort_even([4, 3, 2, 1]) == [2, 3, 4, 1]

    # already sorted input is unchanged
    assert module_0.sort_even([1, 2, 3, 4]) == [1, 2, 3, 4]

    # odd length: extra even-index element stays at the end
    assert module_0.sort_even([3, 1, 2]) == [2, 1, 3]

    # single element / empty list
    assert module_0.sort_even([5]) == [5]
    assert module_0.sort_even([]) == []

    # duplicates and negatives
    assert module_0.sort_even([0, 9, -3, 7, 0]) == [-3, 9, 0, 7, 0]

# Generated at 2026-10-25 10:46:24.959993
# Unit test for function sort_even
def test_sort_even():
    # even-index elements get sorted; odd-index elements stay in place
    assert module_0.sort_even([4, 3, 2, 1]) == [2, 3, 4, 1]

    # already sorted input is unchanged
    assert module_0.sort_even([1, 2, 3, 4]) == [1, 2, 3, 4]

    # odd length: extra even-index element stays at the end
    assert module_0.sort_even([3, 1, 2]) == [2, 1, 3]

    # single element / empty list
    assert module_0.sort_even([5]) == [5]
    assert module_0.sort_even([]) == []

    # duplicates and negatives
    assert module_0.sort_even([0, 9, -3, 7, 0]) == [-3, 9, 0, 7, 0]

# Generated at 2026-10-25 10:46:26.699254
# Unit test for function sort_even
def test_sort_even():
    # even-index elements get sorted; odd-index elements stay in place
    assert module_0.sort_even([4, 3, 2, 1]) == [2, 3, 4, 1]

    # already sorted input is unchanged
    assert module_0.sort_even([1, 2, 3, 4]) == [1, 2, 3, 4]

    # odd length: extra even-index element stays at the end
    assert module_0.sort_even([3, 1, 2]) == [2, 1, 3]

    # single element / empty list
    assert module_0.sort_even([5]) == [5]
    assert module_0.sort_even([]) == []

    # duplicates and negatives
    assert module_0.sort_even([0, 9, -3, 7, 0]) == [-3, 9, 0, 7, 0]