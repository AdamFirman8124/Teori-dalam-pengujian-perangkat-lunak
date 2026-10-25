# file: project/f052/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[3, 4], [3, 6], [4, 3], [4, 5]]}

import pytest

from f052 import below_threshold


def test_empty_list_returns_true():
    # Covers line 6 via loop that never executes (empty list)
    assert below_threshold([], 10) is True


def test_all_elements_below_threshold():
    # Covers lines 3 and 6: loop runs fully, no element >= t
    assert below_threshold([1, 2, 3], 10) is True


def test_element_equal_to_threshold_returns_false():
    # Covers lines 3-5: boundary case e == t triggers early return False
    assert below_threshold([1, 5, 3], 5) is False


def test_element_above_threshold_returns_false():
    # Covers lines 3-5: e > t triggers early return False
    assert below_threshold([1, 2, 99], 10) is False


def test_early_return_skips_rest_of_list():
    # Covers lines 3-5: first element triggers return, rest never examined
    assert below_threshold([10, -5, -5], 1) is False
