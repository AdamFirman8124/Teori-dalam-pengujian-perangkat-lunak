# file: project/f095/__init__.py:1-24
# asked: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}
# gained: {"lines": [3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24], "branches": [[3, 4], [3, 6], [7, 9], [7, 24], [9, 10], [9, 12], [12, 13], [12, 19], [13, 14], [13, 15], [15, 16], [15, 18], [19, 20], [19, 23]]}

"""Tests for f095.check_dict_case, covering all previously uncovered lines (3-24).

Every test calls the pure function with fresh literal dicts, so no global/module
state is touched and no cleanup or monkeypatching is required.
"""

from f095 import check_dict_case


def test_empty_dict_returns_false():
    # Lines 3-4: empty dict short-circuits to False before the loop.
    assert check_dict_case({}) is False


def test_all_upper_keys_returns_true():
    # Lines 6-7 (state init + loop), 9 (str check False branch),
    # 12-14 (start -> upper), 19 (False branch), 22-23 (else break), 24.
    assert check_dict_case({"A": 1, "B": 2}) is True


def test_all_lower_keys_returns_true():
    # Lines 15-16 (start -> lower), 19 (False branch), 22-23 (else break), 24.
    assert check_dict_case({"a": 1, "b": 2}) is True


def test_single_upper_key_loop_runs_to_completion():
    # Exercises the path where the for-loop ends without any break,
    # so line 24 is reached directly with state == "upper".
    assert check_dict_case({"ABC": 1}) is True


def test_lower_state_broken_by_upper_key_returns_false():
    # Lines 19-21: second operand of the `or` on line 19 fires
    # (state "lower" but key not lower) -> "mixed" + break.
    assert check_dict_case({"a": 1, "B": 2}) is False


def test_upper_state_broken_by_lower_key_returns_false():
    # Lines 19-21: first operand of the `or` on line 19 fires
    # (state "upper" but key not upper) -> "mixed" + break.
    assert check_dict_case({"A": 1, "b": 2}) is False


def test_non_string_key_returns_false():
    # Lines 9-11: non-str key forces state "mixed" and breaks the loop.
    assert check_dict_case({1: "one", "a": 2}) is False


def test_first_key_without_case_breaks_immediately():
    # Lines 13 (False), 15 (False), 17-18: first key is neither all-upper
    # nor all-lower, so the else-branch breaks out of the loop.
    assert check_dict_case({"Hello": 1}) is False
    assert check_dict_case({"123": 1}) is False
