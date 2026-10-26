

# Generated at 2026-10-25 07:34:54.151894
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

# Generated at 2026-10-25 07:34:56.748525
# Unit test for function sort_even

# Generated at 2026-10-25 07:34:59.165282
# Unit test for function sort_even

# Generated at 2026-10-25 07:35:01.579725
# Unit test for function sort_even

# Generated at 2026-10-25 07:35:03.998076
# Unit test for function sort_even

# Generated at 2026-10-25 07:35:06.414603
# Unit test for function sort_even

# Generated at 2026-10-25 07:35:08.827592
# Unit test for function sort_even

# Generated at 2026-10-25 07:35:11.243590
# Unit test for function sort_even

# Generated at 2026-10-25 07:35:13.659178
# Unit test for function sort_even

# Generated at 2026-10-25 07:35:16.073167
# Unit test for function sort_even

# Generated at 2026-10-25 07:35:18.488673
# Unit test for function sort_even

# Generated at 2026-10-25 07:35:20.903165
# Unit test for function sort_even

# Generated at 2026-10-25 07:35:23.320093
# Unit test for function sort_even