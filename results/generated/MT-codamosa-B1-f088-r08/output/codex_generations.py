

# Generated at 2026-10-25 10:47:06.177468
# Unit test for function sort_array
def test_sort_array():
    # empty array
    assert module_0.sort_array([]) == []

    # single element (first == last, sum even, but nothing to reorder)
    assert module_0.sort_array([5]) == [5]

    # first + last even -> descending
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]      # 1+3 = 4
    assert module_0.sort_array([4, 1, 2]) == [4, 2, 1]      # 4+2 = 6

    # first + last odd -> ascending
    assert module_0.sort_array([1, 2, 4]) == [1, 2, 4]      # 1+4 = 5
    assert module_0.sort_array([3, 1, 2]) == [1, 2, 3]      # 3+2 = 5

    # uses ORIGINAL first/last, not sorted ones
    # [4, 1, 2]: original 4+2=6 -> descending; sorted 1+4=5 would give ascending
    assert module_0.sort_array([4, 1, 2]) == [4, 2, 1]

    # negatives and duplicates
    assert module_0.sort_array([-3, 0, -3]) == [-3, -3, 0]  # -3 + -3 = -6 (even) -> descending
    assert module_0.sort_array([2, 2, 2]) == [2, 2, 2]      # 2+2 = 4 even -> descending, already equal

# Generated at 2026-10-25 10:47:23.014458
# Unit test for function sort_array
def test_sort_array():
    # empty array
    assert module_0.sort_array([]) == []

    # single element (first == last, sum even, but nothing to reorder)
    assert module_0.sort_array([5]) == [5]

    # first + last even -> descending
    assert module_0.sort_array([1, 2, 3]) == [3, 2, 1]      # 1+3 = 4
    assert module_0.sort_array([4, 1, 2]) == [4, 2, 1]      # 4+2 = 6

    # first + last odd -> ascending
    assert module_0.sort_array([1, 2, 4]) == [1, 2, 4]      # 1+4 = 5
    assert module_0.sort_array([3, 1, 2]) == [1, 2, 3]      # 3+2 = 5

    # uses ORIGINAL first/last, not sorted ones
    # [4, 1, 2]: original 4+2=6 -> descending; sorted 1+4=5 would give ascending
    assert module_0.sort_array([4, 1, 2]) == [4, 2, 1]

    # negatives and duplicates
    assert module_0.sort_array([-3, 0, -3]) == [-3, -3, 0]  # -3 + -3 = -6 (even) -> descending
    assert module_0.sort_array([2, 2, 2]) == [2, 2, 2]      # 2+2 = 4 even -> descending, already equal

# Generated at 2026-10-25 10:47:25.720666
# Unit test for function sort_array

# Generated at 2026-10-25 10:47:28.142856
# Unit test for function sort_array

# Generated at 2026-10-25 10:47:30.555062
# Unit test for function sort_array

# Generated at 2026-10-25 10:47:32.969660
# Unit test for function sort_array

# Generated at 2026-10-25 10:47:35.469491
# Unit test for function sort_array

# Generated at 2026-10-25 10:47:37.855838
# Unit test for function sort_array

# Generated at 2026-10-25 10:47:40.271944
# Unit test for function sort_array

# Generated at 2026-10-25 10:47:43.074497
# Unit test for function sort_array

# Generated at 2026-10-25 10:47:45.489851
# Unit test for function sort_array