# file: project/f096/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}

from f096 import count_up_to


def test_count_up_to_returns_primes_and_handles_composites():
    assert count_up_to(10) == [2, 3, 5, 7]


def test_count_up_to_returns_empty_list_below_first_prime():
    assert count_up_to(2) == []
