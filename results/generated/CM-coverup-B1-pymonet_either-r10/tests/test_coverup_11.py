# file: project/pymonet/either.py:37-46
# asked: {"lines": [46], "branches": []}
# gained: {"lines": [46], "branches": []}

from pymonet.either import Left, Right


def test_right_ap_executes_line_46():
    """Right.ap must execute `return applicative.map(self.value)`.

    In this implementation the receiver's value is the function and the
    applicative's value is the argument: applicative.map(self.value) applies
    self.value (the function) to the applicative's wrapped value.
    """
    add_ten = lambda x: x + 10

    result = Right(add_ten).ap(Right(5))

    assert isinstance(result, Right)
    assert result.value == 15
    assert not result.is_left()
    assert result.is_right()


def test_right_ap_with_value_returning_function():
    """Verify postcondition: result is Right containing the receiver's
    function applied to the applicative's value."""
    double = lambda x: x * 2

    result = Right(double).ap(Right(21))

    assert isinstance(result, Right)
    assert result.value == 42


def test_right_ap_does_not_mutate_operands():
    """ap must not mutate the receiver or the applicative."""
    func = lambda x: x + 1
    applicative = Right(1)
    receiver = Right(func)

    result = receiver.ap(applicative)

    assert receiver.value is func
    assert applicative.value == 1
    assert result.value == 2
