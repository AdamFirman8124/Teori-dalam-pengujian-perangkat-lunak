# file: project/f002/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest
from f002 import truncate_number


def test_truncate_positive_fraction():
    assert truncate_number(3.5) == pytest.approx(0.5)


def test_truncate_integer_returns_zero():
    assert truncate_number(5.0) == pytest.approx(0.0)


def test_truncate_zero():
    assert truncate_number(0.0) == pytest.approx(0.0)


def test_truncate_negative():
    # Python modulo semantics: -2.3 % 1.0 == 0.7 (approx)
    assert truncate_number(-2.3) == pytest.approx(0.7)
    assert truncate_number(-1.0) == pytest.approx(0.0)
