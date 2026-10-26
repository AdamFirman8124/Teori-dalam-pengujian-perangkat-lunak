

# Generated at 2026-10-25 08:10:31.603843
# Unit test for function strange_sort_list

# Generated at 2026-10-25 08:10:34.020988
# Unit test for function strange_sort_list

# Generated at 2026-10-25 08:10:36.437567
# Unit test for function strange_sort_list

# Generated at 2026-10-25 08:10:38.854326
# Unit test for function strange_sort_list

# Generated at 2026-10-25 08:10:41.264520
# Unit test for function strange_sort_list

# Generated at 2026-10-25 08:10:43.681157
# Unit test for function strange_sort_list

# Generated at 2026-10-25 08:10:45.069273
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Basic alternating min/max
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([-1, -2, -3, -4]) == [-4, -1, -2, -3]
    assert module_0.strange_sort_list([0, 10]) == [0, 10]

    # Single element and negatives mixed
    assert module_0.strange_sort_list([7]) == [7]
    assert module_0.strange_sort_list([3, -1, 0, 2]) == [-1, 3, 0, 2]

    # Duplicates
    assert module_0.strange_sort_list([2, 2, 1, 1]) == [1, 2, 1, 2]

    print("All tests passed!")


test_strange_sort_list()

# Generated at 2026-10-25 08:10:46.409146
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Basic alternating min/max
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([-1, -2, -3, -4]) == [-4, -1, -2, -3]
    assert module_0.strange_sort_list([0, 10]) == [0, 10]

    # Single element and negatives mixed
    assert module_0.strange_sort_list([7]) == [7]
    assert module_0.strange_sort_list([3, -1, 0, 2]) == [-1, 3, 0, 2]

    # Duplicates
    assert module_0.strange_sort_list([2, 2, 1, 1]) == [1, 2, 1, 2]

    print("All tests passed!")


test_strange_sort_list()

# Generated at 2026-10-25 08:10:47.837952
# Unit test for function strange_sort_list
def test_strange_sort_list():
    # Basic alternating min/max
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([-1, -2, -3, -4]) == [-4, -1, -2, -3]
    assert module_0.strange_sort_list([0, 10]) == [0, 10]

    # Single element and negatives mixed
    assert module_0.strange_sort_list([7]) == [7]
    assert module_0.strange_sort_list([3, -1, 0, 2]) == [-1, 3, 0, 2]

    # Duplicates
    assert module_0.strange_sort_list([2, 2, 1, 1]) == [1, 2, 1, 2]

    print("All tests passed!")


test_strange_sort_list()