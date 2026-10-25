# file: project/pymonet/either.py:37-46
# asked: {"lines": [46], "branches": []}
# gained: {"lines": [46], "branches": []}

from pymonet.either import Right, Left


def test_right_ap_executes_either_ap_line_46():
    """Right.ap is inherited from Either, so calling it executes
    line 46: `return applicative.map(self.value)`.

    Semantics: self.value is the function, applicative holds the argument,
    so the result is applicative.map(self.value) -> Right(f(arg)).
    """
    right = Right(lambda x: x + 1)
    result = right.ap(Right(3))

    assert isinstance(result, Right)
    assert result.value == 4


def test_right_ap_with_left_applicative_executes_either_ap_line_46():
    """Even when the applicative is a Left, Right.ap still executes
    line 46 (the Left's map short-circuits and returns a Left)."""
    right = Right(lambda x: x + 1)
    result = right.ap(Left(3))

    assert isinstance(result, Left)
    assert result.is_left()
    assert not result.is_right()
