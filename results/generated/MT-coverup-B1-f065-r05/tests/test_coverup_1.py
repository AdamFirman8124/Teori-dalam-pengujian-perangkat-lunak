# file: project/f065/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

from f065 import circular_shift


def test_circular_shift_rotates_when_shift_within_length():
    assert circular_shift(12345, 2) == "45123"


def test_circular_shift_reverses_when_shift_exceeds_length():
    assert circular_shift(12345, 6) == "54321"
