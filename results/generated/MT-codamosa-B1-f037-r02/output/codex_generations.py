

# Generated at 2026-10-25 11:37:31.343871
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

# Generated at 2026-10-25 11:37:34.278456
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

# Generated at 2026-10-25 11:37:37.361181
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

# Generated at 2026-10-25 11:37:38.689417
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

# Generated at 2026-10-25 11:37:40.088889
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