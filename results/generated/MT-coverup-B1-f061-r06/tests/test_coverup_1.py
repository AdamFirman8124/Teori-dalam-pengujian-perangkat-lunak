# file: project/f061/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}
# gained: {"lines": [3, 4, 5, 6, 8, 9, 10, 11], "branches": [[4, 5], [4, 11], [5, 6], [5, 8], [9, 4], [9, 10]]}

import pytest

from f061 import correct_bracketing


def test_correct_bracketing_empty_string_returns_true():
    assert correct_bracketing("") is True


def test_correct_bracketing_single_pair_returns_true():
    assert correct_bracketing("()") is True


def test_correct_bracketing_nested_pairs_returns_true():
    assert correct_bracketing("(()())") is True


def test_correct_bracketing_unclosed_open_returns_false():
    # loop completes with depth > 0 -> final `return depth == 0` is False
    assert correct_bracketing("(()") is False


def test_correct_bracketing_extra_closing_returns_false_early():
    # depth goes negative on the first char -> early `return False`
    assert correct_bracketing(")(") is False


def test_correct_bracketing_negative_depth_short_circuits(monkeypatch):
    # Verify the early return happens before the rest of the string is consumed.
    seen = []

    class SpyStr(str):
        def __iter__(self):
            for ch in str(self):
                seen.append(ch)
                yield ch

    assert correct_bracketing(SpyStr(")abc")) is False
    assert seen == [")"]


def test_correct_bracketing_balanced_with_extra_closing_at_end_returns_false():
    assert correct_bracketing("())(()") is False


@pytest.mark.parametrize(
    "brackets, expected",
    [
        ("(", False),
        (")", False),
        ("()()()", True),
        ("((()))", True),
        ("(()))", False),
    ],
)
def test_correct_bracketing_parametrized(brackets, expected):
    assert correct_bracketing(brackets) is expected
