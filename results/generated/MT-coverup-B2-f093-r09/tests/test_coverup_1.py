# file: project/f093/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": []}
# gained: {"lines": [3, 4, 5, 6], "branches": []}

from f093 import encode


def test_encode_swaps_case_and_shifts_vowels():
    assert encode("hello") == "HGLLQ"
    assert encode("AEIOU") == "cgkqw"
    assert encode("Python 3.8!") == "pYTHQN 3.8!"
    assert encode("") == ""
