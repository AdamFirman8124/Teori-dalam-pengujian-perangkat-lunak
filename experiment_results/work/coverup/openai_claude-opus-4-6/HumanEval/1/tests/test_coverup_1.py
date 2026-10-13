# file: script_1.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

from script_1 import separate_paren_groups

def test_single_simple_group():
    # covers the '(' branch and the ')' branch with depth returning to 0
    assert separate_paren_groups("()") == ["()"]

def test_single_nested_group():
    # covers ')' branch when depth does NOT return to 0 (inner close),
    # then the close that brings depth back to 0 (outer close)
    assert separate_paren_groups("((()))") == ["((()))"]

def test_multiple_groups_with_whitespace_between():
    # covers several groups and the branch where neither '(' nor ')' matches
    assert separate_paren_groups("() (()) ((()))") == ["()", "(())", "((()))"]

def test_multiple_sibling_groups_no_separator():
    assert separate_paren_groups("()()") == ["()", "()"]

def test_empty_string():
    # loop body never executes, result stays empty
    assert separate_paren_groups("") == []

def test_no_parentheses_at_all():
    # covers the branch where neither '(' nor ')' matches
    assert separate_paren_groups("abc def") == []

def test_non_paren_characters_are_discarded():
    # only '(' and ')' characters are retained in the output groups
    result = separate_paren_groups("(a)(b)(c)")
    assert result == ["()", "()", "()"]
    # postcondition: every returned group is balanced
    for group in result:
        assert group.count("(") == group.count(")")

def test_groups_returned_in_order():
    result = separate_paren_groups("(())()(())")
    assert result == ["(())", "()", "(())"]

def test_does_not_mutate_input():
    original = "(())()"
    value = "(())()"
    assert separate_paren_groups(value) == ["(())", "()"]
    assert value == original

def test_result_is_independent_across_calls():
    # verifies no state leaks between calls (function must be pure)
    first = separate_paren_groups("(())")
    second = separate_paren_groups("()")
    assert first == ["(())"]
    assert second == ["()"]
    # mutating the returned list must not affect later calls
    first.append("CORRUPT")
    assert separate_paren_groups("(())") == ["(())"]
