# file: __init__.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

import pytest


@pytest.fixture()
def separate_paren_groups():
    from __init__ import separate_paren_groups as func
    return func


class TestSeparateParenGroups:
    def test_empty_string_returns_empty_list(self, separate_paren_groups):
        result = separate_paren_groups("")
        assert result == []
        assert isinstance(result, list)

    def test_simple_group(self, separate_paren_groups):
        result = separate_paren_groups("(())")
        assert result == ["(())"]

    def test_multiple_groups(self, separate_paren_groups):
        result = separate_paren_groups("(())()()")
        assert result == ["(())", "()", "()"]

    def test_nested_groups(self, separate_paren_groups):
        result = separate_paren_groups("((()))")
        assert result == ["((()))"]

    def test_non_paren_characters_only_parens_captured(self, separate_paren_groups):
        result = separate_paren_groups("abc(def)ghi")
        assert result == ["()"]

    def test_whitespace_between_groups(self, separate_paren_groups):
        result = separate_paren_groups("  (())  ()  ")
        assert result == ["(())", "()"]

    def test_single_open_paren_no_close(self, separate_paren_groups):
        result = separate_paren_groups("(")
        assert result == []

    def test_single_close_paren(self, separate_paren_groups):
        result = separate_paren_groups(")")
        assert result == []

    def test_deeply_nested(self, separate_paren_groups):
        result = separate_paren_groups("(((())))")
        assert result == ["(((())))"]

    def test_mixed_nested_and_simple(self, separate_paren_groups):
        result = separate_paren_groups("(())(())")
        assert result == ["(())", "(())"]

    def test_sequential_depth_transitions(self, separate_paren_groups):
        result = separate_paren_groups("(()())(()())")
        assert result == ["(()())", "(()())"]
        assert all(s.startswith("(") and s.endswith(")") for s in result)
