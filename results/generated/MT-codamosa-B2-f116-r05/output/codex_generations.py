

# Generated at 2026-10-25 08:55:10.049920
# Unit test for function sort_array
def test_sort_array():
    # Ones count ascending, ties broken by numeric value
    assert module_0.sort_array([1, 5, 2, 3, 4]) == [1, 2, 4, 3, 5]      # 1:1, 2:1, 4:1, 3:2, 5:2
    assert module_0.sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]  # 3,3,3,4,4 ones
    assert module_0.sort_array([]) == []                                 # empty
    assert module_0.sort_array([0]) == [0]                               # single element
    assert module_0.sort_array([7, 7, 7]) == [7, 7, 7]                   # duplicates
    assert module_0.sort_array([2**31 - 1, 0, 1]) == [0, 1, 2**31 - 1]   # large values
    print("All tests passed.")

test_sort_array()

# Generated at 2026-10-25 08:55:12.714261
# Unit test for function sort_array

# Generated at 2026-10-25 08:55:15.255844
# Unit test for function sort_array

# Generated at 2026-10-25 08:55:17.674363
# Unit test for function sort_array

# Generated at 2026-10-25 08:55:20.093178
# Unit test for function sort_array

# Generated at 2026-10-25 08:55:22.510166
# Unit test for function sort_array

# Generated at 2026-10-25 08:55:24.924847
# Unit test for function sort_array

# Generated at 2026-10-25 08:55:27.343020
# Unit test for function sort_array

# Generated at 2026-10-25 08:55:29.758446
# Unit test for function sort_array

# Generated at 2026-10-25 08:55:32.178140
# Unit test for function sort_array

# Generated at 2026-10-25 08:55:34.594138
# Unit test for function sort_array

# Generated at 2026-10-25 08:55:37.010416
# Unit test for function sort_array

# Generated at 2026-10-25 08:55:39.430566
# Unit test for function sort_array