# file: project/f020/__init__.py:4-21
# asked: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 21], "branches": [[9, 10], [9, 21], [10, 9], [10, 11], [11, 10], [11, 12], [12, 13], [12, 16], [17, 10], [17, 18]]}

import pytest

from f020 import find_closest_elements


def test_find_closest_elements_basic_pair():
    result = find_closest_elements([1.0, 2.0, 3.0])
    assert result == (1.0, 2.0)
    assert isinstance(result, tuple)
    assert result[0] <= result[1]


def test_find_closest_elements_improves_then_stops_improving():
    # First pair sets distance=9, later pair improves it to 1, then no further
    # improvement is found (covers the "new_distance < distance" false branch).
    result = find_closest_elements([1.0, 10.0, 2.0])
    assert result == (1.0, 2.0)
    assert result[0] <= result[1]


def test_find_closest_elements_equal_distance_keeps_first_pair():
    # Equal distances must not replace the stored pair (strict < comparison).
    result = find_closest_elements([0.0, 1.0, 2.0])
    assert result == (0.0, 1.0)


def test_find_closest_elements_duplicates():
    result = find_closest_elements([5.0, 5.0])
    assert result == (5.0, 5.0)


def test_find_closest_elements_unsorted_input_returns_sorted_pair():
    result = find_closest_elements([9.0, 4.0, 4.5, 100.0])
    assert result == (4.0, 4.5)
    assert result[0] <= result[1]


def test_find_closest_elements_single_element_returns_none():
    assert find_closest_elements([42.0]) is None


def test_find_closest_elements_empty_list_returns_none():
    assert find_closest_elements([]) is None
