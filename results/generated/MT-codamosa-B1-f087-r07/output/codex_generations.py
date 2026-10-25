

# Generated at 2026-10-24 04:37:18.828295
# Unit test for function get_row
def test_get_row():
    assert module_0.get_row(
        [[1, 2, 1], [1, 3], [4, 1, 1]],
        1
    ) == [(0, 2), (0, 0), (1, 0), (2, 2), (2, 1)]

    assert module_0.get_row([[1, 2], [3, 4]], 5) == []
    assert module_0.get_row([], 1) == []
    assert module_0.get_row([[7]], 7) == [(0, 0)]

# Generated at 2026-10-24 04:37:24.868615
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

    assert module_0.get_row(lst, 99) == []
    assert module_0.get_row([], 1) == []

# Generated at 2026-10-24 04:37:27.379277
# Unit test for function get_row

# Generated at 2026-10-24 04:37:29.790398
# Unit test for function get_row

# Generated at 2026-10-24 04:37:32.202220
# Unit test for function get_row

# Generated at 2026-10-24 04:37:34.615938
# Unit test for function get_row

# Generated at 2026-10-24 04:37:37.028128
# Unit test for function get_row

# Generated at 2026-10-24 04:37:39.441004
# Unit test for function get_row

# Generated at 2026-10-24 04:37:45.657308
# Unit test for function get_row
def test_get_row():
    matrix = [
        [1, 2, 1, 3],
        [1, 4, 1],
        [5, 1]
    ]

    assert module_0.get_row(matrix, 1) == [
        (0, 2), (0, 0),
        (1, 2), (1, 0),
        (2, 1)
    ]

    assert module_0.get_row(matrix, 4) == [(1, 1)]
    assert module_0.get_row(matrix, 99) == []
    assert module_0.get_row([], 1) == []