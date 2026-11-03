

# Generated at 2026-11-01 23:05:34.549526
# Unit test for function get_row
def test_get_row():
    # Basic case: duplicates within and across rows
    assert module_0.get_row([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1) == \
        [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Empty outer list
    assert module_0.get_row([], 1) == []

    # Rows of differing lengths, including an empty row
    assert module_0.get_row([[], [1], [1, 2, 3]], 1) == [(1, 0), (2, 0)]

    # Target value not present anywhere
    assert module_0.get_row([[1, 2], [3, 4]], 99) == []

    # All matches in a single row -> columns must come back in descending order
    assert module_0.get_row([[7, 7, 7]], 7) == [(0, 2), (0, 1), (0, 0)]

    # Single-element grid containing the target
    assert module_0.get_row([[5]], 5) == [(0, 0)]

    # All rows empty
    assert module_0.get_row([[], [], []], 3) == []

    # Matches spread over multiple rows, mixed duplicate placements
    assert module_0.get_row([[9, 8], [8, 9], [9, 9]], 9) == [(0, 0), (1, 1), (2, 1), (2, 0)]

    # Works with non-integer values (strings)
    assert module_0.get_row([['a', 'b'], ['b', 'a']], 'b') == [(0, 1), (1, 0)]

    # Zero as the searched value
    assert module_0.get_row([[0, 1], [1, 0]], 0) == [(0, 0), (1, 1)]

    # Negative numbers
    assert module_0.get_row([[-1, -2], [-2, -1]], -2) == [(0, 1), (1, 0)]

# Generated at 2026-11-01 23:06:07.191882
# Unit test for function get_row
def test_get_row():
    # nonce:9ed25ec0
    # Classic case: rows ascending, columns descending within each row
    assert module_0.get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Empty outer list
    assert module_0.get_row([], 1) == []

    # Target not present
    assert module_0.get_row([[1, 2], [3, 4]], 5) == []

    # Single occurrence
    assert module_0.get_row([[0, 1], [2, 3]], 3) == [(1, 1)]

    # Entire single row matches -> strictly descending columns
    assert module_0.get_row([[1, 1, 1, 1]], 1) == [(0, 3), (0, 2), (0, 1), (0, 0)]

    # Multiple rows fully matching

# Generated at 2026-11-01 23:06:47.841872
# Unit test for function get_row
def test_get_row():
# nonce:71014ec3
    # Single occurrence
    assert module_0.get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) == [(1, 1)]
    assert module_0.get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9) == [(2, 2)]

    # Multiple occurrences in the same row: columns sorted descending
    assert module_0.get_row([[1, 2, 1], [1, 1, 1]], 1) == [(0, 2), (0, 0), (1, 2), (1, 1), (1, 0)]

    # Occurrences spread across rows: rows sorted ascending
    assert module_0.get_row([[1, 2], [2, 3], [2]], 2) == [(0, 1), (1, 0), (2, 0)]

    # Full grid of matches
    assert module_0.get_row([[1, 1], [1, 1]], 1) == [(0, 1), (0, 0), (1, 1), (1, 0)]

    # Value not present
    assert module_0.get_row([[1, 2], [3, 4]], 10) == []

    # Empty inputs
    assert module_0.get_row([], 1) == []
    assert module_0.get_row([[], []], 1) == []

    # Non-integer values
    assert module_0.get_row([['a', 'b'], ['b', 'a']], 'a') == [(0, 0), (1, 1)]

    # Single-element rows
    assert module_0.get_row([[5], [5], [5]], 5) == [(0, 0), (1, 0), (2, 0)]

    print("All get_row tests passed!")


if __name__ == "__main__":
    test_get_row()

# Generated at 2026-11-01 23:07:44.675495
# Unit test for function get_row
def test_get_row():
    # Empty list
    assert module_0.get_row([], 1) == []

    # Single element match
    assert module_0.get_row([[1]], 1) == [(0, 0)]

    # Multiple occurrences in same row: columns come in descending order
    assert module_0.get_row([[1, 2, 1, 3, 1]], 1) == [(0, 4), (0, 2), (0, 0)]

    # Classic case: rows ascending, columns descending within each row
    lst = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]]
    assert module_0.get_row(lst, 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Element not present
    assert module_0.get_row([[1, 2], [3, 4]], 5) == []

    # Ragged rows (different lengths)
    assert module_0.get_row([[1, 2], [2, 3, 2]], 2) == [(0, 1), (1, 2), (1, 0)]

    # Element in every row
    assert module_0.get_row([[9, 9], [9]], 9) == [(0, 1), (0, 0), (1, 0)]

    # Empty rows mixed in
    assert module_0.get_row([[], [1], []], 1) == [(1, 0)]

    # No match in a single row
    assert module_0.get_row([[1, 2, 3]], 10) == []

    print("All tests passed!")

# Generated at 2026-11-01 23:08:52.363957
# Unit test for function get_row
def test_get_row():
    # Coordinates sorted by row ascending, column descending within each row
    assert module_0.get_row(
        [[1, 2, 3, 4, 5, 6],
         [4, 4, 5, 1, 2, 9],
         [6, 4, 1, 4, 2, 2]],
        4
    ) == [(0, 3), (1, 1), (1, 0), (2, 3), (2, 1)]

    # Empty outer list -> no coordinates
    assert module_0.get_row([], 1) == []

    # Inner empty lists handled gracefully
    assert module_0.get_row([[], [1], []], 1) == [(1, 0)]

    # Value not present anywhere -> empty result
    assert module_0.get_row([[1, 2], [3, 4]], 5) == []

    # Single occurrence
    assert module_0.get_row([[10, 20, 30]], 30) == [(0, 2)]

    # Duplicates in the same row come out in descending column order
    assert module_0.get_row([[7, 7, 7]], 7) == [(0, 2), (0, 1), (0, 0)]

    # Ragged rows of differing lengths
    assert module_0.get_row([[1], [1, 2], [], [2, 1]], 1) == [(0, 0), (1, 0), (3, 1)]

    # Multiple matches across rows preserve row-major ordering
    assert module_0.get_row([[5, 5], [5], [5, 5, 5]], 5) == [
        (0, 1), (0, 0), (1, 0), (2, 2), (2, 1), (2, 0)
    ]

    # Rows with no match are skipped
    assert module_0.get_row([[1, 2], [3, 9], [2, 2]], 2) == [(0, 1), (2, 1), (2, 0)]