# file: script_q2.py:19-23
# asked: {"lines": [20, 21, 22, 23], "branches": [[20, 21], [20, 23], [21, 20], [21, 22]]}
# gained: {"lines": [20, 21, 22, 23], "branches": [[20, 21], [20, 23], [21, 20], [21, 22]]}

from script_q2 import contains_unique_day


def test_contains_unique_day_returns_true_for_a_month_with_a_unique_day():
    possible_birthdays = [
        (5, 17),
        (6, 18),
    ]

    result = contains_unique_day(5, possible_birthdays)

    assert result is True


def test_contains_unique_day_returns_false_when_no_day_in_month_is_unique():
    possible_birthdays = [
        (5, 17),
        (5, 17),
        (6, 18),
    ]

    result = contains_unique_day(5, possible_birthdays)

    assert result is False
