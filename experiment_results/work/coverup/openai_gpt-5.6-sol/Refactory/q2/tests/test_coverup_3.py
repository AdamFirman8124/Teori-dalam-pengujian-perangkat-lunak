# file: script_q2.py:19-23
# asked: {"lines": [20, 21, 22, 23], "branches": [[20, 21], [20, 23], [21, 20], [21, 22]]}
# gained: {"lines": [20, 21, 22, 23], "branches": [[20, 21], [20, 23], [21, 20], [21, 22]]}

from script_q2 import contains_unique_day


def test_contains_unique_day_returns_true_for_unique_day_in_month():
    possible_birthdays = [
        ("May", 15),
        ("June", 16),
        ("July", 17),
    ]

    assert contains_unique_day("May", possible_birthdays) is True


def test_contains_unique_day_returns_false_when_matching_day_is_not_unique():
    possible_birthdays = [
        ("May", 15),
        ("June", 15),
    ]

    assert contains_unique_day("May", possible_birthdays) is False
