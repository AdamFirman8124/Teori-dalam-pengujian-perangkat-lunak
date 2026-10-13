# file: script_q2.py:3-8
# asked: {"lines": [4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

from script_q2 import unique_day


def test_unique_day_returns_true_for_exactly_one_match():
    possible_birthdays = [
        ("January", 10),
        ("February", 20),
        ("March", 30),
    ]

    assert unique_day(20, possible_birthdays) is True


def test_unique_day_returns_false_for_multiple_matches():
    possible_birthdays = [
        ("January", 10),
        ("February", 10),
        ("March", 30),
    ]

    assert unique_day(10, possible_birthdays) is False


def test_unique_day_returns_false_for_no_matches():
    possible_birthdays = [
        ("January", 10),
        ("February", 20),
    ]

    assert unique_day(30, possible_birthdays) is False
