# file: project/pymonet/either.py:106-111
# asked: {"lines": [111], "branches": []}
# gained: {"lines": [111], "branches": []}

from pymonet.either import Left


def test_left_ap_returns_copy_with_same_value():
    value = object()
    original = Left(value)

    result = original.ap(object())

    assert isinstance(result, Left)
    assert result is not original
    assert result.value is value
