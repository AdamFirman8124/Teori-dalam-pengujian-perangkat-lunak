

# Generated at 2026-10-24 22:50:00.575195
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

# Generated at 2026-10-24 22:50:06.511974
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

# Generated at 2026-10-24 22:50:11.754556
# Unit test for function get_row
def test_get_row():
    lst = [
        [1, 2, 1],
        [3, 1, 1],
        [1]
    ]

    assert module_0.get_row(lst, 1) == [
        (0, 2), (0, 0),
        (1, 2), (1, 1),
        (2, 0)
    ]

    # Value not present
    assert module_0.get_row(lst, 99) == []

# Generated at 2026-10-24 22:50:18.083267
# Unit test for function get_row
def test_get_row():
    matrix = [
        [1, 2, 3, 2],
        [2, 4, 2],
        [5, 2]
    ]

    assert module_0.get_row(matrix, 2) == [
        (0, 3), (0, 1),
        (1, 2), (1, 0),
        (2, 1)
    ]
    assert module_0.get_row(matrix, 9) == []
    assert module_0.get_row([], 2) == []

# Generated at 2026-10-24 22:50:23.211888
# Unit test for function get_row
def test_get_row():
    matrix = [
        [1, 2, 1, 3],
        [1, 4, 5, 1],
        [6, 1, 1, 7]
    ]

    assert module_0.get_row(matrix, 1) == [
        (0, 2), (0, 0),
        (1, 3), (1, 0),
        (2, 2), (2, 1)
    ]
    assert module_0.get_row(matrix, 4) == [(1, 1)]
    assert module_0.get_row(matrix, 99) == []
    assert module_0.get_row([], 1) == []