

# Generated at 2026-11-02 12:18:08.845858
# Unit test for function get_row
def test_get_row():
    # Test with sorted 2D list, x appears once
    assert module_0.get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) == [(1, 1)]

    # Test with sorted 2D list, x appears multiple times
    assert module_0.get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3) == [(0, 2)]
    assert module_0.get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [(0, 0)]
    assert module_0.get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9) == [(2, 2)]

    # Test with x appearing multiple times in the same row (columns reversed)
    assert module_0.get_row([[1, 2, 2, 3], [4, 2, 2, 2], [5, 6, 2, 2]], 2) == [(0, 2), (0, 1), (1, 3), (1, 2), (1, 1), (2, 3), (2, 2)]

    # Test with x not in the list
    assert module_0.get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 10) == []

    # Test with empty list
    assert module_0.get_row([], 1) == []

    # Test with list of empty rows
    assert module_0.get_row([[], [], []], 1) == []

    # Test with single element list
    assert module_0.get_row([[1]], 1) == [(0, 0)]

    # Test with rows of varying lengths
    assert module_0.get_row([[1], [1, 2], [1, 2, 3]], 1) == [(0, 0), (1, 0), (2, 0)]

    # Test with negative numbers
    assert module_0.get_row([[-1, -2], [-3, -1]], -1) == [(0, 0), (1, 1)]

    print("All test cases passed!")


if __name__ == "__main__":
    test_get_row()

# Generated at 2026-11-02 12:18:50.706751
# Unit test for function get_row
def test_get_row():
    # Empty list
    assert module_0.get_row([], 1) == []

    # List with empty rows
    assert module_0.get_row([[], []], 1) == []

    # Single element, found
    assert module_0.get_row([[1]], 1) == [(0, 0)]

    # Single element, not found
    assert module_0.get_row([[1]], 2) == []

    # Element not present anywhere
    assert module_0.get_row([[1, 2], [3, 4]], 5) == []

    # Typical case: rows ascending, columns descending within each row
    assert module_0.get_row(
        [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 1, 6], [1, 2, 3, 4, 5, 1]], 1
    ) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Multiple matches in one row: columns must be descending
    assert module_0.get_row([[1, 2, 1, 3, 1]], 1) == [(0, 4), (0, 2), (0, 0)]

    # Multiple matches in multiple rows
    assert module_0.get_row([[1, 1], [1, 1]], 1) == [(0, 1), (0, 0), (1, 1), (1, 0)]

    # Match appears only in a later row
    assert module_0.get_row([[], [1], [1, 2, 3]], 2) == [(2, 2)]

    # Zero as the target value
    assert module_0.get_row([[0, 1], [1, 0]], 0) == [(0, 0), (1, 1)]

    # Non-integer values
    assert module_0.get_row([['a', 'b'], ['a']], 'a') == [(0, 0), (1, 0)]

    # Ragged rows of differing lengths
    assert module_0.get_row([[9, 8, 7], [9], [9, 9]], 9) == [(0, 0), (1, 0), (2, 1), (2, 0)]

    print("All tests passed!")


test_get_row()

# Generated at 2026-11-02 12:19:34.584512
# Unit test for function get_row
def test_get_row():
    # Test with a typical 2D list, multiple occurrences of x
    assert module_0.get_row([[1, 2, 3, 4, 5, 6],
                    [1, 2, 3, 4, 1, 6],
                    [1, 2, 3, 4, 5, 1]], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Test with an empty outer list
    assert module_0.get_row([], 1) == []

    # Test with empty rows mixed in
    assert module_0.get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]

    # Test when x is not present
    assert module_0.get_row([[1, 2, 3], [4, 5, 6]], 7) == []

    # Test with a single element matching
    assert module_0.get_row([[5]], 5) == [(0, 0)]

    # Test with a single element not matching
    assert module_0.get_row([[5]], 3) == []

    # Test with all rows containing x, columns sorted descending per row
    assert module_0.get_row([[2, 2, 2], [2, 2, 2]], 2) == [(0, 2), (0, 1), (0, 0), (1, 2), (1, 1), (1, 0)]

    # Test with negative numbers
    assert module_0.get_row([[-1, 0, -1], [0, -1, 0]], -1) == [(0, 2), (0, 0), (1, 1)]

    # Test result ordering: rows ascending, columns descending within each row
    result = module_0.get_row([[9, 1, 9], [1, 9, 9]], 9)
    assert result == [(0, 2), (0, 0), (1, 2), (1, 1)]

    print("All tests passed!")


if __name__ == "__main__":
    test_get_row()

# Generated at 2026-11-02 12:20:14.592862
# Unit test for function get_row
def test_get_row():
    # Basic case: element appears in multiple rows
    assert module_0.get_row([[1, 2, 3, 4, 5, 6],
                    [1, 2, 3, 4, 1, 6],
                    [1, 2, 3, 4, 5, 1]], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Element appears once
    assert module_0.get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) == [(1, 1)]

    # Element not present
    assert module_0.get_row([[1, 2], [3, 4]], 10) == []

    # Empty outer list
    assert module_0.get_row([], 1) == []

    # Rows that are empty lists
    assert module_0.get_row([[], []], 1) == []

    # Single element match
    assert module_0.get_row([[1]], 1) == [(0, 0)]

    # Multiple matches in the same row -> columns sorted descending
    assert module_0.get_row([[1, 1, 1]], 1) == [(0, 2), (0, 1), (0, 0)]

    # Ragged (non-rectangular) list
    assert module_0.get_row([[1], [1, 2], [2, 1]], 1) == [(0, 0), (1, 0), (2, 1)]

    # Searching for zero
    assert module_0.get_row([[0], [1, 0]], 0) == [(0, 0), (1, 1)]

    # Works with non-integer elements
    assert module_0.get_row([['a', 'b'], ['b']], 'b') == [(0, 1), (1, 0)]

    # Row order preserved even when later row matches come first in scan
    assert module_0.get_row([[2], [1, 2]], 2) == [(0, 0), (1, 1)]

    print("All tests passed!")


if __name__ == "__main__":
    test_get_row()

# Generated at 2026-11-02 12:21:03.948105
# Unit test for function get_row
def test_get_row():
# nonce:34ba6669
    # Empty list
    assert module_0.get_row([], 1) == []

    # Single element, no match
    assert module_0.get_row([[1]], 2) == []

    # Single element, match
    assert module_0.get_row([[1]], 1) == [(0, 0)]

    # Multiple rows and columns, sorted by row asc then column desc
    assert module_0.get_row([[1, 2, 3, 4, 5, 6],
                    [1, 2, 3, 4, 1, 6],
                    [1, 2, 3, 4, 5, 1]], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

    # Empty sublists
    assert module_0.get_row([[], [1], [1, 2, 3]], 2) == [(2, 2)]

    # Value appearing multiple times in the same row (columns descending)
    assert module_0.get_row([[3, 3, 3]], 3) == [(0, 2), (0, 1), (0, 0)]

    # Value not present anywhere
    assert module_0.get_row([[1, 2], [3, 4]], 99) == []

    # Match in first row only
    assert module_0.get_row([[5, 5], [6, 7]], 5) == [(0, 1), (0, 0)]

    # Larger grid, check ordering across rows
    assert module_0.get_row([[0, 1, 2], [2, 2, 0], [1, 2, 0]], 0) == [(0, 0), (1, 2), (2, 2)]

    print("All tests passed!")


if __name__ == "__main__":
    test_get_row()