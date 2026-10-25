

# Generated at 2026-10-24 20:54:45.879869
# Unit test for function sort_third
def test_sort_third():
    original = [5, 6, 3, 4, 8, 9, 2, 1, 7]

    result = module_0.sort_third(original)

    assert result == [2, 6, 3, 4, 8, 9, 5, 1, 7]
    assert original == [5, 6, 3, 4, 8, 9, 2, 1, 7]  # Input is unchanged

# Generated at 2026-10-24 20:54:50.844614
# Unit test for function sort_third
def test_sort_third():
    original = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    result = module_0.sort_third(original)

    assert result == [3, 8, 7, 6, 5, 4, 9, 2, 1]
    assert original == [9, 8, 7, 6, 5, 4, 3, 2, 1]  # Input is unchanged

    assert module_0.sort_third([]) == []
    assert module_0.sort_third([3, 2, 1]) == [3, 2, 1]
    assert module_0.sort_third([4, 2, 1, 3]) == [3, 2, 1, 4]

# Generated at 2026-10-24 20:54:56.423844
# Unit test for function sort_third
def test_sort_third():
    original = [5, 2, 3, 1, 4, 6, 3, 8, 9]
    result = module_0.sort_third(original)

    assert result == [1, 2, 3, 3, 4, 6, 5, 8, 9]
    assert original == [5, 2, 3, 1, 4, 6, 3, 8, 9]  # Input is unchanged

# Generated at 2026-10-24 20:55:01.542987
# Unit test for function sort_third
def test_sort_third():
    original = [9, 2, 3, 6, 5, 4, 3, 8, 7, 0]
    result = module_0.sort_third(original)

    assert result == [0, 2, 3, 3, 5, 4, 6, 8, 7, 9]
    assert original == [9, 2, 3, 6, 5, 4, 3, 8, 7, 0]

# Generated at 2026-10-24 20:55:04.072604
# Unit test for function sort_third

# Generated at 2026-10-24 20:55:06.488675
# Unit test for function sort_third

# Generated at 2026-10-24 20:55:09.050132
# Unit test for function sort_third