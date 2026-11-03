# file: project/f065/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}
# gained: {"lines": [3, 4, 5, 7], "branches": [[4, 5], [4, 7]]}

from f065 import circular_shift


def test_circular_shift_shift_within_length():
    """Covers lines 3-4 and the else branch (line 7): shift <= len(s)."""
    # s = "12", len(s) - shift = 1 -> s[1:] + s[:1] = "2" + "1"
    assert circular_shift(12, 1) == "21"


def test_circular_shift_shift_equals_length():
    """Boundary case of the else branch: shift == len(s) yields the original string."""
    assert circular_shift(12, 2) == "12"


def test_circular_shift_zero_shift():
    """Zero shift returns the original string unchanged (else branch)."""
    assert circular_shift(12345, 0) == "12345"


def test_circular_shift_shift_greater_than_length():
    """Covers line 5: shift > len(s) returns the reversed string."""
    assert circular_shift(12, 3) == "21"
    assert circular_shift(123, 100) == "321"
