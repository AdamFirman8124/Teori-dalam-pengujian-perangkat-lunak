# file: project\f001\__init__.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

from f001 import separate_paren_groups


def test_separate_paren_groups_returns_each_balanced_group():
    assert separate_paren_groups("abc(())xyz()") == ["(())", "()"]


def test_separate_paren_groups_returns_empty_list_for_no_groups():
    assert separate_paren_groups("") == []
