# file: project/f014/__init__.py:4-10
# asked: {"lines": [6, 8, 9, 10], "branches": [[8, 9], [8, 10]]}
# gained: {"lines": [6, 8, 9, 10], "branches": [[8, 9], [8, 10]]}

from f014 import all_prefixes


def test_all_prefixes_nonempty_executes_loop_body():
    result = all_prefixes("abc")
    assert result == ["a", "ab", "abc"]
    assert len(result) == 3


def test_all_prefixes_single_character():
    assert all_prefixes("x") == ["x"]


def test_all_prefixes_empty_executes_loop_exit_without_body():
    result = all_prefixes("")
    assert result == []
    assert len(result) == 0
