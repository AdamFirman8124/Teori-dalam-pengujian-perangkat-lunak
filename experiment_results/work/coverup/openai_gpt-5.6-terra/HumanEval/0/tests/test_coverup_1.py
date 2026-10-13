# file: script_0.py:4-19
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}

from script_0 import has_close_elements


def test_has_close_elements_returns_true_for_distinct_close_values():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0], 0.3) is True


def test_has_close_elements_returns_false_when_no_distance_is_below_threshold():
    assert has_close_elements([1.0, 2.0, 3.0], 1.0) is False
