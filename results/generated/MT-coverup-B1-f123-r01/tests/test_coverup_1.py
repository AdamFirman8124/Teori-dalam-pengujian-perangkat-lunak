# file: project/f123/__init__.py:1-16
# asked: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}
# gained: {"lines": [3, 4, 6, 7, 8, 9, 11, 13, 14, 16], "branches": [[3, 4], [3, 6], [7, 8], [7, 16], [8, 9], [8, 11], [13, 7], [13, 14]]}

from f123 import get_odd_collatz


def test_get_odd_collatz_n_1():
    # Covers: n odd initial branch, while loop not entered
    assert get_odd_collatz(1) == [1]


def test_get_odd_collatz_n_2():
    # Covers: n even initial branch, even step, odd append
    assert get_odd_collatz(2) == [1]


def test_get_odd_collatz_n_3():
    # Covers: n odd initial branch, odd step (3*3+1), even step,
    # append taken and not taken
    assert get_odd_collatz(3) == [1, 3, 5]


def test_get_odd_collatz_n_4():
    # Covers: even start with multiple even steps before odd
    assert get_odd_collatz(4) == [1]


def test_get_odd_collatz_n_12():
    # Covers: even start that later hits odd n inside loop
    assert get_odd_collatz(12) == [1, 3, 5]
