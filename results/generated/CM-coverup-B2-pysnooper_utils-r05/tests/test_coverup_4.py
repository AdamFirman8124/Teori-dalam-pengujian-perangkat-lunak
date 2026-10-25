# file: project/pysnooper/utils.py:81-87
# asked: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}
# gained: {"lines": [82, 83, 85, 86, 87], "branches": [[82, 83], [82, 85]]}

import pytest

from pysnooper.utils import truncate


def test_truncate_short_string_returns_unchanged():
    assert truncate('hello', 10) == 'hello'


def test_truncate_none_max_length_returns_unchanged():
    assert truncate('a very long string indeed', None) == 'a very long string indeed'


def test_truncate_exact_length_returns_unchanged():
    assert truncate('hello', 5) == 'hello'


def test_truncate_long_string_is_truncated():
    result = truncate('abcdefghijklmnopqrstuvwxyz', 10)
    # left = (10 - 3) // 2 = 3, right = 10 - 3 - 3 = 4
    assert result == 'abc...wxyz'
    assert len(result) == 10


def test_truncate_odd_max_length():
    result = truncate('abcdefghijklmnop', 9)
    # left = (9 - 3) // 2 = 3, right = 9 - 3 - 3 = 3
    assert result == 'abc...nop'
    assert len(result) == 9
