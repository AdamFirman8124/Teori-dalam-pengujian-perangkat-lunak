# file: project/f066/__init__.py:1-3
# asked: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}
# gained: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}

from f066 import digitSum


def test_digit_sum_empty_string():
    """Covers line 2: the early-return branch when s == ''."""
    assert digitSum("") == 0


def test_digit_sum_mixed_case():
    """Covers lines 2-3: non-empty path; uppercase chars counted, lowercase contribute 0."""
    result = digitSum("aBcD")
    assert result == ord('B') + ord('D')


def test_digit_sum_all_upper():
    """Covers line 3: every character is uppercase."""
    assert digitSum("ABC") == ord('A') + ord('B') + ord('C')


def test_digit_sum_all_lower():
    """Covers line 3: no uppercase characters, so the sum is 0."""
    assert digitSum("xyz") == 0
