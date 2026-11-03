# file: project/f066/__init__.py:1-3
# asked: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}
# gained: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}

"""Tests for f066.digitSum covering lines 2-3 and all branches."""

from f066 import digitSum


def test_digit_sum_empty_string_returns_zero():
    """Line 2: the `s == ""` true branch must return 0."""
    assert digitSum("") == 0


def test_digit_sum_mixed_case_sums_only_uppercase_ords():
    """Line 2 false branch + line 3: uppercase chars contribute ord(c),
    non-uppercase chars contribute 0 (both branches of the conditional)."""
    assert digitSum("aA") == ord("A")
    assert digitSum("Hello") == ord("H")
    assert digitSum("aBcD") == ord("B") + ord("D")


def test_digit_sum_all_uppercase():
    """Line 3: every char takes the `ord(char)` branch."""
    assert digitSum("ABC") == ord("A") + ord("B") + ord("C")
    assert digitSum("Z") == ord("Z")


def test_digit_sum_no_uppercase_returns_zero():
    """Line 3: every char takes the `else 0` branch (digits, punctuation,
    whitespace and lowercase letters are not uppercase)."""
    assert digitSum("abc") == 0
    assert digitSum("123!@# ") == 0
    assert digitSum("a1!b2?") == 0


def test_digit_sum_non_ascii_uppercase():
    """Line 3: non-ASCII uppercase letters also take the ord() branch."""
    assert digitSum("éÉ") == ord("É")
