# file: project/f092/__init__.py:1-8
# asked: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}
# gained: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}

import pytest

from f092 import any_int


def test_any_int_true_when_sum_matches():
    # x + y == z
    assert any_int(2, 3, 5) is True
    # x + z == y
    assert any_int(5, 3, -2) is True
    # y + z == x
    assert any_int(10, 4, 6) is True


def test_any_int_false_when_no_sum_matches():
    assert any_int(1, 2, 4) is False


def test_any_int_false_with_non_int_args():
    assert any_int(1.5, 2, 3) is False
    assert any_int(1, "2", 3) is False
    assert any_int(1, 2, None) is False
    # bool is a subclass of int; still counts as int here
    assert any_int(True, 2, 3) is True
