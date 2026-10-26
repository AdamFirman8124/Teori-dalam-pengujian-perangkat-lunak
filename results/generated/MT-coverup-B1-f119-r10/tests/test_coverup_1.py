# file: project/f119/__init__.py:1-29
# asked: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}

from f119 import match_parens


def test_match_parens_accepts_balanced_first_concatenation():
    assert match_parens(["()(", ")"]) == "Yes"


def test_match_parens_checks_second_concatenation_after_first_fails():
    assert match_parens([")", "()("]) == "Yes"


def test_match_parens_rejects_unbalanced_strings_without_negative_prefix():
    assert match_parens(["(", "(()"]) == "No"


def test_match_parens_rejects_when_both_concatenations_start_unbalanced():
    assert match_parens([")", ")"]) == "No"
