# file: project/f161/__init__.py:1-16
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], "branches": [[6, 7], [6, 11], [7, 8], [7, 10], [12, 13], [12, 14], [14, 15], [14, 16]]}

from f161 import solve


def test_solve_swaps_case_of_alphabetic_characters():
    assert solve("Ab1-z") == "aB1-Z"


def test_solve_reverses_string_without_alphabetic_characters():
    assert solve("12-!?") == "?!-21"


def test_solve_handles_empty_string():
    assert solve("") == ""
