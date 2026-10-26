# file: project/f065/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

from f065 import circular_shift


def test_circular_shift_greater_than_len_reverses():
    assert circular_shift(123, 5) == "321"
    assert circular_shift(12345, 10) == "54321"
    assert circular_shift("abcd", 5) == "dcba"


def test_circular_shift_normal_rotation():
    assert circular_shift(12345, 2) == "45123"
    assert circular_shift("abcd", 1) == "dabc"
    assert circular_shift(12, 1) == "21"


def test_circular_shift_boundary_shifts():
    # shift == len(s) returns same string via else branch
    assert circular_shift(123, 3) == "123"
    # shift == 0 returns same string via else branch
    assert circular_shift(123, 0) == "123"
    assert circular_shift("abcd", 4) == "abcd"
