# file: project/pymonet/either.py:127-136
# asked: {"lines": [134, 136], "branches": []}
# gained: {"lines": [134, 136], "branches": []}

from pymonet.either import Left
from pymonet.maybe import Maybe


def test_left_to_maybe_returns_nothing():
    result = Left("error").to_maybe()

    assert isinstance(result, Maybe)
    assert result.is_nothing is True
    assert result == Maybe.nothing()
