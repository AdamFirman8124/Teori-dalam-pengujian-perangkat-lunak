# file: script_q1.py:2-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

from script_q1 import search


def test_search_returns_index_of_first_element_greater_than_or_equal_to_x():
    sequence = [1, 3, 5, 7]

    result = search(4, sequence)

    assert result == 2


def test_search_returns_sequence_length_when_x_is_greater_than_all_elements():
    sequence = [1, 3, 5, 7]

    result = search(8, sequence)

    assert result == len(sequence)
