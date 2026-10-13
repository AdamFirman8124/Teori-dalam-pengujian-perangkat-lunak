# file: script_q2.py:3-8
# asked: {"lines": [4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}
# gained: {"lines": [4, 5, 6, 7, 8], "branches": [[5, 6], [5, 8], [6, 5], [6, 7]]}

from script_q2 import unique_day


def test_unique_day_returns_true_for_exactly_one_matching_birthday():
    possible_birthdays = [
        ("January", 12),
        ("March", 7),
        ("July", 21),
    ]

    assert unique_day(7, possible_birthdays) is True


def test_unique_day_returns_false_when_no_birthday_matches():
    possible_birthdays = [
        ("January", 12),
        ("March", 7),
        ("July", 21),
    ]

    assert unique_day(30, possible_birthdays) is False


def test_unique_day_returns_false_when_multiple_birthdays_match():
    possible_birthdays = [
        ("January", 12),
        ("March", 12),
        ("July", 21),
    ]

    assert unique_day(12, possible_birthdays) is False


def test_unique_day_returns_false_for_empty_birthday_list():
    assert unique_day(12, []) is False
