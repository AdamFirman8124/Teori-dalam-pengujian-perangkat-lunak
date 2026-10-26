

# Generated at 2026-10-25 09:48:37.171516
# Unit test for function get_row
def test_get_row():
    # x appears in multiple rows; columns sorted descending within each row
    assert module_0.get_row([[1, 2, 3, 4, 5, 6],
                    [1, 2, 3, 4, 1, 6],
                    [1, 2, 3, 4, 5, 1]], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # empty grid
    assert module_0.get_row([], 1) == []

    # x appears once per row
    assert module_0.get_row([[], [1], [1, 2, 3]], 1) == [(1, 0), (2, 0)]

    # x not present
    assert module_0.get_row([[1, 2], [3, 4]], 9) == []

    # duplicate values in one row -> columns descending
    assert module_0.get_row([[3, 3, 3]], 3) == [(0, 2), (0, 1), (0, 0)]

    print("All tests passed.")


test_get_row()

# Generated at 2026-10-25 09:48:38.498234
# Unit test for function get_row
def test_get_row():
    # x appears in multiple rows; columns sorted descending within each row
    assert module_0.get_row([[1, 2, 3, 4, 5, 6],
                    [1, 2, 3, 4, 1, 6],
                    [1, 2, 3, 4, 5, 1]], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # empty grid
    assert module_0.get_row([], 1) == []

    # x appears once per row
    assert module_0.get_row([[], [1], [1, 2, 3]], 1) == [(1, 0), (2, 0)]

    # x not present
    assert module_0.get_row([[1, 2], [3, 4]], 9) == []

    # duplicate values in one row -> columns descending
    assert module_0.get_row([[3, 3, 3]], 3) == [(0, 2), (0, 1), (0, 0)]

    print("All tests passed.")


test_get_row()

# Generated at 2026-10-25 09:48:39.827026
# Unit test for function get_row
def test_get_row():
    # x appears in multiple rows; columns sorted descending within each row
    assert module_0.get_row([[1, 2, 3, 4, 5, 6],
                    [1, 2, 3, 4, 1, 6],
                    [1, 2, 3, 4, 5, 1]], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # empty grid
    assert module_0.get_row([], 1) == []

    # x appears once per row
    assert module_0.get_row([[], [1], [1, 2, 3]], 1) == [(1, 0), (2, 0)]

    # x not present
    assert module_0.get_row([[1, 2], [3, 4]], 9) == []

    # duplicate values in one row -> columns descending
    assert module_0.get_row([[3, 3, 3]], 3) == [(0, 2), (0, 1), (0, 0)]

    print("All tests passed.")


test_get_row()

# Generated at 2026-10-25 09:48:41.285234
# Unit test for function get_row
def test_get_row():
    # x appears in multiple rows; columns sorted descending within each row
    assert module_0.get_row([[1, 2, 3, 4, 5, 6],
                    [1, 2, 3, 4, 1, 6],
                    [1, 2, 3, 4, 5, 1]], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # empty grid
    assert module_0.get_row([], 1) == []

    # x appears once per row
    assert module_0.get_row([[], [1], [1, 2, 3]], 1) == [(1, 0), (2, 0)]

    # x not present
    assert module_0.get_row([[1, 2], [3, 4]], 9) == []

    # duplicate values in one row -> columns descending
    assert module_0.get_row([[3, 3, 3]], 3) == [(0, 2), (0, 1), (0, 0)]

    print("All tests passed.")


test_get_row()

# Generated at 2026-10-25 09:48:42.661749
# Unit test for function get_row
def test_get_row():
    # x appears in multiple rows; columns sorted descending within each row
    assert module_0.get_row([[1, 2, 3, 4, 5, 6],
                    [1, 2, 3, 4, 1, 6],
                    [1, 2, 3, 4, 5, 1]], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # empty grid
    assert module_0.get_row([], 1) == []

    # x appears once per row
    assert module_0.get_row([[], [1], [1, 2, 3]], 1) == [(1, 0), (2, 0)]

    # x not present
    assert module_0.get_row([[1, 2], [3, 4]], 9) == []

    # duplicate values in one row -> columns descending
    assert module_0.get_row([[3, 3, 3]], 3) == [(0, 2), (0, 1), (0, 0)]

    print("All tests passed.")


test_get_row()