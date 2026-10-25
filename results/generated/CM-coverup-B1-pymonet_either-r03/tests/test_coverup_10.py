# file: project/pymonet/either.py:37-46
# asked: {"lines": [46], "branches": []}
# gained: {"lines": [46], "branches": []}

from pymonet.either import Either, Left, Right


def test_either_ap_with_right_applicative_executes_line_46():
    """Either.ap (base implementation, line 46) applied to a Right applicative.

    `self` holds the function and `applicative` holds the value, so the
    function is applied to the applicative's value via `applicative.map`.
    Right and Left both override `ap`, so the base Either.ap body is only
    reached by invoking it directly on an Either instance.
    """
    either = Right(lambda x: x * 3)
    applicative = Right(2)

    result = Either.ap(either, applicative)

    assert isinstance(result, Right)
    assert result.value == 6


def test_either_ap_with_left_applicative_executes_line_46():
    """Either.ap (base implementation, line 46) applied to a Left applicative.

    Left.map ignores the mapper and returns a copy of itself, so the
    function inside the Right is never applied.
    """
    either = Right(lambda x: x * 3)
    applicative = Left("error")

    result = Either.ap(either, applicative)

    assert isinstance(result, Left)
    assert result.value == "error"
