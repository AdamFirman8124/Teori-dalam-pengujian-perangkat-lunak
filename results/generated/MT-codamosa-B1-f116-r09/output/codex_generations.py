

# Generated at 2026-10-24 23:09:02.376052
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([1]) == [1]
    assert module_0.sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8]) == [
        0, 1, 2, 4, 8, 3, 5, 6, 7
    ]
    assert module_0.sort_array([7, 3, 5, 1, 6, 2, 4]) == [
        1, 2, 4, 3, 5, 6, 7
    ]
    assert module_0.sort_array([3, 3, 1, 2]) == [1, 2, 3, 3]

# Generated at 2026-10-24 23:09:07.253173
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([3, 8, 3, 6, 5, 7, 9, 1]) == [1, 8, 3, 3, 5, 6, 9, 7]
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([0]) == [0]
    assert module_0.sort_array([7, 3, 1]) == [1, 3, 7]
    assert module_0.sort_array([5, 3, 6]) == [3, 5, 6]  # Equal bit counts: numeric order

# Generated at 2026-10-24 23:09:15.143437
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([]) == []
    assert module_0.sort_array([1]) == [1]
    assert module_0.sort_array([1, 15, 5, 7, 3]) == [1, 3, 5, 7, 15]
    assert module_0.sort_array([3, 8, 3, 6, 5, 7, 9, 1]) == [
        1, 8, 3, 3, 5, 6, 9, 7
    ]
    assert module_0.sort_array([8, 4, 2, 1]) == [1, 2, 4, 8]
    assert module_0.sort_array([0, 3, 1, 2]) == [0, 1, 2, 3]

# Generated at 2026-10-24 23:09:21.580384
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([3, 8, 3, 6, 5, 7, 9, 1]) == [
        1, 8, 3, 3, 5, 6, 9, 7
    ]
    assert module_0.sort_array([5, 3, 7, 10, 14]) == [3, 5, 10, 7, 14]
    assert module_0.sort_array([0, 1, 2, 4]) == [0, 1, 2, 4]
    assert module_0.sort_array([]) == []

# Generated at 2026-10-24 23:09:28.334783
# Unit test for function sort_array
def test_sort_array():
    assert module_0.sort_array([3, 7, 8, 9]) == [8, 3, 9, 7]
    assert module_0.sort_array([1, 2, 3, 4]) == [1, 2, 4, 3]
    assert module_0.sort_array([5, 3, 7, 10, 14]) == [3, 5, 10, 7, 14]
    assert module_0.sort_array([0, 3, 1, 3]) == [0, 1, 3, 3]
    assert module_0.sort_array([]) == []