# file: project/pymonet/either.py:113-118
# asked: {"lines": [118], "branches": []}
# gained: {"lines": [118], "branches": []}

from pymonet.either import Left


def test_left_is_left_returns_true():
    left = Left("error")

    result = left.is_left()

    assert result is True
