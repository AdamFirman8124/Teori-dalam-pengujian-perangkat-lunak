# file: project/pymonet/either.py:106-111
# asked: {"lines": [111], "branches": []}
# gained: {"lines": [111], "branches": []}

from pymonet.either import Left


def test_left_ap_returns_copy_with_same_value():
    left = Left("error")

    result = left.ap(object())

    assert isinstance(result, Left)
    assert result.value == "error"
    assert result is not left
