# file: project/pymonet/either.py:127-136
# asked: {"lines": [134, 136], "branches": []}
# gained: {"lines": [134, 136], "branches": []}

from pymonet.either import Left
from pymonet.maybe import Maybe


def test_left_to_maybe_returns_nothing_and_discards_left_value():
    payload = object()
    left = Left(payload)

    result = left.to_maybe()

    assert isinstance(result, Maybe)
    assert result.is_nothing is True
    assert not hasattr(result, "value")
    assert left.value is payload
    assert left.is_left() is True
    assert left.is_right() is False
