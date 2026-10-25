

# Generated at 2026-10-25 00:05:28.416824
# Unit test for function strange_sort_list

# Generated at 2026-10-25 00:05:30.837281
# Unit test for function strange_sort_list

# Generated at 2026-10-25 00:05:33.256712
# Unit test for function strange_sort_list

# Generated at 2026-10-25 00:05:35.683596
# Unit test for function strange_sort_list

# Generated at 2026-10-25 00:05:40.592999
# Unit test for function strange_sort_list
def test_strange_sort_list():assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]

# Generated at 2026-10-25 00:05:48.172284
# Unit test for function strange_sort_list
def test_strange_sort_list():
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([1]) == [1]
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([5, 1, 4, 2, 3]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([2, 2, 1, 3]) == [1, 3, 2, 2]
    assert module_0.strange_sort_list([-3, -1, -2, 0]) == [-3, 0, -2, -1]

# Generated at 2026-10-25 00:05:54.115690
# Unit test for function strange_sort_list
def test_strange_sort_list():
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([5]) == [5]
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([4, 1, 3, 2]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([3, 1, 2, 3, 1]) == [1, 3, 1, 3, 2]
    assert module_0.strange_sort_list([-2, 5, 0, -2]) == [-2, 5, -2, 0]

# Generated at 2026-10-25 00:06:00.668433
# Unit test for function strange_sort_list
def test_strange_sort_list():
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([1]) == [1]
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([5, 1, 3, 1, 4]) == [1, 5, 1, 4, 3]
    assert module_0.strange_sort_list([-3, -1, -2, 0]) == [-3, 0, -2, -1]