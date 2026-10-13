# file: script_q2.py:11-16
# asked: {"lines": [12, 13, 14, 15, 16], "branches": [[13, 14], [13, 16], [14, 13], [14, 15]]}
# gained: {"lines": [12, 13, 14, 15, 16], "branches": [[13, 14], [13, 16], [14, 13], [14, 15]]}

from script_q2 import unique_month


def test_unique_month_returns_true_for_exactly_one_matching_birthday():
    possible_birthdays = [(3, 14), (7, 4), (12, 25)]

    result = unique_month(7, possible_birthdays)

    assert result is True


def test_unique_month_returns_false_for_no_or_multiple_matching_birthdays():
    assert unique_month(2, [(3, 14), (7, 4)]) is False
    assert unique_month(7, [(7, 4), (7, 15), (12, 25)]) is False
