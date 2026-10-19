# file: dataset\coverup-eval\MuTAP-benchmarks\f001\f001\__init__.py:4-22
# asked: {"lines": [4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [4, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

from f001 import separate_paren_groups


def test_single_group_ignores_non_parenthesis_characters():
    assert separate_paren_groups("(a)") == ["()"]


def test_multiple_groups_are_returned_separately():
    assert separate_paren_groups("(a)(b)") == ["()", "()"]


def test_nested_parentheses_are_kept_in_one_group():
    assert separate_paren_groups("(a(b)c)") == ["(())"]


def test_non_parenthesis_input_returns_empty_list():
    assert separate_paren_groups("abc") == []


def test_empty_input_returns_empty_list():
    assert separate_paren_groups("") == []


def test_unclosed_group_is_not_returned():
    assert separate_paren_groups("(a)(b") == ["()"]


def test_whitespace_is_ignored():
    assert separate_paren_groups(" ( ( ) ) ( ) ") == ["(())", "()"]
