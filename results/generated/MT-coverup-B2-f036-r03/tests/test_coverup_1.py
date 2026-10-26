# file: project/f036/__init__.py:1-11
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11], "branches": [[4, 5], [4, 7], [5, 4], [5, 6], [9, 10], [9, 11]]}

from f036 import fizz_buzz


def test_fizz_buzz_counts_sevens_in_selected_numbers():
    # range(92) -> 0,11,13,22,26,33,39,44,52,55,65,66,77,78,88,91
    # joined: "0111322263339445255656677788891" -> three '7' characters
    assert fizz_buzz(92) == 3


def test_fizz_buzz_returns_zero_when_no_numbers_are_selected():
    assert fizz_buzz(0) == 0


def test_fizz_buzz_returns_zero_when_no_seven_present():
    # range(11) -> only 0 is selected -> "0" -> no '7'
    assert fizz_buzz(11) == 0
