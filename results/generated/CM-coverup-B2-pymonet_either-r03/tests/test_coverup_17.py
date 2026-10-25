# file: project/pymonet/either.py:120-125
# asked: {"lines": [125], "branches": []}
# gained: {"lines": [125], "branches": []}

from pymonet.either import Left


def test_left_is_right_returns_false():
    """Left.is_right() must return False (covers line 125)."""
    left = Left(None)
    assert left.is_right() is False
