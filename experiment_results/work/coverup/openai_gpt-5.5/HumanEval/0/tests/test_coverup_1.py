# file: script_0.py:4-19
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}

import pytest

from script_0 import has_close_elements


def test_has_close_elements_returns_true_for_pair_below_threshold():
    assert has_close_elements([1.0, 2.0, 2.2, 5.0], 0.25) is True


def test_has_close_elements_returns_false_when_no_pair_below_threshold():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) is False


def test_has_close_elements_returns_false_for_single_element():
    assert has_close_elements([1.0], 10.0) is False
