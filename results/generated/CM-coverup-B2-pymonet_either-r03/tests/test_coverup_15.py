# file: project/pymonet/either.py:106-111
# asked: {"lines": [111], "branches": []}
# gained: {"lines": [111], "branches": []}

from pymonet.either import Left


def test_left_ap_returns_copy_with_same_value():
    value = object()
    left = Left(value)
    monad = object()

    result = left.ap(monad)

    assert isinstance(result, Left)
    assert result is not left
    assert result.value is value
    assert left.value is value
