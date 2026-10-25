# file: project/pymonet/either.py:106-111
# asked: {"lines": [111], "branches": []}
# gained: {"lines": [111], "branches": []}

from pymonet.either import Left


def test_left_ap_returns_a_new_left_with_the_same_value():
    original = Left("error")
    applicative = object()

    result = original.ap(applicative)

    assert isinstance(result, Left)
    assert result is not original
    assert result.value == original.value == "error"
