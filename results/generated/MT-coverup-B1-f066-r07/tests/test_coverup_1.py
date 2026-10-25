# file: project/f066/__init__.py:1-3
# asked: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}
# gained: {"lines": [2, 3], "branches": [[2, 2], [2, 3]]}

from f066 import digitSum


def test_digit_sum_empty_string():
    assert digitSum("") == 0


def test_digit_sum_counts_only_uppercase_characters():
    assert digitSum("AaZ1") == ord("A") + ord("Z")
