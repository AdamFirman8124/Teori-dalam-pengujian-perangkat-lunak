# file: project/f092/__init__.py:1-8
# asked: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}
# gained: {"lines": [4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 6], [5, 7]]}

import pytest

from f092 import any_int


@pytest.mark.parametrize(
    ("x", "y", "z"),
    [
        (5, 2, 7),      # x + y == z
        (3, 10, 7),     # x + z == y
        (9, 2, 7),      # y + z == x
        (-1, -2, -3),   # works with negatives
        (0, 0, 0),      # degenerate case
    ],
)
def test_any_int_returns_true_when_a_pair_sums_to_the_third(x, y, z):
    result = any_int(x, y, z)
    assert result is True
    assert (x + y == z) or (x + z == y) or (y + z == x)


@pytest.mark.parametrize(
    ("x", "y", "z"),
    [
        (1, 2, 4),      # ints, but no pair sums to the third
        (-1, 5, 3),     # negatives, still no match
    ],
)
def test_any_int_returns_false_for_ints_without_matching_sum(x, y, z):
    result = any_int(x, y, z)
    assert result is False
    assert not ((x + y == z) or (x + z == y) or (y + z == x))


@pytest.mark.parametrize(
    ("x", "y", "z"),
    [
        (2.5, 2, 3),    # x is not an int (short-circuits on first check)
        (2, 2.5, 3),    # y is not an int (short-circuits on second check)
        (2, 3, 4.5),    # z is not an int (third check reached)
        ("2", 3, 5),    # x is a string
        (2, None, 3),   # y is None
    ],
)
def test_any_int_returns_false_for_non_int_arguments(x, y, z):
    assert any_int(x, y, z) is False
