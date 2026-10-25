# file: project/f161/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}

from f161 import solve


def test_solve_lowercase_to_uppercase():
    assert solve("hello") == "HELLO"


def test_solve_uppercase_to_lowercase():
    assert solve("HeLLo") == "hEllO"


def test_solve_mixed_alpha_and_nonalpha():
    # covers both True and False outcomes of i.isalpha() with flg == 1
    assert solve("a1B!") == "A1b!"
    assert solve("ab12") == "AB12"


def test_solve_no_alpha_reverses_string():
    # covers i.isalpha() False-only loop and flg == 0 branch
    assert solve("12345") == "54321"
    assert solve("!@#") == "#@!"
    assert solve("5") == "5"


def test_solve_empty_string():
    # covers zero-iteration loops and flg == 0 branch
    assert solve("") == ""
