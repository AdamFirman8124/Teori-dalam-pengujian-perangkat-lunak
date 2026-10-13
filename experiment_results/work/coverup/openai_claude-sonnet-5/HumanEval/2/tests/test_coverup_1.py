# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

import pytest

from script_2 import truncate_number


def test_truncate_number_basic():
    assert truncate_number(3.5) == 0.5
    assert truncate_number(4.0) == 0.0
    assert truncate_number(1.25) == pytest.approx(0.25)


def test_truncate_number_postconditions():
    for value in (3.5, 7.0, 0.125, 12.75):
        result = truncate_number(value)
        assert 0.0 <= result < 1.0
        assert value % 1.0 == result
        assert float(int(value)) + result == pytest.approx(value)
