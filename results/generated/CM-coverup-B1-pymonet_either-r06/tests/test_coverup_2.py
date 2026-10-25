# file: project/pymonet/either.py:17-20
# asked: {"lines": [18, 19, 20], "branches": []}
# gained: {"lines": [18, 19, 20], "branches": []}

from pymonet.either import Either, Left, Right


def test_eq_right_with_equal_right():
    assert Right(1) == Right(1)
    assert (Right(1) == Right(1)) is True


def test_eq_left_with_equal_left():
    assert Left(1) == Left(1)
    assert (Left(1) == Left(1)) is True


def test_eq_right_with_different_value_is_false():
    assert (Right(1) == Right(2)) is False


def test_eq_left_with_different_value_is_false():
    assert (Left(1) == Left(2)) is False


def test_eq_right_with_left_same_value_is_false():
    # value equality holds, but is_right() differs -> third condition decides
    assert (Right(1) == Left(1)) is False
    assert (Left(1) == Right(1)) is False


def test_eq_with_non_either_is_false():
    # isinstance(other, Either) is False -> short-circuits before .value access
    assert (Right(1) == 1) is False
    assert (Left(1) == 1) is False
    assert (Right(1) == object()) is False
    assert (Right(1) == None) is False


def test_eq_with_non_either_lacking_value_attribute():
    class NoValue:
        pass

    # must not raise AttributeError thanks to the isinstance short-circuit
    assert (Right(1) == NoValue()) is False


def test_eq_is_symmetric_and_reflexive():
    right = Right('a')
    left = Left('a')
    assert right == right
    assert left == left
    assert (right == left) == (left == right)


def test_eq_does_not_mutate_operands():
    right = Right(5)
    left = Left(5)
    before = (right.value, left.value, right.is_right(), left.is_right())
    right == left
    left == right
    after = (right.value, left.value, right.is_right(), left.is_right())
    assert before == after
