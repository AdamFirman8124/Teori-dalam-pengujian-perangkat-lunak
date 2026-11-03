# file: project/f144/__init__.py:1-9
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9], "branches": [[7, 8], [7, 9]]}

import pytest

from f144 import simplify


@pytest.mark.parametrize(
    "x, n, expected",
    [
        # True branch (line 8): product of fractions is a whole number
        ("1/2", "4/2", True),     # 1*4 / (2*2) = 4/4 = 1
        ("3/1", "2/1", True),     # 6/1 = 6
        ("-1/2", "4/1", True),    # -4/2 = -2 (negative whole number)
        ("0/1", "5/3", True),     # 0/15 = 0 (zero is whole)
        # False branch (line 9): product is not a whole number
        ("1/2", "2/3", False),    # 2/6 = 1/3
        ("7/4", "1/3", False),    # 7/12
        ("-1/2", "3/1", False),   # -3/2 = -1.5 (truncation must not fool the check)
    ],
)
def test_simplify_covers_both_branches(x, n, expected):
    # Exercise lines 3-9: splitting, int conversion, multiplication, and both
    # outcomes of the whole-number check.
    result = simplify(x, n)
    # Postcondition: result is a bool matching the expected whole-number verdict.
    assert isinstance(result, bool)
    assert result is expected


def test_simplify_true_branch_explicit():
    # 1/5 * 10/2 = 10/10 = 1 -> must return True (line 8)
    assert simplify("1/5", "10/2") is True


def test_simplify_false_branch_explicit():
    # 1/3 * 1/3 = 1/9 -> must return False (line 9)
    assert simplify("1/3", "1/3") is False
