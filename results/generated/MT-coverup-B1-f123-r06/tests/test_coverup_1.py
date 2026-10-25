# file: project/f123/__init__.py:1-16
# asked: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}

from f123 import get_odd_collatz


def test_get_odd_collatz_with_even_start():
    assert get_odd_collatz(6) == [1, 3, 5]


def test_get_odd_collatz_with_odd_start():
    assert get_odd_collatz(3) == [1, 3, 5]


def test_get_odd_collatz_without_looping():
    assert get_odd_collatz(1) == [1]
