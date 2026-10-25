

# Generated at 2026-10-24 12:59:52.441425
# Unit test for function sort_third
def test_sort_third():
    # empty and single element
    assert module_0.sort_third([]) == []
    assert module_0.sort_third([1]) == [1]
    assert module_0.sort_third([2, 1]) == [2, 1]

    # no change when only index 0 is divisible by 3
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([2, 1, 3]) == [2, 1, 3]

    # sorts indices 0, 3
    assert module_0.sort_third([4, 3, 2, 1]) == [1, 3, 2, 4]

    # sorts indices 0, 3, 6

# Generated at 2026-10-24 12:59:54.993704
# Unit test for function sort_third

# Generated at 2026-10-24 12:59:57.515973
# Unit test for function sort_third

# Generated at 2026-10-24 12:59:59.933816
# Unit test for function sort_third

# Generated at 2026-10-24 13:00:02.347133
# Unit test for function sort_third

# Generated at 2026-10-24 13:00:04.762667
# Unit test for function sort_third

# Generated at 2026-10-24 13:00:07.175863
# Unit test for function sort_third

# Generated at 2026-10-24 13:00:21.085601
# Unit test for function sort_third
def test_sort_third():
    assert module_0.sort_third([]) == []
    assert module_0.sort_third([1]) == [1]
    assert module_0.sort_third([1, 2]) == [1, 2]
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 8, 7, 6, 5, 4, 9, 2, 1]
    assert module_0.sort_third([3, 2, 1, 6, 5, 4, 9, 8, 7]) == [3, 2, 1, 6, 5, 4, 9, 8, 7]
    assert module_0.sort_third([5, 4, 3, 2, 1]) == [2, 4, 3, 5, 1]
    orig = [5, 6, 3, 4, 8, 9, 2]
    copy = list(orig)
    assert module_0.sort_third(orig) == [2, 6, 3, 4, 8, 9, 5]
    assert orig == copy

# Generated at 2026-10-24 13:00:23.967673
# Unit test for function sort_third
def test_sort_third():
    assert module_0.sort_third([]) == []
    assert module_0.sort_third([1]) == [1]
    assert module_0.sort_third([1, 2]) == [1, 2]
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 8, 7, 6, 5, 4, 9, 2, 1]
    assert module_0.sort_third([3, 2, 1, 6, 5, 4, 9, 8, 7]) == [3, 2, 1, 6, 5, 4, 9, 8, 7]
    assert module_0.sort_third([5, 4, 3, 2, 1]) == [2, 4, 3, 5, 1]
    orig = [5, 6, 3, 4, 8, 9, 2]
    copy = list(orig)
    assert module_0.sort_third(orig) == [2, 6, 3, 4, 8, 9, 5]
    assert orig == copy