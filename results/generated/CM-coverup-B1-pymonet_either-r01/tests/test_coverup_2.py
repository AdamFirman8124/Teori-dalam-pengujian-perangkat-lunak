# file: project/pymonet/either.py:17-20
# asked: {"lines": [18, 19, 20], "branches": []}
# gained: {"lines": [18, 19, 20], "branches": []}

from pymonet.either import Left, Right


def test_either_equality_returns_true_for_equal_right_values():
    first = Right(42)
    second = Right(42)

    assert first == second
    assert second == first


def test_either_equality_returns_false_for_different_values():
    first = Left("error")
    second = Left("other error")

    assert first != second


def test_either_equality_returns_false_for_non_either_and_different_variants():
    left = Left(42)
    right = Right(42)

    assert left != object()
    assert left != right
    assert right != left
