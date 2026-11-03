

# Generated at 2026-11-01 20:28:35.611163
# Unit test for function get_row
def test_get_row():
    # x appears once in each of multiple rows
    assert module_0.get_row([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # x not present
    assert module_0.get_row([[1, 2, 3], [4, 5, 6]], 9) == []

    # empty 2D list
    assert module_0.get_row([], 1) == []

    # list containing an empty row
    assert module_0.get_row([[], [1], [1, 2, 3]], 1) == [(1, 0)]

    # single element match
    assert module_0.get_row([[1]], 1) == [(0, 0)]

    # multiple occurrences in the same row -> columns sorted descending
    assert module_0.get_row([[1, 1, 1]], 1) == [(0, 2), (0, 1), (0, 0)]

    # rows of different lengths
    assert module_0.get_row([[2], [2, 2], [1, 2, 2, 1]], 2) == [(0, 0), (1, 1), (1, 0), (2, 2), (2, 1)]

    # works with strings
    assert module_0.get_row([["a", "b"], ["b", "a", "b"]], "b") == [(0, 1), (1, 2), (1, 0)]

    # works with negative numbers and zeros
    assert module_0.get_row([[-1, 0, -1], [0]], -1) == [(0, 2), (0, 0)]

    # rows sorted by row index ascending even if given out of pattern
    assert module_0.get_row([[5], [3], [5, 5]], 5) == [(0, 0), (2, 1), (2, 0)]

    print("All tests passed!")


if __name__ == "__main__":
    test_get_row()

# Generated at 2026-11-01 20:28:59.135279
# Unit test for function get_row
def test_get_row():
    # Single occurrence
    assert module_0.get_row([[1, 2, 3], [4, 5, 6]], 2) == [(0, 1)]

    # Multiple occurrences: rows ascending, columns descending within a row
    assert module_0.get_row(
        [[1, 2, 3, 4, 5, 6],
         [1, 2, 3, 4, 1, 6],
         [1, 2, 3, 4, 5, 1]],
        1
    ) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Repeated values in a single row -> columns in descending order
    assert module_0.get_row([[1, 1, 1]], 1) == [(0, 2), (0, 1), (0, 0)]

    # Value not present
    assert module_0.get_row([[1, 2], [3, 4]], 99) == []

    # Empty outer list
    assert module_0.get_row([], 1) == []

    # Empty inner lists
    assert module_0.get_row([[], [], []], 1) == []

    # Ragged (non-rectangular) input
    assert module_0.get_row([[7], [8, 7, 7], [], [7]], 7) == [(0, 0), (1, 2), (1, 1), (3, 0)]

    # Works with non-integer elements
    assert module_0.get_row([['a', 'b'], ['b', 'a']], 'b') == [(0, 1), (1, 0)]

# Generated at 2026-11-01 20:29:28.428622
# Unit test for function get_row
def test_get_row():
    # Typical 2D list with multiple occurrences across rows
    assert module_0.get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Empty list
    assert module_0.get_row([], 1) == []

    # Empty sublists mixed with non-empty
    assert module_0.get_row([[], [1], [1, 2, 3]], 1) == [(1, 0), (2, 1)]

    # Value not present
    assert module_0.get_row([[1, 2], [3, 4]], 5) == []

    # Multiple occurrences in a single row (columns sorted descending)
    assert module_0.get_row([[1, 1, 1]], 1) == [(0, 2), (0, 1), (0, 0)]

    # Ragged rows with multiple matches per row
    assert module_0.get_row([[2], [2, 2], [1, 2, 2]], 2) == [(0, 0), (1, 1), (1, 0), (2, 2), (2, 1)]

    # Works with strings
    assert module_0.get_row([["a", "b"], ["b", "a"]], "b") == [(0, 1), (1, 0)]

    # Single row, all matches
    assert module_0.get_row([[5, 5, 5, 5]], 5) == [(0, 3), (0, 2), (0, 1), (0, 0)]

    # Match in the last position only
    assert module_0.get_row([[1, 2, 3], [4, 5, 6]], 6) == [(1, 2)]

    print("All tests passed!")

# Generated at 2026-11-01 20:29:56.480132
# Unit test for function get_row
def test_get_row():
    # Typical case: multiple rows, x appears in several rows (columns descending within each row)
    assert module_0.get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # x appears once per row
    assert module_0.get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 6) == [(0, 5), (1, 5)]

    # Empty list
    assert module_0.get_row([], 1) == []

    # Rows of varying lengths (including empty row)
    assert module_0.get_row([[], [1], [1, 2]], 1) == [(1, 0)]

    # x not present at all
    assert module_0.get_row([[1, 2, 3], [4, 5, 6]], 7) == []

    # Multiple occurrences in the same row: columns must be in descending order
    assert module_0.get_row([[1, 1, 1], [1, 1, 1]], 1) == [
        (0, 2), (0, 1), (0, 0),
        (1, 2), (1, 1), (1, 0)
    ]

    # Single row
    assert module_0.get_row([[5, 3, 5, 1]], 5) == [(0, 2), (0, 0)]

    # Single-element rows (column vector)
    assert module_0.get_row([[2], [3], [2]], 2) == [(0, 0), (2, 0)]

    # Larger values
    assert module_0.get_row([[10, 20], [30, 10]], 10) == [(0, 0), (1, 1)]

# Generated at 2026-11-01 20:30:18.494491
# Unit test for function get_row
def test_get_row():
    # nonce:41972dc5
    # Standard case: rows ascending, columns descending within each row
    assert module_0.get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Empty matrix
    assert module_0.get_row([], 1) == []

    # Matrix with empty rows; single match at last position of its row
    assert module_0.get_row([[], [1], [1, 2, 3]], 2) == [(2, 2)]

    # Multiple matches in one row -> columns must come out descending
    assert module_0.get_row([[1, 1, 1]], 1) == [(0, 2), (0, 1), (0, 0)]

    # Value not present anywhere
    assert module_0.get_row([[1, 2], [3, 4]], 5) == []

    # Matches spread across several rows, multiple per row
    assert module_0.get_row([[9, 8], [7, 9], [9, 9]], 9) == [(0, 0), (1, 1), (2, 1), (2, 0)]

    # Single-element matrix containing target
    assert module_0.get_row([[42]], 42) == [(0, 0)]

    # Target is zero
    assert module_0.get_row([[0], [1, 0], []], 0) == [(0, 0), (1, 1)]