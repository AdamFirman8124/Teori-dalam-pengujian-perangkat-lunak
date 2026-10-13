# file: script_0.py:4-19
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}

from script_0 import has_close_elements


def test_has_close_elements_returns_false_when_no_pair_is_below_threshold():
    numbers = [1.0, 2.0]
    threshold = 0.5

    result = has_close_elements(numbers, threshold)

    assert result is False


def test_has_close_elements_returns_true_when_a_pair_is_below_threshold():
    numbers = [1.0, 1.2, 3.0]
    threshold = 0.3

    result = has_close_elements(numbers, threshold)

    assert result is True
