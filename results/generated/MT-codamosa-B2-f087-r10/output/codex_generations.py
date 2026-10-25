

# Generated at 2026-10-24 05:37:42.999694
# Unit test for function get_row

# Generated at 2026-10-24 05:37:47.440530
# Unit test for function get_row
def test_get_row():lst = [
        [1, 2, 1, 3],
        [1, 4, 1],
        [5, 1, 6, 1],
    ]

# Generated at 2026-10-24 05:37:55.368156
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

# Generated at 2026-10-24 05:38:15.046808
# Unit test for function get_row
def test_get_row():
    # Single match
    assert module_0.get_row([[1]], 1) == [(0, 0)]

    # Multiple matches, same row â columns descending
    assert module_0.get_row([[1, 2, 1], [3, 4, 5]], 1) == [(0, 2), (0, 0)]

    # Matches across rows â rows ascending, columns descending within row
    assert module_0.get_row([[1, 2, 3], [4, 1, 5], [1, 1, 1]], 1) == [(0, 0), (1, 1), (2, 2), (2, 1), (2, 0)]

    # No match
    assert module_0.get_row([[1, 2], [3, 4]], 9) == []

    # Empty list
    assert module_0.get_row([], 1) == []

    # Rows of unequal length
    assert module_0.get_row([[7, 8], [7], [7, 7, 7]], 7) == [(0, 1), (0, 0), (1, 0), (2, 2), (2, 1), (2, 0)]

    # Ragged row with no match in some rows
    assert module_0.get_row([[1], [], [1]], 1) == [(0, 0), (2, 0)]

    print("All tests passed.")

test_get_row()

# Generated at 2026-10-24 05:38:22.521057
# Unit test for function get_row
def test_get_row():
    lst = [
        [1, 2, 1, 1],
        [1, 3, 1],
        [],
        [4, 1],
    ]

    assert module_0.get_row(lst, 1) == [
        (0, 3),
        (0, 2),
        (0, 0),
        (1, 2),
        (1, 0),
        (3, 1),
    ]
    assert module_0.get_row(lst, 99) == []
    assert module_0.get_row([], 1) == []

# Generated at 2026-10-24 05:38:29.382095
# Unit test for function get_row
def test_get_row():
    matrix = [
        [1, 2, 1],
        [1, 3],
        [4, 1, 1],
    ]

    assert module_0.get_row(matrix, 1) == [
        (0, 2),
        (0, 0),
        (1, 0),
        (2, 2),
        (2, 1),
    ]
    assert module_0.get_row(matrix, 9) == []
    assert module_0.get_row([], 1) == []