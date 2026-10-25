# file: project/pymonet/either.py:37-46
# asked: {"lines": [46], "branches": []}
# gained: {"lines": [46], "branches": []}

from pymonet.either import Either, Left, Right


def test_either_ap_applies_wrapped_function_to_right():
    applicative = Right(41)

    result = Either(lambda value: value + 1).ap(applicative)

    assert isinstance(result, Right)
    assert result.value == 42
    assert result is not applicative


def test_either_ap_preserves_left():
    applicative = Left("error")

    result = Either(lambda value: value + 1).ap(applicative)

    assert isinstance(result, Left)
    assert result.value == "error"
    assert result is not applicative
