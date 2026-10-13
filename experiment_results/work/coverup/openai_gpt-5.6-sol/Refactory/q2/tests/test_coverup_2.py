# file: script_q2.py:11-16
# asked: {"lines": [12, 13, 14, 15, 16], "branches": [[13, 14], [13, 16], [14, 13], [14, 15]]}
# gained: {"lines": [12, 13, 14, 15, 16], "branches": [[13, 14], [13, 16], [14, 13], [14, 15]]}

from script_q2 import unique_month


def test_unique_month_returns_true_for_exactly_one_matching_birthday():
    birthdays = [("May", 15), ("June", 17), ("July", 20)]
    original_birthdays = birthdays.copy()

    assert unique_month("June", birthdays) is True
    assert birthdays == original_birthdays


def test_unique_month_returns_false_for_multiple_matching_birthdays():
    birthdays = [("May", 15), ("May", 16), ("June", 17)]
    original_birthdays = birthdays.copy()

    assert unique_month("May", birthdays) is False
    assert birthdays == original_birthdays


def test_unique_month_returns_false_for_no_matching_birthdays():
    birthdays = [("May", 15), ("June", 17)]
    original_birthdays = birthdays.copy()

    assert unique_month("July", birthdays) is False
    assert birthdays == original_birthdays
