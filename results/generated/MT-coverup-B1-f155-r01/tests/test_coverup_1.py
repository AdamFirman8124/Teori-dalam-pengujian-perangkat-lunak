# file: project/f155/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import pytest

from f155 import even_odd_count


def test_even_odd_count_mixed():
    assert even_odd_count(1234) == (2, 2)


def test_even_odd_count_all_even():
    assert even_odd_count(2468) == (4, 0)


def test_even_odd_count_all_odd():
    assert even_odd_count(1357) == (0, 4)


def test_even_odd_count_negative():
    assert even_odd_count(-123) == (1, 2)


def test_even_odd_count_zero():
    assert even_odd_count(0) == (1, 0)
