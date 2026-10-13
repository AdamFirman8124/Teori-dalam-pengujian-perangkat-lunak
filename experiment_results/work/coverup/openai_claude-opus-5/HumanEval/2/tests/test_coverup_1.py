# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

import pytest

from script_2 import truncate_number


def test_truncate_number_returns_decimal_part():
    assert truncate_number(3.5) == pytest.approx(0.5)


def test_truncate_number_edge_cases():
    assert truncate_number(2.0) == pytest.approx(0.0)
    assert truncate_number(7.25) == pytest.approx(0.25)
    assert truncate_number(0.75) == pytest.approx(0.75)
    result = truncate_number(10.999)
    assert 0.0 <= result < 1.0
    assert pytest.approx(0.999, abs=1e-9) == result
