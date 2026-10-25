# file: project/f149/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

from f149 import sorted_list_sum


def test_sorted_list_sum_filters_odd_lengths_and_sorts_by_length():
    values = ["ccc", "ee", "dddd", "b", "aa"]

    result = sorted_list_sum(values)

    assert result == ["aa", "ee", "dddd"]
    assert values == ["aa", "b", "ccc", "dddd", "ee"]
