# file: project\f001\__init__.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 15], [18, 10], [18, 19]]}

import sys
import pytest

sys.path.insert(0, 'f001')

from f001 import separate_paren_groups


def test_empty_string():
    result = separate_paren_groups("")
    assert result == []


def test_only_opening_paren():
    result = separate_paren_groups("(")
    assert result == []


def test_orphan_closing_paren():
    result = separate_paren_groups(")")
    assert result == []


def test_single_balanced_group():
    result = separate_paren_groups("()")
    assert result == ["()"]


def test_nested_parentheses():
    result = separate_paren_groups("(())")
    assert result == ["(())"]


def test_multiple_groups():
    result = separate_paren_groups("()()")
    assert result == ["()", "()"]


def test_mixed_nested_and_multiple_groups():
    result = separate_paren_groups("(())()((()))")
    assert result == ["(())", "()", "((()))"]


def test_deeply_nested():
    result = separate_paren_groups("(((())))")
    assert result == ["(((())))"]
