# file: project/f161/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}

from f161 import solve


def test_swapcase_alpha():
    assert solve("Hello") == "hELLO"
    assert solve("ABC") == "abc"
    assert solve("abc") == "ABC"


def test_no_alpha_returns_reversed():
    assert solve("123") == "321"
    assert solve("!@#") == "#@!"
    assert solve("123! ") == " !321"


def test_mixed_alpha_and_non_alpha():
    assert solve("a1B2c") == "A1b2C"
    assert solve("Ab1!") == "aB1!"


def test_empty_string():
    assert solve("") == ""
