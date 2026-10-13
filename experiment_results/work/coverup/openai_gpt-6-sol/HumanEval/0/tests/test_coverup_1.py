# file: script_0.py:4-19
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}

from script_0 import has_close_elements


def test_returns_true_when_distinct_elements_are_close():
    numbers = [1.0, 2.8, 3.0, 4.0]
    assert has_close_elements(numbers, 0.3) is True
    assert numbers == [1.0, 2.8, 3.0, 4.0]


def test_returns_false_when_no_distinct_elements_are_close():
    numbers = [1.0, 2.0, 3.0]
    assert has_close_elements(numbers, 0.5) is False
    assert numbers == [1.0, 2.0, 3.0]


def test_returns_false_for_a_single_element():
    assert has_close_elements([1.0], 1.0) is False
