# file: project/f037/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[7, 8], [7, 9], [9, 10], [9, 11]]}

from f037 import sort_even


def test_sort_even_even_length_reorders():
    """Even-length list: exercises lines 3-8 and the False branch of line 9."""
    original = [5, 6, 3, 4]
    result = sort_even(original)
    # evens [5, 3] -> sorted [3, 5]; odds [6, 4] stay in place
    assert result == [3, 6, 5, 4]
    # the input list must not be mutated (evens is a slice copy)
    assert original == [5, 6, 3, 4]


def test_sort_even_odd_length_appends_last_even():
    """Odd-length list: exercises the True branch of lines 9-10."""
    result = sort_even([1, 2, 3])
    # evens [1, 3] -> sorted [1, 3]; odds [2]; leftover even 3 appended
    assert result == [1, 2, 3]


def test_sort_even_odd_length_unsorted():
    """Odd-length list whose even indices need reordering."""
    result = sort_even([4, 1, 3, 2, 2, 5])
    # evens [4, 3, 2] -> sorted [2, 3, 4]; odds [1, 2, 5] stay in place
    assert result == [2, 1, 3, 2, 4, 5]


def test_sort_even_empty_list():
    """Empty list: lines 3-6 run, loop body skipped, False branch of line 9."""
    assert sort_even([]) == []


def test_sort_even_single_element():
    """Single element: loop body skipped, True branch appends the lone even."""
    assert sort_even([7]) == [7]
