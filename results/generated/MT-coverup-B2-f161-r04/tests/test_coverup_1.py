# file: project/f161/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}

from f161 import solve


def test_solve_with_letters_swaps_case():
    assert solve("aBc") == "AbC"
    assert solve("Hello") == "hELLO"
    assert solve("ABC") == "abc"
    assert solve("xyz") == "XYZ"


def test_solve_without_letters_reverses_string():
    assert solve("123") == "321"
    assert solve("12 34") == "43 21"
    assert solve("!@#") == "#@!"


def test_solve_mixed_alpha_and_non_alpha():
    assert solve("a1B!") == "A1b!"
    assert solve("Hello, World! 123") == "hELLO, wORLD! 123"


def test_solve_empty_string():
    assert solve("") == ""


def test_solve_single_character():
    assert solve("a") == "A"
    assert solve("Z") == "z"
    assert solve("7") == "7"
    assert solve(" ") == " "
