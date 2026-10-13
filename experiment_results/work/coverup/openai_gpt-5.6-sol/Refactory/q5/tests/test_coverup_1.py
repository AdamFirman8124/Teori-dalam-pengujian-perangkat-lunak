# file: script_q5.py:1-6
# asked: {"lines": [2, 3, 4, 5, 6], "branches": [[3, 4], [3, 6]]}
# gained: {"lines": [2, 3, 4, 5, 6], "branches": [[3, 4], [3, 6]]}

from script_q5 import top_k


def test_top_k_returns_largest_values_and_removes_them():
    values = [3, 1, 4, 2]

    result = top_k(values, 3)

    assert result == [4, 3, 2]
    assert values == [1]


def test_top_k_with_zero_k_returns_empty_list_without_mutating_input():
    values = [5, 2, 8]

    result = top_k(values, 0)

    assert result == []
    assert values == [5, 2, 8]


def test_top_k_handles_duplicate_maximum_values():
    values = [7, 3, 7, 1]

    result = top_k(values, 2)

    assert result == [7, 7]
    assert values == [3, 1]
