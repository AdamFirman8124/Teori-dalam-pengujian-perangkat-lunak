

# Generated at 2026-11-02 20:07:40.693635
# Unit test for function get_row
def test_get_row():
    # Typical case: multiple occurrences across rows
    assert module_0.get_row([[1, 2, 3, 4, 5, 6],
                    [1, 2, 3, 4, 1, 6],
                    [1, 2, 3, 4, 5, 1]], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Empty outer list
    assert module_0.get_row([], 1) == []

    # Rows of varying lengths, including empty rows
    assert module_0.get_row([[], [1], [1, 2, 3]], 1) == [(1, 0), (2, 0)]

    # Element not present
    assert module_0.get_row([[1, 2], [3, 4]], 5) == []

    # Duplicates within the same row: columns sorted descending
    assert module_0.get_row([[1, 1], [1, 1]], 1) == [(0, 1), (0, 0), (1, 1), (1, 0)]

    # Single match
    assert module_0.get_row([[7, 8, 9]], 8) == [(0, 1)]

    # Works with strings
    assert module_0.get_row([["a", "b"], ["b", "a"]], "b") == [(0, 1), (1, 0)]

    # Works with negative numbers and floats
    assert module_0.get_row([[-1, -1], [2.5]], -1) == [(0, 1), (0, 0)]

    print("All tests passed!")


if __name__ == "__main__":
    test_get_row()

# Generated at 2026-11-02 20:09:10.247370
# Unit test for function get_row
def test_get_row():
    # Single match
    assert module_0.get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) == [(1, 1)]

    # Classic example: rows ascending, columns descending within a row
    assert module_0.get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Multiple matches in same row (column order must be descending)
    assert module_0.get_row([[1, 2, 1], [1, 1, 1]], 1) == [(0, 2), (0, 0), (1, 2), (1, 1), (1, 0)]

    # Value not present
    assert module_0.get_row([[1, 2], [3, 4]], 99) == []

    # Empty outer list
    assert module_0.get_row([], 1) == []

    # Empty inner rows
    assert module_0.get_row([[], []], 1) == []

    # Jagged rows of different lengths
    assert module_0.get_row([[1], [1, 2], [], [1, 2, 1]], 1) == [(0, 0), (1, 0), (3, 2), (3, 0)]

    # Single element list
    assert module_0.get_row([[7]], 7) == [(0, 0)]

    # All elements match
    assert module_0.get_row([[0, 0], [0, 0]], 0) == [(0, 1), (0, 0), (1, 1), (1, 0)]

    # Matching non-integer values (e.g., strings)
    assert module_0.get_row([["a", "b"], ["b", "a"]], "b") == [(0, 1), (1, 0)]

    print("All tests passed!")


if __name__ == "__main__":
    test_get_row()

# Generated at 2026-11-02 20:10:23.120962
# Unit test for function get_row
def test_get_row():
    # Multiple occurrences across multiple rows (rows ascending, cols descending)
    assert module_0.get_row([[1, 2, 3, 4, 5, 6],
                    [1, 2, 3, 4, 1, 6],
                    [1, 2, 3, 4, 5, 1]], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Empty list
    assert module_0.get_row([], 1) == []

    # Value not present
    assert module_0.get_row([[1, 2, 3]], 5) == []

    # Single element match
    assert module_0.get_row([[7]], 7) == [(0, 0)]

    # Multiple matches in a single row -> columns in descending order
    assert module_0.get_row([[1, 2, 1, 2]], 2) == [(0, 3), (0, 1)]
    assert module_0.get_row([[3, 3, 3]], 3) == [(0, 2), (0, 1), (0, 0)]

    # Ragged (non-uniform) rows
    assert module_0.get_row([[1], [2, 1], [1, 1]], 1) == [(0, 0), (1, 1), (2, 1), (2, 0)]

    # Value spread across rows
    assert module_0.get_row([[9, 8], [8, 9]], 9) == [(0, 0), (1, 1)]

    # No matches in a multi-row list
    assert module_0.get_row([[1, 2], [3, 4]], 9) == []

# Generated at 2026-11-02 20:12:28.067397
# Unit test for function get_row
def test_get_row():
    # Typical case: multiple rows, value appearing multiple times per row
    # Rows sorted ascending, columns sorted descending within each row
    assert module_0.get_row([[1, 2, 3, 4, 5, 6],
                    [1, 2, 3, 4, 1, 6],
                    [1, 2, 3, 4, 5, 1]], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Value appears once
    assert module_0.get_row([[1, 2, 3], [4, 5, 6]], 5) == [(1, 1)]

    # Value not present in the list
    assert module_0.get_row([[1, 2, 3], [4, 5, 6]], 7) == []

    # Empty outer list
    assert module_0.get_row([], 1) == []

    # Empty inner lists
    assert module_0.get_row([[], [], []], 1) == []

    # Multiple occurrences in the same row -> columns in descending order
    assert module_0.get_row([[9, 9, 9, 9]], 9) == [(0, 3), (0, 2), (0, 1), (0, 0)]

    # Same row has multiple hits, rows still ascending overall
    assert module_0.get_row([[3, 3], [3], [3, 3, 3]], 3) == [(0, 1), (0, 0), (1, 0), (2, 2), (2, 1), (2, 0)]

    # Works with non-integer types (strings)
    assert module_0.get_row([["a", "b"], ["b", "a", "b"]], "b") == [(0, 1), (1, 2), (1, 0)]

    # Row containing no occurrences in the middle
    assert module_0.get_row([[5], [1, 2], [5]], 5) == [(0, 0), (2, 0)]

    print("All tests passed!")


if __name__ == "__main__":
    test_get_row()

# Generated at 2026-11-02 20:13:49.994777
# Unit test for function get_row
def test_get_row():
    # Target appears multiple times across rows; columns descending within each row
    assert module_0.get_row(
        [[1, 2, 3, 4, 5, 6],
         [1, 2, 3, 4, 1, 6],
         [1, 2, 3, 4, 5, 1]], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Empty input list
    assert module_0.get_row([], 1) == []

    # Sublists of varying lengths (including empty sublists)
    assert module_0.get_row([[], [1], [1, 2, 3]], 2) == [(2, 2)]
    assert module_0.get_row([[], [], []], 1) == []

    # Target not present
    assert module_0.get_row([[1, 2, 3], [4, 5, 6]], 7) == []

    # Single occurrence
    assert module_0.get_row([[1, 2], [3, 4]], 3) == [(1, 0)]

    # All occurrences in one row -> columns in descending order
    assert module_0.get_row([[5, 5, 5]], 5) == [(0, 2), (0, 1), (0, 0)]

    # Occurrences spanning rows and columns, verify ordering rule
    assert module_0.get_row([[0], [0, 0]], 0) == [(0, 0), (1, 1), (1, 0)]

    # Rows in ascending order take priority
    assert module_0.get_row([[9, 9], [9]], 9) == [(0, 1), (0, 0), (1, 0)]

    print("All tests passed!")


if __name__ == "__main__":
    test_get_row()