# file: project/f066/__init__.py:1-3
# asked: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}
# gained: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}

import pytest

from f066 import digitSum


def test_digit_sum_empty_string():
    """Covers line 2 (True branch): empty string returns 0."""
    assert digitSum("") == 0


def test_digit_sum_mixed_case():
    """Covers line 2 (False branch) and line 3: only uppercase chars contribute."""
    # 'B' -> 66, 'C' -> 67; lowercase and digits contribute 0
    assert digitSum("aBC1") == ord("B") + ord("C") == 133


def test_digit_sum_all_lowercase():
    """Covers line 2 (False branch) and line 3 (else branch of generator)."""
    assert digitSum("abc") == 0


def test_digit_sum_all_uppercase():
    """Covers line 2 (False branch) and line 3 (if branch of generator)."""
    assert digitSum("ABC") == ord("A") + ord("B") + ord("C") == 198


def test_digit_sum_single_uppercase_char():
    """Covers line 2 (False branch) and line 3 with a single uppercase char."""
    assert digitSum("Z") == ord("Z") == 90


def test_digit_sum_non_alpha_characters():
    """Covers line 2 (False branch) and line 3 with non-alpha characters."""
    # Non-alpha characters are not uppercase, so contribute 0
    assert digitSum("123 !?") == 0
