# file: project/pymonet/either.py:37-46
# asked: {"lines": [46], "branches": []}
# gained: {"lines": [46], "branches": []}

from pymonet.either import Right


def test_right_ap_applies_contained_function():
    result = Right(lambda value: value * 2).ap(Right(21))

    assert isinstance(result, Right)
    assert result.value == 42
