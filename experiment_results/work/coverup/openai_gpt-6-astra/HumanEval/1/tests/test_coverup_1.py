# file: script_1.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

import pytest

from script_1 import separate_paren_groups


@pytest.mark.parametrize(
    ("paren_string", "expected"),
    [
        ("", []),
        ("()", ["()"]),
        ("(())()", ["(())", "()"]),
        ("text (a) ignored", ["()"]),
    ],
)
def test_separate_paren_groups(paren_string, expected):
    assert separate_paren_groups(paren_string) == expected


def test_separate_paren_groups_preserves_multiple_nested_groups():
    paren_string = "((()))(())()"
    result = separate_paren_groups(paren_string)

    assert result == ["((()))", "(())", "()"]
    assert all(group.startswith("(") and group.endswith(")") for group in result)
