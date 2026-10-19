# file: project\f002\__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest
from f002 import truncate_number


def test_truncate_number_positive():
    result = truncate_number(1.5)
    assert result == 0.5


def test_truncate_number_negative():
    result = truncate_number(-1.5)
    assert result == 0.5


def test_truncate_number_zero():
    result = truncate_number(0.0)
    assert result == 0.0


def test_truncate_number_integer():
    result = truncate_number(5.0)
    assert result == 0.0


def test_truncate_number_small_fraction():
    result = truncate_number(0.001)
    assert result == 0.001
