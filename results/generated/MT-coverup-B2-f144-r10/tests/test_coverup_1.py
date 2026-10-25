# file: project/f144/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}

import pytest

from f144 import simplify


def test_simplify_true():
    """3/2 * 2/3 = 1 -> integer result, returns True."""
    assert simplify("3/2", "2/3") is True


def test_simplify_false():
    """1/2 * 1/3 = 1/6 -> non-integer result, returns False."""
    assert simplify("1/2", "1/3") is False
