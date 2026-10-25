

# Generated at 2026-10-24 21:39:46.115528
# Unit test for function sort_array

# Generated at 2026-10-24 21:39:48.533295
# Unit test for function sort_array

# Generated at 2026-10-24 21:39:50.950989
# Unit test for function sort_array

# Generated at 2026-10-24 21:39:53.369914
# Unit test for function sort_array

# Generated at 2026-10-24 21:39:55.784870
# Unit test for function sort_array

# Generated at 2026-10-24 21:39:58.203142
# Unit test for function sort_array

# Generated at 2026-10-24 21:40:00.619233
# Unit test for function sort_array

# Generated at 2026-10-24 21:40:03.037803
# Unit test for function sort_array

# Generated at 2026-10-24 21:40:05.451780
# Unit test for function sort_array

# Generated at 2026-10-24 21:40:07.871389
# Unit test for function sort_array

# Generated at 2026-10-24 21:40:10.286222
# Unit test for function sort_array

# Generated at 2026-10-24 21:40:14.645638
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert module_0.sort_array([2, 3, 4]) == [4, 3, 2]
    assert module_0.sort_array([5]) == [5]
    assert module_0.sort_array([3, 1, 2]) == [1, 2, 3]
    assert module_0.sort_array([1, 5, 2, 3]) == [5, 3, 2, 1]
    assert module_0.sort_array([4, 1, 9, 2]) == [1, 2, 4, 9]
    assert module_0.sort_array([-1, 0, 1]) == [1, 0, -1]

# Generated at 2026-10-24 21:40:27.736576
# Unit test for function sort_array
def test_sort_array():
    # Empty array
    assert module_0.sort_array([]) == []

    # First + last elements = odd â ascending order
    assert module_0.sort_array([3, 1, 2]) == [1, 2, 3]

    # First + last elements = even â descending order
    assert module_0.sort_array([3, 1, 2, 5]) == [5, 3, 2, 1]

    # Single-element array
    assert module_0.sort_array([7]) == [7]

    # Original array should not be modified
    array = [4, 1, 3]
    module_0.sort_array(array)
    assert array == [4, 1, 3]