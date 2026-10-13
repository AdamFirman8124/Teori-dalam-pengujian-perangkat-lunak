# file: script_1.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

from script_1 import separate_paren_groups


def _is_balanced(group: str) -> bool:
    depth = 0
    for c in group:
        depth += 1 if c == "(" else -1
        if depth < 0:
            return False
    return depth == 0


def test_empty_string_returns_empty_list():
    assert separate_paren_groups("") == []


def test_only_non_paren_characters():
    # Exercises the for loop with neither '(' nor ')' ever encountered.
    assert separate_paren_groups("abc def") == []


def test_single_simple_group():
    result = separate_paren_groups("()")
    assert result == ["()"]
    assert _is_balanced(result[0])


def test_nested_group_covers_depth_nonzero_branch():
    # The inner ')' does not reach depth 0; only the outer ')' does.
    result = separate_paren_groups("(())")
    assert result == ["(())"]
    assert _is_balanced(result[0])


def test_multiple_groups_with_whitespace():
    s = "(()()) ((())) ()"
    result = separate_paren_groups(s)
    assert result == ["(()())", "((()))", "()"]
    assert all(_is_balanced(g) for g in result)
    # Postcondition: concatenated groups equal the paren characters in order.
    assert "".join(result) == "".join(c for c in s if c in "()")


def test_groups_with_ignored_inner_characters():
    result = separate_paren_groups("(a(b)c)(d)")
    assert result == ["(())", "()"]
    assert all(_is_balanced(g) for g in result)


def test_unbalanced_input_returns_only_complete_groups():
    assert separate_paren_groups("(()") == []
    assert separate_paren_groups("()(") == ["()"]


def test_repeated_calls_do_not_share_state():
    # The function uses only local state; verify calls are independent and repeatable.
    first = separate_paren_groups("(a)(b)")
    second = separate_paren_groups("(a)(b)")
    assert first == ["()", "()"]
    assert second == ["()", "()"]
    assert first is not second
