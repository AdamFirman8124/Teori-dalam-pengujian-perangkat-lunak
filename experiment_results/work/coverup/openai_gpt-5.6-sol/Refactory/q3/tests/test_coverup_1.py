# file: script_q3.py:3-8
# asked: {"lines": [4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

from script_q3 import remove_extras


def test_remove_extras_removes_duplicates_and_preserves_order():
    values = [3, 1, 3, 2, 1, 2]
    result = remove_extras(values)

    assert result == [3, 1, 2]
    assert values == [3, 1, 3, 2, 1, 2]


def test_remove_extras_returns_empty_list_for_empty_input():
    result = remove_extras([])

    assert result == []
