# file: script_2.py:1-10
# asked: {"lines": [10], "branches": []}
# gained: {"lines": [10], "branches": []}

import pytest


@pytest.fixture(autouse=True)
def _cleanup():
    yield
    # no global state is mutated by truncate_number; nothing to restore


def test_truncate_number_positive_decimal():
    from script_2 import truncate_number
    assert truncate_number(3.5) == pytest.approx(0.5)


def test_truncate_number_integer_part():
    from script_2 import truncate_number
    assert truncate_number(7.0) == pytest.approx(0.0)
    assert truncate_number(12.25) == pytest.approx(0.25)


def test_truncate_number_documented_result_type():
    from script_2 import truncate_number
    result = truncate_number(3.5)
    assert isinstance(result, float)
    assert 0.0 <= result < 1.0
