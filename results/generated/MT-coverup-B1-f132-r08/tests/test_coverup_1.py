# file: project/f132/__init__.py:1-18
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], "branches": [[5, 6], [5, 10], [6, 7], [6, 9], [14, 15], [14, 18], [15, 14], [15, 16]]}

from f132 import is_nested


def test_double_nested_true():
    assert is_nested("[[]]") is True


def test_sequential_not_nested():
    assert is_nested("[][]") is False


def test_empty_string():
    assert is_nested("") is False


def test_only_opening_brackets():
    assert is_nested("[[") is False


def test_only_closing_brackets():
    assert is_nested("]]") is False


def test_single_pair_not_nested():
    assert is_nested("[]") is False


def test_triple_nested_true():
    assert is_nested("[[[]]]") is True


def test_unbalanced_open_extra_covers_i_ge_l():
    assert is_nested("[[[]]") is True
