# file: project/f002/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f002 import truncate_number


def test_truncate_number_integer_part():
    result = truncate_number(3.5)
    assert result == pytest.approx(0.5)


def test_truncate_number_whole_number():
    result = truncate_number(4.0)
    assert result == pytest.approx(0.0)


def test_truncate_number_negative():
    result = truncate_number(-1.25)
    assert result == pytest.approx(0.75)
