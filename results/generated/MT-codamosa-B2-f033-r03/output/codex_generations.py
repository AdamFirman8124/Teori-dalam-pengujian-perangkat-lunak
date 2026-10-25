

# Generated at 2026-10-25 01:29:19.956946
# Unit test for function sort_third

# Generated at 2026-10-25 01:29:22.375641
# Unit test for function sort_third

# Generated at 2026-10-25 01:29:24.795408
# Unit test for function sort_third

# Generated at 2026-10-25 01:29:27.217292
# Unit test for function sort_third

# Generated at 2026-10-25 01:29:29.631982
# Unit test for function sort_third

# Generated at 2026-10-25 01:29:32.047219
# Unit test for function sort_third

# Generated at 2026-10-25 01:29:34.461731
# Unit test for function sort_third

# Generated at 2026-10-25 01:29:36.876668
# Unit test for function sort_third

# Generated at 2026-10-25 01:29:39.291463
# Unit test for function sort_third

# Generated at 2026-10-25 01:29:41.705562
# Unit test for function sort_third

# Generated at 2026-10-25 01:29:48.018407
# Unit test for function sort_third
def test_sort_third():
    assert module_0.sort_third([1, 2, 3]) == [1, 2, 3]
    assert module_0.sort_third([5, 6, 3, 4, 8, 9, 2]) == [2, 6, 3, 4, 8, 9, 5]
    assert module_0.sort_third([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [3, 8, 7, 6, 5, 4, 9, 2, 1]
    assert module_0.sort_third([5, 3, -2, -8, 0, 4, 1]) == [-8, 3, -2, 1, 0, 4, 5]
    assert module_0.sort_third([10, 2]) == [10, 2]
    assert module_0.sort_third([]) == []
    assert module_0.sort_third((7, 1, 3, 2)) == [2, 1, 3, 7]
    src = [3, 1, 2, 6, 5, 4]
    result = module_0.sort_third(src)
    assert src == [3, 1, 2, 6, 5, 4]
    assert result == [3, 1, 2, 6, 5, 4]

# Generated at 2026-10-25 01:29:58.053685
# Unit test for function sort_third
def test_sort_third():
    original = [9, 2, 8, 3, 7, 6, 1, 5, 4, 0]

    result = module_0.sort_third(original)

    # Elements at indices 0, 3, 6, and 9 are sorted
    assert result == [0, 2, 8, 1, 7, 6, 9, 5, 4, 3]

    # Elements at other indices remain unchanged
    assert result[1::3] == [2, 7, 5]
    assert result[2::3] == [8, 6, 4]

    # The function does not modify the original list
    assert original == [9, 2, 8, 3, 7, 6, 1, 5, 4, 0]