# file: project/f001/__init__.py:4-22
# asked: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}
# gained: {"lines": [6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 22], "branches": [[10, 11], [10, 22], [11, 12], [11, 14], [14, 10], [14, 15], [18, 10], [18, 19]]}

import importlib
import importlib.util
import os


def _load_separate_paren_groups():
    """Import the function under test, falling back to the file path."""
    try:
        return importlib.import_module("f001").separate_paren_groups
    except ImportError:
        candidates = [
            os.path.join(os.getcwd(), "f001", "__init__.py"),
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "f001", "__init__.py"),
        ]
        for path in candidates:
            if os.path.isfile(path):
                spec = importlib.util.spec_from_file_location("f001_under_test", path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                return module.separate_paren_groups
        raise


def test_empty_string_returns_empty_list():
    separate_paren_groups = _load_separate_paren_groups()
    result = separate_paren_groups("")
    assert result == []
    assert isinstance(result, list)


def test_no_parentheses_returns_empty_list():
    separate_paren_groups = _load_separate_paren_groups()
    result = separate_paren_groups("abc def")
    assert result == []


def test_single_simple_group():
    separate_paren_groups = _load_separate_paren_groups()
    result = separate_paren_groups("(hello)")
    assert result == ["()"]
    assert len(result) == 1


def test_empty_parens_group():
    separate_paren_groups = _load_separate_paren_groups()
    result = separate_paren_groups("()")
    assert result == ["()"]


def test_two_adjacent_groups():
    separate_paren_groups = _load_separate_paren_groups()
    result = separate_paren_groups("(a)(b)")
    assert result == ["()", "()"]
    assert len(result) == 2


def test_groups_embedded_in_text():
    separate_paren_groups = _load_separate_paren_groups()
    result = separate_paren_groups("f(x, y) + g(z)")
    assert result == ["()", "()"]


def test_nested_groups_kept_together():
    separate_paren_groups = _load_separate_paren_groups()
    result = separate_paren_groups("(a(b)c)")
    assert result == ["(())"]
    assert len(result) == 1


def test_deeply_nested_groups():
    separate_paren_groups = _load_separate_paren_groups()
    result = separate_paren_groups("(a(b(c)d)e)")
    assert result == ["((()))"]
    assert len(result) == 1


def test_nested_then_multiple():
    separate_paren_groups = _load_separate_paren_groups()
    result = separate_paren_groups("(a(b))(c)")
    assert result == ["(())", "()"]


def test_unmatched_open_paren_is_dropped():
    separate_paren_groups = _load_separate_paren_groups()
    result = separate_paren_groups("(a")
    assert result == []


def test_unmatched_open_paren_after_complete_group():
    separate_paren_groups = _load_separate_paren_groups()
    result = separate_paren_groups("(a)(b")
    assert result == ["()"]


def test_unmatched_close_paren_is_dropped():
    separate_paren_groups = _load_separate_paren_groups()
    result = separate_paren_groups(")")
    assert result == []


def test_unmatched_close_paren_after_complete_group():
    separate_paren_groups = _load_separate_paren_groups()
    result = separate_paren_groups("(a))")
    assert result == ["()"]


def test_text_between_groups_is_ignored():
    separate_paren_groups = _load_separate_paren_groups()
    result = separate_paren_groups("foo(1) bar(2) baz(3)")
    assert result == ["()", "()", "()"]
    assert all(g.startswith("(") and g.endswith(")") for g in result)


def test_only_parenthesis_characters_are_retained():
    separate_paren_groups = _load_separate_paren_groups()
    result = separate_paren_groups("x( a , b )y")
    assert result == ["()"]
    assert all(ch in "()" for ch in result[0])


def test_result_is_list_of_strings():
    separate_paren_groups = _load_separate_paren_groups()
    result = separate_paren_groups("(a)(b)(c)")
    assert isinstance(result, list)
    assert all(isinstance(item, str) for item in result)
    assert result == ["()", "()", "()"]


def test_multiline_input():
    separate_paren_groups = _load_separate_paren_groups()
    result = separate_paren_groups("(line1\nline2)\n(other)")
    assert result == ["()", "()"]
