# file: project/f069/__init__.py:1-21
# asked: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}
# gained: {"lines": [12, 13, 14, 16, 17, 18, 19, 21], "branches": [[13, 14], [13, 16], [17, 18], [17, 21], [18, 17], [18, 19]]}

import pytest

from f069 import search


def test_search_returns_greatest_valid_value():
    # Covers lines 12-21: frequency counting and the search loop where
    # the condition frq[i] >= i is true for at least one value.
    assert search([4, 1, 2, 2, 3, 1]) == 2


def test_search_multiple_valid_values_picks_greatest():
    # Ensures the loop keeps updating 'ans' (line 19) for every valid i,
    # returning the greatest qualifying integer.
    assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3


def test_search_no_valid_value_returns_minus_one():
    # Covers the branch where frq[i] >= i is never true, so 'ans'
    # stays -1 (lines 16, 17, 18, 21 executed with the false branch).
    assert search([5, 5, 4, 4, 4]) == -1


def test_search_single_element_valid():
    # Minimal list where the single element qualifies (frequency 1 >= 1).
    assert search([1]) == 1


def test_search_single_element_invalid():
    # Minimal list where the single element does not qualify.
    assert search([2]) == -1


def test_search_all_ones():
    # Every 1 qualifies; result must be 1.
    assert search([1, 1, 1]) == 1
