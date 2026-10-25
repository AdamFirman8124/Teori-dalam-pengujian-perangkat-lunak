# file: project/f069/__init__.py:1-21
# asked: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}
# gained: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}

import pytest

from f069 import search


def test_search_basic():
    assert search([4, 1, 2, 2, 3, 1]) == 2


def test_search_multiple_candidates_returns_greatest():
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3


def test_search_no_valid_value_returns_minus_one():
    assert search([5, 5, 4, 4, 4]) == -1


def test_search_single_element():
    assert search([1]) == 1


def test_search_all_ones():
    assert search([1, 1, 1]) == 1


def test_search_frequency_exactly_equal():
    assert search([2, 2]) == 2
