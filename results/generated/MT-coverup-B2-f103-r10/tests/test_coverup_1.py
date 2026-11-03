# file: project/f103/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

from f103 import rounded_avg


def test_rounded_avg_m_less_than_n_returns_minus_one():
    """Covers the `m < n` branch (line 3) and early return (line 4)."""
    assert rounded_avg(5, 4) == -1
    assert rounded_avg(1, 0) == -1
    assert rounded_avg(-2, -5) == -1


def test_rounded_avg_single_element_range():
    """Covers loop entry with exactly one iteration (lines 5-8)."""
    # summation = 7, count = 1 -> avg = 7 -> bin(7) == '0b111'
    assert rounded_avg(7, 7) == bin(7)
    assert rounded_avg(7, 7) == "0b111"


def test_rounded_avg_normal_case_summation_and_loop():
    """Covers lines 5-8 with multiple loop iterations."""
    # n=1, m=5: summation = 1+2+3+4+5 = 15, count = 5, avg = 3.0 -> bin(3)
    assert rounded_avg(1, 5) == bin(3)
    assert rounded_avg(1, 5) == "0b11"

    # n=0, m=10: summation = 55, count = 11, avg = 5.0 -> bin(5)
    assert rounded_avg(0, 10) == bin(5)
    assert rounded_avg(0, 10) == "0b101"


def test_rounded_avg_rounding_behavior():
    """Exercise round() on non-integer averages (line 8 division/round path)."""
    # n=1, m=2: summation = 3, count = 2, avg = 1.5 -> round -> 2
    assert rounded_avg(1, 2) == bin(2)
    assert rounded_avg(1, 2) == "0b10"

    # n=1, m=3: summation = 6, count = 3, avg = 2.0 (exact)
    assert rounded_avg(1, 3) == bin(2)
    assert rounded_avg(1, 3) == "0b10"

    # n=2, m=5: summation = 14, count = 4, avg = 3.5 -> round -> 4
    assert rounded_avg(2, 5) == bin(4)
    assert rounded_avg(2, 5) == "0b100"


def test_rounded_avg_negative_values():
    """Ensure loop and division work with negative bounds (line 6-8)."""
    # n=-3, m=-1: summation = -6, count = 3, avg = -2.0 -> bin(-2) == '-0b10'
    assert rounded_avg(-3, -1) == bin(-2)
    assert rounded_avg(-3, -1) == "-0b10"

    # n=-2, m=2: summation = 0, count = 5, avg = 0.0 -> bin(0) == '0b0'
    assert rounded_avg(-2, 2) == bin(0)
    assert rounded_avg(-2, 2) == "0b0"
