# file: project/pymonet/either.py:37-46
# asked: {"lines": [46], "branches": []}
# gained: {"lines": [46], "branches": []}

from pymonet.either import Right, Left


def test_right_ap_executes_either_ap_line_46():
    """Right.ap is inherited from Either, so calling it executes
    line 46: `return applicative.map(self.value)`.

    Semantics: self holds the function, the applicative holds the value,
    so the result is Right(applicative.value(self.value)).
    """
    function = Right(lambda x: x + 1)
    result = function.ap(Right(3))

    assert isinstance(result, Right)
    assert result.value == 4


def test_right_ap_with_left_applicative_executes_either_ap_line_46():
    """Even when the applicative is a Left, Right.ap still executes
    line 46 (the Left's map short-circuits and returns a Left)."""
    function = Right(lambda x: x + 1)
    result = function.ap(Left(3))

    assert isinstance(result, Left)
    assert result.is_left()
    assert not result.is_right()
