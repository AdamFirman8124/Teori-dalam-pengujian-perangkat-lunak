# file: project/pymonet/either.py:113-118
# asked: {"lines": [118], "branches": []}
# gained: {"lines": [118], "branches": []}

import pytest

from pymonet.either import Left


def test_left_is_left_returns_true():
    """Cover Left.is_left (line 118): must return True."""
    left = Left("error value")

    result = left.is_left()

    assert result is True


def test_left_is_left_on_various_values():
    """Cover Left.is_left with different wrapped values."""
    assert Left(None).is_left() is True
    assert Left(0).is_left() is True
    assert Left(Exception("boom")).is_left() is True
