# file: project\f001\__init__.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 15], [18, 10], [18, 19]]}

import pytest
from f001 import separate_paren_groups


class TestSeparateParenGroups:
    def test_empty_string(self):
        result = separate_paren_groups("")
        assert result == []

    def test_only_opening_paren(self):
        result = separate_paren_groups("(")
        assert result == []

    def test_only_closing_paren(self):
        result = separate_paren_groups(")")
        assert result == []

    def test_single_balanced_group(self):
        result = separate_paren_groups("()")
        assert result == ["()"]

    def test_nested_parentheses(self):
        result = separate_paren_groups("(())")
        assert result == ["(())"]

    def test_multiple_groups(self):
        result = separate_paren_groups("()()")
        assert result == ["()", "()"]

    def test_mixed_nested_and_multiple_groups(self):
        result = separate_paren_groups("(())()((()))")
        assert result == ["(())", "()", "((()))"]

    def test_deeply_nested(self):
        result = separate_paren_groups("(((())))")
        assert result == ["(((())))"]
