# file: project/f096/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "branches": [[4, 5], [4, 12], [6, 7], [6, 10], [7, 6], [7, 8], [10, 4], [10, 11]]}

import f096


def test_count_up_to_basic():
    assert f096.count_up_to(10) == [2, 3, 5, 7]


def test_count_up_to_empty():
    assert f096.count_up_to(2) == []


def test_count_up_to_composite_break():
    # 4 is composite: inner loop hits i % j == 0, sets is_prime=False, breaks
    assert f096.count_up_to(5) == [2, 3]
    assert f096.count_up_to(6) == [2, 3, 5]
