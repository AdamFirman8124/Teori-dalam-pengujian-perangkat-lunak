# file: script_106.py:1-20
# asked: {"lines": [10, 11, 12, 13, 14, 15, 17, 18, 19, 20], "branches": [[11, 12], [11, 20], [12, 13], [12, 17], [14, 14], [14, 15], [18, 18], [18, 19]]}
# gained: {"lines": [10, 11, 12, 13, 14, 15, 17, 18, 19, 20], "branches": [[11, 12], [11, 20], [12, 13], [12, 17], [14, 14], [14, 15], [18, 18], [18, 19]]}

import pytest
from script_106 import f


def test_f_with_5():
    """Test f(5) as given in the example."""
    result = f(5)
    assert result == [1, 2, 6, 24, 15]


def test_f_with_1():
    """Test f(1) - single odd element."""
    result = f(1)
    assert result == [1]


def test_f_with_2():
    """Test f(2) - one odd, one even."""
    result = f(2)
    assert result == [1, 2]


def test_f_with_6():
    """Test f(6) - multiple even and odd elements."""
    result = f(6)
    assert result == [1, 2, 6, 24, 15, 720]


def test_f_with_0():
    """Test f(0) - edge case with empty list."""
    result = f(0)
    assert result == []


def test_f_with_10():
    """Test f(10) - larger input."""
    result = f(10)
    expected = [
        1,       # i=1: sum(1..1) = 1
        2,       # i=2: 2! = 2
        6,       # i=3: sum(1..3) = 6
        24,      # i=4: 4! = 24
        15,      # i=5: sum(1..5) = 15
        720,     # i=6: 6! = 720
        28,      # i=7: sum(1..7) = 28
        40320,   # i=8: 8! = 40320
        45,      # i=9: sum(1..9) = 45
        3628800  # i=10: 10! = 3628800
    ]
    assert result == expected
