# file: script_0.py:4-19
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}

from script_0 import has_close_elements


def test_has_close_elements_returns_true_for_numbers_within_threshold():
    numbers = [1.0, 2.0, 2.2]

    result = has_close_elements(numbers, 0.3)

    assert result is True


def test_has_close_elements_returns_false_when_no_numbers_are_within_threshold():
    numbers = [1.0, 2.0, 3.0]

    result = has_close_elements(numbers, 0.5)

    assert result is False
