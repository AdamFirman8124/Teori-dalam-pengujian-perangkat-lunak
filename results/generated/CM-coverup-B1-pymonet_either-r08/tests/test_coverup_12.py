# file: project/pymonet/either.py:81-82
# asked: {"lines": [82], "branches": []}
# gained: {"lines": [82], "branches": []}

from pymonet.either import Either


def test_either_is_right_base_implementation_returns_none():
    either = Either("value")

    assert either.is_right() is None
