# file: project/f093/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": []}
# gained: {"lines": [3, 4, 5, 6], "branches": []}

from f093 import encode


def test_encode_replaces_vowels_and_swapcases_other_characters():
    assert encode("aeiouAEIOU xyz XYZ") == "CGKQWcgkqw XYZ xyz"


def test_encode_empty_message():
    assert encode("") == ""
