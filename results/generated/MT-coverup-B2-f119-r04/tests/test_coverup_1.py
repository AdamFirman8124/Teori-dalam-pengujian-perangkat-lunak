# file: project/f119/__init__.py:1-29
# asked: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}

from f119 import match_parens


def test_balanced_first_concatenation():
    assert match_parens(["()(", ")"]) == "Yes"


def test_balanced_second_concatenation():
    assert match_parens([")", "("]) == "Yes"


def test_unbalanced_due_to_closing_parenthesis_prefix():
    assert match_parens([")", ")"]) == "No"


def test_unbalanced_due_to_surplus_opening_parenthesis():
    assert match_parens(["(", ""]) == "No"
