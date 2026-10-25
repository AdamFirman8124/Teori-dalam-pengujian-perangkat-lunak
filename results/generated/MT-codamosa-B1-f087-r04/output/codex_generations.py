

# Generated at 2026-10-24 06:18:15.030462
# Unit test for function get_row
def test_get_row():
    lst = [
        [1, 2, 1],
        [3, 1],
        [1, 4, 1]
    ]

    assert module_0.get_row(lst, 1) == [
        (0, 2), (0, 0),
        (1, 1),
        (2, 2), (2, 0)
    ]

    assert module_0.get_row(lst, 4) == [(2, 1)]
    assert module_0.get_row(lst, 99) == []

# Generated at 2026-10-24 06:18:21.876447
# Unit test for function get_row
def test_get_row():
    lst = [
        [1, 2, 1],
        [1, 3],
        [4, 1, 1]
    ]

    assert module_0.get_row(lst, 1) == [
        (0, 2), (0, 0),
        (1, 0),
        (2, 2), (2, 1)
    ]

    assert module_0.get_row(lst, 3) == [(1, 1)]
    assert module_0.get_row(lst, 99) == []
    assert module_0.get_row([], 1) == []

# Generated at 2026-10-24 06:18:27.735754
# Unit test for function get_row
def test_get_row():
    matrix = [
        [1, 2, 1],
        [3, 1, 4],
        [1, 5, 1]
    ]

    assert module_0.get_row(matrix, 1) == [
        (0, 2), (0, 0),
        (1, 1),
        (2, 2), (2, 0)
    ]
    assert module_0.get_row(matrix, 9) == []
    assert module_0.get_row([], 1) == []

# Generated at 2026-10-24 06:18:42.783034
# Unit test for function get_row
def test_get_row():
    lst = [
        [5, 1, 5],
        [2, 5, 3],
        [4, 5, 5]
    ]

    # Rows ascending; columns descending within each row
    assert module_0.get_row(lst, 5) == [
        (0, 2), (0, 0),
        (1, 1),
        (2, 2), (2, 1)
    ]

    # Value not present
    assert module_0.get_row(lst, 99) == []

# Generated at 2026-10-24 06:18:47.888709
# Unit test for function get_row
def test_get_row():
    matrix = [
        [1, 2, 1],
        [3, 1, 4],
        [1, 5, 1],
    ]

    assert module_0.get_row(matrix, 1) == [
        (0, 2),
        (0, 0),
        (1, 1),
        (2, 2),
        (2, 0),
    ]
    assert module_0.get_row(matrix, 9) == []
    assert module_0.get_row([], 1) == []