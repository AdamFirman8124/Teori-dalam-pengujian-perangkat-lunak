# file: project/pymonet/either.py:120-125
# asked: {"lines": [125], "branches": []}
# gained: {"lines": [125], "branches": []}

from pymonet.either import Left


def test_left_is_right_returns_false():
    left = Left("error")

    assert left.is_right() is False
