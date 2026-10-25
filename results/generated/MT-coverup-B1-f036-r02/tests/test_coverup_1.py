# file: project/f036/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}

from f036 import fizz_buzz


def test_fizz_buzz_counts_sevens_in_selected_numbers():
    assert fizz_buzz(78) == 2


def test_fizz_buzz_returns_zero_when_selected_numbers_contain_no_sevens():
    assert fizz_buzz(14) == 0
