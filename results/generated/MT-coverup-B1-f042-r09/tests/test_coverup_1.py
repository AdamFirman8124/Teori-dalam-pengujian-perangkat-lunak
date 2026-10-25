# file: project/f042/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f042 import incr_list


def test_incr_list_returns_incremented_copy():
    original = [1, 2, 3]
    result = incr_list(original)

    assert result == [2, 3, 4]
    assert original == [1, 2, 3]
    assert result is not original


def test_incr_list_empty_list():
    assert incr_list([]) == []


def test_incr_list_negative_and_float_values():
    assert incr_list([-1, 0, 1.5]) == [0, 1, 2.5]
