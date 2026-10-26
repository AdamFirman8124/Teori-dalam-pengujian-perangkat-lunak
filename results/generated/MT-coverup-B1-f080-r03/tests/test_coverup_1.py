# file: project/f080/__init__.py:1-10
# asked: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}

from f080 import is_happy


def test_is_happy_rejects_short_strings():
    assert is_happy("") is False
    assert is_happy("ab") is False


def test_is_happy_checks_all_three_character_comparisons():
    assert is_happy("aab") is False
    assert is_happy("abb") is False
    assert is_happy("aba") is False
    assert is_happy("abcd") is True
