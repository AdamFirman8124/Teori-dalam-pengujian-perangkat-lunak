# file: project/f065/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

from f065 import circular_shift


def test_circular_shift_shift_smaller_than_length():
    # Covers lines 3-4 and the else branch (line 7): shift < len(s)
    assert circular_shift(12, 1) == "21"


def test_circular_shift_shift_equal_to_length():
    # Boundary case for the else branch (line 7): shift == len(s)
    assert circular_shift(12, 2) == "12"


def test_circular_shift_shift_greater_than_length():
    # Covers lines 3-4 and the if branch (line 5): shift > len(s) reverses the string
    assert circular_shift(12, 5) == "21"


def test_circular_shift_non_integer_input():
    # Line 3 (s = str(x)) with a non-integer argument; else branch again
    assert circular_shift("abc", 1) == "cab"
