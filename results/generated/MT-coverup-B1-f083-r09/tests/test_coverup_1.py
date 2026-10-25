# file: project/f083/__init__.py:1-5
# asked: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}
# gained: {"lines": [3, 4, 5], "branches": [[3, 4], [3, 5]]}

from f083 import starts_one_ends


def test_starts_one_ends_for_one_digit_number():
    assert starts_one_ends(1) == 1


def test_starts_one_ends_for_numbers_other_than_one():
    assert starts_one_ends(2) == 18
