# file: project/pymonet/either.py:37-46
# asked: {"lines": [46], "branches": []}
# gained: {"lines": [46], "branches": []}

from pymonet.either import Either, Right


def test_either_ap_applies_contained_function_to_right():
    function_either = Either(lambda value: value * 2)

    result = function_either.ap(Right(21))

    assert isinstance(result, Right)
    assert result.value == 42
