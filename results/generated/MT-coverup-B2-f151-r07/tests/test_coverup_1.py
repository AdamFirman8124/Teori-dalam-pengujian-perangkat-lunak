# file: project/f151/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f151 import double_the_difference


def test_double_the_difference_mixed_list_covers_all_branches():
    """Exercise every condition of the comprehension:
    - 3, 5: positive odd integers -> included (i > 0 True, i % 2 != 0 True, no '.')
    - 2: positive even -> excluded by i % 2 != 0
    - -3: negative odd -> excluded by i > 0
    - 0: excluded by i > 0
    - 1.5: positive odd-valued float -> excluded by '.' in str(i)
    """
    lst = [3, 2, -3, 0, 1.5, 5]
    result = double_the_difference(lst)
    assert result == 3 ** 2 + 5 ** 2
    assert result == 34


def test_double_the_difference_empty_list():
    """Line 3 must also execute for an empty input, yielding sum([]) == 0."""
    assert double_the_difference([]) == 0


def test_double_the_difference_all_excluded():
    """Every element fails at least one condition, so the comprehension
    yields an empty list and the sum is 0."""
    lst = [-1, -2, 4, 2.5, 0]
    assert double_the_difference(lst) == 0


def test_double_the_difference_only_positive_odds():
    """All elements pass all conditions; verify exact sum of squares."""
    lst = [1, 3, 7]
    assert double_the_difference(lst) == 1 + 9 + 49
    assert double_the_difference(lst) == 59
