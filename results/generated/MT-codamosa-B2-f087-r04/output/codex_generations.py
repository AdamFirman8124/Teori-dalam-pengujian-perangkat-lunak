

# Generated at 2026-11-02 08:14:31.214370
# Unit test for function get_row
def test_get_row():
    # Multiple occurrences across rows: rows ascending, columns descending
    assert module_0.get_row([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Empty input list
    assert module_0.get_row([], 1) == []

    # Rows of varying lengths, including empty rows
    assert module_0.get_row([[], [1], [1, 2, 3]], 1) == [(1, 0), (2, 0)]

    # Value not present anywhere
    assert module_0.get_row([[1, 2, 3], [4, 5, 6]], 7) == []

    # Multiple occurrences within the same row (column order descending)
    assert module_0.get_row([[1, 1], [1, 1]], 1) == [(0, 1), (0, 0), (1, 1), (1, 0)]

    # Single occurrence
    assert module_0.get_row([[10, 20], [30, 40]], 40) == [(1, 1)]

    # First row occurrence
    assert module_0.get_row([[5, 6, 7], [8, 9, 10]], 5) == [(0, 0)]

    # Non-integer values
    assert module_0.get_row([['a', 'b'], ['b', 'a']], 'a') == [(0, 0), (1, 1)]

    # Nested empty structure search
    assert module_0.get_row([[], [], []], 0) == []

# Generated at 2026-11-02 08:15:09.701157
# Unit test for function get_row
def test_get_row():
    # Basic case: multiple matches across rows, columns sorted descending within each row
    assert module_0.get_row([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Empty outer list
    assert module_0.get_row([], 1) == []

    # Empty sublists mixed with non-empty ones
    assert module_0.get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]

    # Value not present anywhere
    assert module_0.get_row([[1, 2], [3, 4]], 5) == []

    # Multiple matches in a single row -> descending column order
    assert module_0.get_row([[1, 1, 1]], 1) == [(0, 2), (0, 1), (0, 0)]

    # One match per row -> rows in ascending order
    assert module_0.get_row([[2], [2], [2]], 2) == [(0, 0), (1, 0), (2, 0)]

    # Works with strings
    assert module_0.get_row([['a', 'b'], ['a']], 'a') == [(0, 0), (1, 0)]

    # Works with negative numbers
    assert module_0.get_row([[-1, 0], [-1]], -1) == [(0, 0), (1, 0)]

    print("All tests passed!")


test_get_row()

# Generated at 2026-11-02 08:16:30.484326
# Unit test for function get_row
def test_get_row():
    # nonce:4dd48ff3
    # Standard case: multiple rows with matches, multiple matches per row
    assert module_0.get_row([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1) == [
        (0, 0), (1, 4), (1, 0), (2, 5), (2, 0)
    ]
    # Empty list
    assert module_0.get_row([], 1) == []
    # Nested empty rows
    assert module_0.get_row([[], [], []], 1) == []
    # Single element match
    assert module_0.get_row([[1]], 1) == [(0, 0)]
    # No match found
    assert module_0.get_row([[1, 2], [3, 4]], 5) == []
    # Multiple matches in the same row (columns descending)
    assert module_0.get_row([[3, 3, 3]], 3) == [(0, 2), (0, 1), (0, 0)]
    # Match in a later row only
    assert module_0.get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    # Rows sorted ascending, columns descending within each row
    assert module_0.get_row([[0, 9], [9, 0], [9, 9]], 9) == [(0, 1), (1, 0), (2, 1), (2, 0)]
    # Non-integer values
    assert module_0.get_row([['a', 'b'], ['b', 'a']], 'a') == [(0, 0), (1, 1)]

    print("All test cases passed!")


test_get_row()

# Generated at 2026-11-02 08:18:01.885973
# Unit test for function get_row
def test_get_row():
    # Basic case: value appears in multiple rows and columns
    assert module_0.get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) == [(1, 1)]
    assert module_0.get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [(0, 0)]

    # Value appears multiple times in the same row (columns sorted descending)
    assert module_0.get_row([[1, 2, 1], [1, 1, 1]], 1) == [(0, 2), (0, 0), (1, 2), (1, 1), (1, 0)]

    # Value appears in multiple rows
    assert module_0.get_row([[1, 2], [3, 4], [1, 5]], 1) == [(0, 0), (2, 0)]

    # Value not present
    assert module_0.get_row([[1, 2, 3]], 99) == []

    # Empty list input
    assert module_0.get_row([], 1) == []

    # Rows of varying lengths (ragged list)
    assert module_0.get_row([[1], [1, 2], [1, 2, 1]], 1) == [(0, 0), (1, 0), (2, 2), (2, 0)]

    # Duplicates across rows and columns
    assert module_0.get_row([[3, 3, 3], [3], [2, 3]], 3) == [(0, 2), (0, 1), (0, 0), (1, 0), (2, 1)]

    # Works with strings as well
    assert module_0.get_row([["a", "b"], ["b", "a"]], "b") == [(0, 1), (1, 0)]

    # Row order must be ascending even if found later first
    assert module_0.get_row([[9, 5], [5, 9], [5, 5]], 5) == [(0, 1), (1, 0), (2, 1), (2, 0)]


if __name__ == "__main__":
    test_get_row()
    print("All tests passed!")

# Generated at 2026-11-02 08:19:27.130171
# Unit test for function get_row
def test_get_row():
    # nonce:c2966ee5
    # Test with a typical 2D list, multiple matches across rows
    assert module_0.get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Test with x appearing once per row
    assert module_0.get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 6) == [(0, 5), (1, 5)]

    # Test with x not present in the list
    assert module_0.get_row([
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 1, 6],
        [1, 2, 3, 4, 5, 1]
    ], 7) == []

    # Test with an empty list
    assert module_0.get_row([], 1) == []

    # Test with empty rows mixed in
    assert module_0.get_row([[], [1], [], [1, 1]], 1) == [(1, 0), (3, 1), (3, 0)]

    # Test with a single-element list
    assert module_0.get_row([[5]], 5) == [(0, 0)]
    assert module_0.get_row([[5]], 3) == []

    # Test with multiple occurrences in a single row (columns descending)
    assert module_0.get_row([[1, 1, 1]], 1) == [(0, 2), (0, 1), (0, 0)]

    # Test with rows of different lengths
    assert module_0.get_row([[2], [2, 2], [2, 2, 2]], 2) == [
        (0, 0), (1, 1), (1, 0), (2, 2), (2, 1), (2, 0)
    ]

    # Test with string elements
    assert module_0.get_row([['a', 'b'], ['b', 'a']], 'b') == [(0, 1), (1, 0)]

    # Test that rows appear in ascending order even if input rows are unordered
    assert module_0.get_row([
        [9, 9],
        [8, 8, 8],
        [9]
    ], 9) == [(0, 1), (0, 0), (2, 0)]