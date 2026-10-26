

# Generated at 2026-10-25 11:14:07.575042
# Unit test for function sort_array

# Generated at 2026-10-25 11:14:10.181392
# Unit test for function sort_array

# Generated at 2026-10-25 11:14:12.597942
# Unit test for function sort_array

# Generated at 2026-10-25 11:14:15.017791
# Unit test for function sort_array

# Generated at 2026-10-25 11:14:24.794597
# Unit test for function sort_array
def test_sort_array():assert module_0.sort_array([3, 8, 3, 6, 5, 7, 9, 1]) == [1, 8, 3, 3, 5, 6, 9, 7]

# Generated at 2026-10-25 11:14:32.205984
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([0]) == [0]
    assert module_0.sort_array([3, 8, 3, 6, 5, 7, 9, 1]) == [
        1, 8,       # 1 set bit
        3, 3, 5, 6, 9,  # 2 set bits
        7            # 3 set bits
    ]
    assert module_0.sort_array([7, 3, 1, 0, 2, 4]) == [0, 1, 2, 4, 3, 7]

# Generated at 2026-10-25 11:14:39.653656
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([0]) == [0]
    assert module_0.sort_array([1, 2, 3, 4]) == [1, 2, 4, 3]
    assert module_0.sort_array([3, 8, 3, 6, 5, 7, 9, 1]) == [
        1, 8, 3, 3, 5, 6, 9, 7
    ]
    assert module_0.sort_array([7, 3, 1, 0]) == [0, 1, 3, 7]

# Generated at 2026-10-25 11:14:45.491922
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([3, 8, 3, 6, 5, 7, 9, 1]) == [
        1, 8,          # 1 set bit
        3, 3, 5, 6, 9, # 2 set bits, numerically sorted
        7               # 3 set bits
    ]
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([0, 2, 1, 4]) == [0, 1, 2, 4]