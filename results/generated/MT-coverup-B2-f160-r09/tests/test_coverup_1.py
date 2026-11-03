# file: project/f160/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}
# gained: {"lines": [3, 4, 5, 6], "branches": [[4, 5], [4, 6]]}

import pytest

from f160 import do_algebra


# do_algebra is a pure function (no globals, I/O, or mutable state), so no
# monkeypatching/teardown is required; each test is fully self-contained.


@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        (["+"], [2, 3], 5),
        (["-"], [10, 4], 6),
        (["-"], [3, 10], -7),          # negative result still handled by eval
        (["*"], [3, 4], 12),
        (["//"], [9, 2], 4),           # floor division
        (["**"], [2, 3], 8),           # exponentiation
        (["+"], [12, 34], 46),         # multi-digit operands
    ],
    ids=["add", "sub", "sub-negative", "mul", "floordiv", "pow", "multidigit"],
)
def test_single_operator_executes_all_lines(operator, operand, expected):
    """A single call with one operator executes lines 3-6 and returns the
    correct arithmetic result."""
    result = do_algebra(operator, operand)
    assert result == expected


def test_multiple_operators_build_full_expression():
    """Several operators exercise the loop body repeatedly (line 5) and the
    built string is evaluated with normal Python precedence:
    '2+3*4-5' -> 2 + 12 - 5 == 9 (not (2+3)*4-5 == 15)."""
    result = do_algebra(["+", "*", "-"], [2, 3, 4, 5])
    assert result == 9
    assert result == eval("2+3*4-5")  # postcondition: eval semantics preserved


def test_all_same_operator_chains():
    """Repeated identical operators accumulate onto the expression string."""
    assert do_algebra(["+", "+", "+"], [1, 2, 3, 4]) == 10
    assert do_algebra(["*", "*"], [2, 3, 4]) == 24


def test_empty_operator_list_returns_first_operand():
    """With no operators the loop body (line 5) is skipped but lines 3, 4 and 6
    still run, returning the first operand unchanged."""
    assert do_algebra([], [42]) == 42
