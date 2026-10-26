# file: project/f096/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}

import pytest

from f096 import count_up_to


def test_count_up_to_empty_range():
    # n <= 2: loop body never runs, only lines 3 and 12 execute
    assert count_up_to(0) == []
    assert count_up_to(1) == []
    assert count_up_to(2) == []


def test_count_up_to_single_prime():
    # n == 3: i == 2, inner range(2, 2) is empty -> is_prime stays True -> append
    assert count_up_to(3) == [2]


def test_count_up_to_composites_and_primes():
    # Covers both the break branch (composite i) and the append branch (prime i)
    assert count_up_to(10) == [2, 3, 5, 7]
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_count_up_to_upper_bound_exclusive():
    # n is exclusive: 7 itself must not appear when n == 7
    result = count_up_to(7)
    assert result == [2, 3, 5]
    assert 7 not in result


def test_count_up_to_returns_fresh_list():
    # Postcondition: each call returns a new list, no shared mutable state
    first = count_up_to(10)
    second = count_up_to(10)
    assert first == second
    assert first is not second
    first.append(999)
    assert count_up_to(10) == [2, 3, 5, 7]
