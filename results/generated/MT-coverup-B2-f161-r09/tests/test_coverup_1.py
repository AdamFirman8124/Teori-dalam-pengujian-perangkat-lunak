# file: project/f161/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}

from f161 import solve


def test_solve_empty_string():
    assert solve("") == ""


def test_solve_no_alpha_reverses():
    assert solve("123") == "321"
    assert solve("!@#") == "#@!"


def test_solve_alpha_swapcase():
    assert solve("abc") == "ABC"
    assert solve("ABC") == "abc"
    assert solve("Hello") == "hELLO"


def test_solve_mixed_alpha_and_non_alpha():
    assert solve("a1B!") == "A1b!"
    assert solve("1a2") == "1A2"
