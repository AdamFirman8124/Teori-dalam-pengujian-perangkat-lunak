# file: script_q1.py:2-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

from script_q1 import search


def test_search_returns_first_matching_index():
    assert search(3, [1, 3, 3, 5]) == 1


def test_search_returns_length_when_no_element_matches():
    assert search(6, [1, 3, 5]) == 3


def test_search_with_empty_sequence():
    assert search(1, []) == 0
