# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

import pytest

from script_2 import truncate_number


def test_truncate_number_basic():
    assert truncate_number(3.5) == 0.5


def test_truncate_number_whole_number():
    assert truncate_number(5.0) == 0.0


def test_truncate_number_less_than_one():
    assert truncate_number(0.25) == 0.25


def test_truncate_number_irrational_fraction():
    result = truncate_number(1.23456)
    assert 0.0 <= result < 1.0
    assert result == pytest.approx(0.23456)
