

# Generated at 2026-10-24 12:54:44.327548
# Unit test for function get_row

# Generated at 2026-10-24 12:54:46.742279
# Unit test for function get_row

# Generated at 2026-10-24 12:54:49.155751
# Unit test for function get_row

# Generated at 2026-10-24 12:54:51.573163
# Unit test for function get_row

# Generated at 2026-10-24 12:54:53.987692
# Unit test for function get_row

# Generated at 2026-10-24 12:55:06.425424
# Unit test for function get_row
def test_get_row():assert module_0.get_row([[1, 2, 1], [1, 1, 3], [4, 1, 1]], 1) == [(0, 2), (0, 0), (1, 1), (1, 0), (2, 2), (2, 1)]

# Generated at 2026-10-24 12:55:22.501249
# Unit test for function get_row
def test_get_row():
    # empty list
    assert module_0.get_row([], 1) == []

    # empty rows
    assert module_0.get_row([[], [], []], 1) == []

    # single element found / not found
    assert module_0.get_row([[1]], 1) == [(0, 0)]
    assert module_0.get_row([[2]], 1) == []

    # x not present
    assert module_0.get_row([[2, 3], [4, 5]], 1) == []

    # single row, multiple occurrences -> columns descending
    assert module_0.get_row([[1, 1, 1]], 1) == [(0, 2), (0, 1), (0, 0)]

    # multiple rows, sorted by row ascending
    assert module_0.get_row([[1, 2, 3], [4, 1, 6]], 1) == [(0, 0), (1, 1)]

    # same row

# Generated at 2026-10-24 12:55:37.553853
# Unit test for function get_row
def test_get_row():
    matrix = [
        [1, 2, 1],
        [3, 1],
        [1, 4, 1]
    ]

    assert module_0.get_row(matrix, 1) == [
        (0, 2),
        (0, 0),
        (1, 1),
        (2, 2),
        (2, 0)
    ]

    assert module_0.get_row(matrix, 5) == []

# Generated at 2026-10-24 12:55:49.972588
# Unit test for function get_row
def test_get_row():
    matrix = [
        [1, 2, 1],
        [3, 1],
        [1, 4, 1],
    ]

    assert module_0.get_row(matrix, 1) == [
        (0, 2),
        (0, 0),
        (1, 1),
        (2, 2),
        (2, 0),
    ]

    assert module_0.get_row(matrix, 5) == []