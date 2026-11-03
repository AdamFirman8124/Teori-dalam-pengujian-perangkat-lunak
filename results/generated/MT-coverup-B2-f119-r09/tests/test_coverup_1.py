# file: project/f119/__init__.py:1-29
# asked: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}

import pytest

from f119 import match_parens


@pytest.mark.parametrize(
    "lst, expected",
    [
        # check(S1) succeeds: covers '(' increment (lines 19-20), ')' decrement
        # without going negative (lines 21-22), and the val == 0 -> True branch
        # of the final ternary in check (line 25), plus the 'Yes' return (line 29).
        (["()(", ")"], "Yes"),
        # check(S1) fails early via val < 0 -> return False (lines 23-24);
        # check(S2) is then evaluated and also fails, so 'No' is returned
        # (covers the else branch of the return expression, line 29).
        ([")", ")"], "No"),
        # check(S1) fails via val < 0 (line 24) but check(S2) succeeds,
        # covering the second operand of the `or` in the return expression.
        ([")", "(()"], "Yes"),
        # check runs to completion but val != 0, covering the False branch of
        # the final ternary in check (line 25); both orders fail -> 'No'.
        (["(", "("], "No"),
    ],
)
def test_match_parens(lst, expected):
    assert match_parens(lst) == expected


def test_match_parens_examples_from_docstring():
    # Directly verify the documented examples as postconditions.
    assert match_parens(["()(", ")"]) == "Yes"
    assert match_parens([")", ")"]) == "No"
