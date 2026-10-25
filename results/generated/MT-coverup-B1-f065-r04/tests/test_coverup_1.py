# file: project/f065/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

from f065 import circular_shift


def test_circular_shift_greater_than_length_reverses_string():
    assert circular_shift(123, 4) == "321"


def test_circular_shift_within_length_rotates_string():
    assert circular_shift(12345, 2) == "45123"
