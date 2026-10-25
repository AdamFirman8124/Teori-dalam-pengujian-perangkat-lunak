

# Generated at 2026-10-25 02:14:21.389598
# Unit test for function strange_sort_list
def test_strange_sort_list():
    values = [3, 1, 4, 2, 5]

    result = module_0.strange_sort_list(values)

    assert result == [1, 5, 2, 4, 3]
    assert values == []  # The function consumes the input list


def test_strange_sort_list_empty():
    values = []

    assert module_0.strange_sort_list(values) == []


def test_strange_sort_list_single_item():
    values = [7]

    assert module_0.strange_sort_list(values) == [7]


def test_strange_sort_list_with_duplicates():
    values = [2, 1, 2, 1]

    assert module_0.strange_sort_list(values) == [1, 2, 1, 2]

# Generated at 2026-10-25 02:14:35.012765
# Unit test for function strange_sort_list
def test_strange_sort_list():
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert module_0.strange_sort_list([5, 1, 3, 2, 4]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([2, 2, 1, 3]) == [1, 3, 2, 2]
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([7]) == [7]

# Generated at 2026-10-25 02:14:50.258687
# Unit test for function strange_sort_list
def test_strange_sort_list():
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([5, 1, 4, 2, 3]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([3, 1, 2, 1]) == [1, 3, 1, 2]
    assert module_0.strange_sort_list([]) == []
    assert module_0.strange_sort_list([7]) == [7]

# Generated at 2026-10-25 02:15:06.313119
# Unit test for function strange_sort_list
def test_strange_sort_list():
    assert module_0.strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([5, 1, 4, 2, 3]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([3, 1, 2, 1]) == [1, 3, 1, 2]
    assert module_0.strange_sort_list([7]) == [7]
    assert module_0.strange_sort_list([]) == []

# Generated at 2026-10-25 02:15:21.497338
# Unit test for function strange_sort_list
def test_strange_sort_list():
    assert module_0.strange_sort_list([5, 1, 4, 2, 3]) == [1, 5, 2, 4, 3]
    assert module_0.strange_sort_list([3, 1, 2, 1]) == [1, 3, 1, 2]
    assert module_0.strange_sort_list([7]) == [7]
    assert module_0.strange_sort_list([]) == []

    # The function consumes the input list
    values = [4, 2, 3]
    assert module_0.strange_sort_list(values) == [2, 4, 3]
    assert values == []