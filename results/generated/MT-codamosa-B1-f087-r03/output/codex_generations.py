

# Generated at 2026-10-24 12:17:21.138728
# Unit test for function get_row

# Generated at 2026-10-24 12:17:23.772543
# Unit test for function get_row

# Generated at 2026-10-24 12:17:26.194066
# Unit test for function get_row

# Generated at 2026-10-24 12:17:28.609176
# Unit test for function get_row

# Generated at 2026-10-24 12:17:31.027964
# Unit test for function get_row

# Generated at 2026-10-24 12:17:33.446651
# Unit test for function get_row

# Generated at 2026-10-24 12:17:35.865644
# Unit test for function get_row

# Generated at 2026-10-24 12:17:47.543782
# Unit test for function get_row
def test_get_row():assert module_0.get_row([[1, 2, 1], [3, 1, 4]], 1) == [(0, 2), (0, 0), (1, 1)]

# Generated at 2026-10-24 12:18:01.383176
# Unit test for function get_row
def test_get_row():
    # basic single match
    assert module_0.get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) == [(1, 1)]

    # multiple matches in the same row -> columns descending
    assert module_0.get_row([[1, 2, 1]], 1) == [(0, 2), (0, 0)]

    # matches across rows -> rows ascending, columns descending within a row
    assert module_0.get_row([[1, 2, 1], [1]], 1) == [(0, 2), (0, 0), (1, 0)]

    # no match
    assert module_0.get_row([[1, 2], [3, 4]], 99) == []

    # empty input
    assert module_0.get_row([], 1) == []

    # empty rows / ragged input
    assert module_0.get_row([[], [1], []], 1) == [(1, 0)]

# Generated at 2026-10-24 12:18:02.707500
# Unit test for function get_row
def test_get_row():
    # basic single match
    assert module_0.get_row([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 5) == [(1, 1)]

    # multiple matches in the same row -> columns descending
    assert module_0.get_row([[1, 2, 1]], 1) == [(0, 2), (0, 0)]

    # matches across rows -> rows ascending, columns descending within a row
    assert module_0.get_row([[1, 2, 1], [1]], 1) == [(0, 2), (0, 0), (1, 0)]

    # no match
    assert module_0.get_row([[1, 2], [3, 4]], 99) == []

    # empty input
    assert module_0.get_row([], 1) == []

    # empty rows / ragged input
    assert module_0.get_row([[], [1], []], 1) == [(1, 0)]