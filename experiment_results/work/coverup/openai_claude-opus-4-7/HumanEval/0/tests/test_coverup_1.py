# file: script_0.py:4-19
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}

import pytest
from typing import List


def test_has_close_elements_returns_true_when_close_pair_exists():
    from script_0 import has_close_elements

    result = has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    assert result is True


def test_has_close_elements_returns_false_when_no_close_pair():
    from script_0 import has_close_elements

    result = has_close_elements([1.0, 2.0, 3.0], 0.5)
    assert result is False


def test_has_close_elements_single_element_returns_false():
    from script_0 import has_close_elements

    result = has_close_elements([5.0], 10.0)
    assert result is False


def test_has_close_elements_empty_list_returns_false():
    from script_0 import has_close_elements

    result = has_close_elements([], 1.0)
    assert result is False


def test_has_close_elements_exact_threshold_not_close():
    from script_0 import has_close_elements

    result = has_close_elements([0.0, 1.0], 1.0)
    assert result is False


def test_has_close_elements_duplicate_values():
    from script_0 import has_close_elements

    result = has_close_elements([2.0, 2.0], 0.001)
    assert result is True


def test_has_close_elements_negative_numbers():
    from script_0 import has_close_elements

    result = has_close_elements([-1.0, -1.5, -10.0], 1.0)
    assert result is True
