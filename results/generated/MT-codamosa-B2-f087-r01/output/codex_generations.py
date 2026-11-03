

# Generated at 2026-11-02 15:17:54.961263
# Unit test for function get_row
def test_get_row():
    # Basic case: multiple rows, multiple occurrences per row
    # Columns sorted descending within each row, rows ascending
    assert module_0.get_row([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Single occurrence values
    assert module_0.get_row([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 3) == [(0, 2), (1, 2), (2, 2)]
    assert module_0.get_row([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 6) == [(0, 5), (1, 5)]

    # Empty outer list
    assert module_0.get_row([], 1) == []

    # Rows of differing lengths, including empty rows
    assert module_0.get_row([[], [1], [1, 2, 3]], 1) == [(1, 0), (2, 0)]

    # Value not present anywhere
    assert module_0.get_row([[1, 2, 3]], 5) == []

    # Multiple occurrences within a single row (descending column order)
    assert module_0.get_row([[2, 2, 2]], 2) == [(0, 2), (0, 1), (0, 0)]

    # Single element matrix
    assert module_0.get_row([[1]], 1) == [(0, 0)]
    assert module_0.get_row([[1]], 2) == []

    # Nested case with rows appearing in non-sorted coordinate order before sorting
    assert module_0.get_row([[4, 4], [1, 4], [4, 1]], 4) == [(0, 1), (0, 0), (1, 1), (2, 0)]

# Generated at 2026-11-02 15:19:53.303799
# Unit test for function get_row
def test_get_row():
    # Basic case with multiple matches across rows, columns sorted descending within each row
    assert module_0.get_row([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1) == [
        (0, 0), (1, 4), (1, 0), (2, 5), (2, 0)
    ]
    # Value appearing once per row
    assert module_0.get_row([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 6) == [
        (0, 5), (1, 5)
    ]
    # Value not present
    assert module_0.get_row([[1, 2, 3], [4, 5, 6]], 9) == []
    # Empty outer list
    assert module_0.get_row([], 1) == []
    # Empty inner lists
    assert module_0.get_row([[], [1], [1, 2, 3]], 1) == [(2, 0)]
    # Single element match
    assert module_0.get_row([[1]], 1) == [(0, 0)]
    # Duplicates within the same row: columns in descending order
    assert module_0.get_row([[1, 1], [1, 1]], 1) == [(0, 1), (0, 0), (1, 1), (1, 0)]
    # Rows sorted ascending even when matches appear in later rows first
    assert module_0.get_row([[0, 1], [2, 1], [3, 1]], 1) == [(0, 1), (1, 1), (2, 1)]
    print("All get_row tests passed!")


test_get_row()

# Generated at 2026-11-02 15:22:52.751933
# Unit test for function get_row
def test_get_row():
    # Basic case: value appears once in each of two rows
    assert module_0.get_row([[1, 2, 3], [2, 3, 4]], 2) == [(0, 1), (1, 0)]

    # Value not present
    assert module_0.get_row([[1, 2, 3]], 5) == []

    # Empty input list
    assert module_0.get_row([], 1) == []

    # Row containing an empty list
    assert module_0.get_row([[]], 1) == []

    # Single element match
    assert module_0.get_row([[1]], 1) == [(0, 0)]

    # Multiple matches within rows: columns sorted descending within ascending rows
    assert module_0.get_row([[1, 1], [1, 1]], 1) == [(0, 1), (0, 0), (1, 1), (1, 0)]

    # Larger case with multiple matches per row
    assert module_0.get_row([[3, 2, 3], [1, 3, 3]], 3) == [(0, 2), (0, 0), (1, 2), (1, 1)]

    # Value repeated across several rows
    assert module_0.get_row([[9], [9], [9]], 9) == [(0, 0), (1, 0), (2, 0)]

    # Works with strings
    assert module_0.get_row([['a', 'b'], ['b', 'a']], 'b') == [(0, 1), (1, 0)]

    # Classic multi-row example
    assert module_0.get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

# Generated at 2026-11-02 15:25:28.229997
# Unit test for function get_row
def test_get_row():
    # Basic case with multiple occurrences across rows
    assert module_0.get_row([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1) == [
        (0, 0), (1, 4), (1, 0), (2, 5), (2, 0)
    ]

    # Value appearing multiple times in the same row (columns sorted descending)
    assert module_0.get_row([[1, 1, 1], [2, 2, 2]], 1) == [(0, 2), (0, 1), (0, 0)]

    # Empty outer list
    assert module_0.get_row([], 1) == []

    # Empty inner lists
    assert module_0.get_row([[], [1], [1, 2, 3]], 1) == [(1, 0), (2, 0)]

    # Value not present in the list
    assert module_0.get_row([[1, 2, 3], [4, 5, 6]], 7) == []

    # Single element match
    assert module_0.get_row([[5]], 5) == [(0, 0)]

    # Single element no match
    assert module_0.get_row([[5]], 3) == []

    # Value in the last row and last column
    assert module_0.get_row([[1, 2], [3, 4]], 4) == [(1, 1)]

    # Multiple rows with matches, ensuring row-major order
    assert module_0.get_row([[9, 8], [7, 9], [9, 9]], 9) == [(0, 0), (1, 1), (2, 1), (2, 0)]

    print("All tests passed!")


if __name__ == "__main__":
    test_get_row()