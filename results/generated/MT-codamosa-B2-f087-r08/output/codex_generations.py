

# Generated at 2026-10-25 04:52:10.574202
# Unit test for function get_row
def test_get_row():
    lst = [
        [1, 2, 3],
        [2, 4, 2],
        [5, 2, 2]
    ]

    assert module_0.get_row(lst, 2) == [
        (0, 1),
        (1, 2),
        (1, 0),
        (2, 2),
        (2, 1)
    ]

    assert module_0.get_row(lst, 9) == []

# Generated at 2026-10-25 04:52:16.012555
# Unit test for function get_row
def test_get_row():
    lst = [
        [1, 2, 1, 3],
        [1, 4, 1],
        [5, 1, 1, 1]
    ]

    assert module_0.get_row(lst, 1) == [
        (0, 2), (0, 0),
        (1, 2), (1, 0),
        (2, 3), (2, 2), (2, 1)
    ]
    assert module_0.get_row(lst, 4) == [(1, 1)]
    assert module_0.get_row(lst, 99) == []
    assert module_0.get_row([], 1) == []

# Generated at 2026-10-25 04:52:18.431718
# Unit test for function get_row

# Generated at 2026-10-25 04:52:21.020014
# Unit test for function get_row

# Generated at 2026-10-25 04:52:23.438442
# Unit test for function get_row

# Generated at 2026-10-25 04:52:32.171684
# Unit test for function get_row
def test_get_row():
    # Basic case: x appears in multiple rows, columns sorted descending within each row
    assert module_0.get_row([[1, 2, 3, 4, 5, 6],
                    [1, 2, 3, 4, 1, 6],
                    [1, 2, 3, 4, 5, 1]], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Single row, duplicate occurrences sorted by column descending
    assert module_0.get_row([[9, 8, 9, 7, 9]], 9) == [(0, 4), (0, 2), (0, 0)]

    # x not present anywhere -> empty list
    assert module_0.get_row([[1, 2, 3], [4, 5, 6]], 99) == []

    # Empty matrix -> empty list
    assert module_0.get_row([], 5) == []

    # Matrix with empty rows -> empty list
    assert module_0.get_row([[], [], []], 5) == []

    # x larger than any element, single occurrence
    assert module_0.get_row([[10, 20], [30, 40]], 40) == [(1, 1)]

    # Multiple occurrences in one row only
    assert module_0.get_row([[5, 5, 5]], 5) == [(0, 2), (0, 1), (0, 0)]

    # Ragged rows
    assert module_0.get_row([[2], [2, 2], [], [1, 2, 2]], 2) == [(0, 0), (1, 1), (1, 0), (3, 2), (3, 1)]

    # Negative numbers
    assert module_0.get_row([[-1, -2, -1], [0, -1]], -1) == [(0, 2), (0, 0), (1, 1)]

    # Result must always be sorted by row index ascending
    result = module_0.get_row([[3, 3], [3], [3, 3, 3]], 3)
    assert result == [(0, 1), (0, 0), (1, 0), (2, 2), (2, 1), (2, 0)]

    print("All tests passed!")


if __name__ == "__main__":
    test_get_row()

# Generated at 2026-10-25 04:52:37.905728
# Unit test for function get_row
def test_get_row():
    lst = [
        [1, 2, 1, 3],
        [1, 4, 1],
        [5, 1, 1]
    ]

    assert module_0.get_row(lst, 1) == [
        (0, 2), (0, 0),
        (1, 2), (1, 0),
        (2, 2), (2, 1)
    ]

    # Value not present
    assert module_0.get_row(lst, 99) == []

    # Empty list
    assert module_0.get_row([], 1) == []