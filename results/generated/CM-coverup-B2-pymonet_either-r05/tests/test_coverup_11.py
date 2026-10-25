# file: project/pymonet/either.py:37-46
# asked: {"lines": [46], "branches": []}
# gained: {"lines": [46], "branches": []}

from pymonet.either import Right


def test_right_ap_applies_wrapped_function():
    result = Right(lambda value: value * 2).ap(Right(21))

    assert result == Right(42)
    assert result.is_right()
    assert result.value == 42
