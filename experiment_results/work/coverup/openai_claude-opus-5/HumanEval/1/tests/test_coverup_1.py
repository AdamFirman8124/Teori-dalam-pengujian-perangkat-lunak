# file: script_1.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

import pytest
from script_1 import separate_paren_groups


def test_empty_string():
    assert separate_paren_groups("") == []


def test_no_parens():
    assert separate_paren_groups("abc") == []


def test_single_group():
    assert separate_paren_groups("(abc)") == ["()"]


def test_multiple_groups():
    assert separate_paren_groups("(a)(b)(c)") == ["()", "()", "()"]


def test_nested_groups():
    assert separate_paren_groups("((a)b)(c)") == ["(())", "()"]


def test_trailing_unclosed_ignored():
    assert separate_paren_groups("(a)(bc") == ["()"]


def test_non_string_input():
    with pytest.raises(TypeError):
        separate_paren_groups(None)
