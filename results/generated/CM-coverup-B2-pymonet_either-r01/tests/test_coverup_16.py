# file: project/pymonet/either.py:113-118
# asked: {"lines": [118], "branches": []}
# gained: {"lines": [118], "branches": []}

from pymonet.either import Left


def test_left_is_left_returns_true():
    error = object()
    left = Left(error)

    assert left.is_left() is True
    assert left.value is error
