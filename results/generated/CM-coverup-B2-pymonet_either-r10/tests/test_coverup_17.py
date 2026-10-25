# file: project/pymonet/either.py:120-125
# asked: {"lines": [125], "branches": []}
# gained: {"lines": [125], "branches": []}

from pymonet.either import Left


def test_left_is_right_returns_false():
    left = Left("error")

    result = left.is_right()

    assert result is False
