# file: script_46.py:1-24
# asked: {"lines": [16, 17, 18, 20, 21, 22, 24], "branches": [[17, 18], [17, 20], [20, 21], [20, 24]]}
# gained: {"lines": [16, 17, 18, 20, 21, 22, 24], "branches": [[17, 18], [17, 20], [20, 21], [20, 24]]}

import pytest
from script_46 import fib4


def test_fib4_base_cases():
    """Test base cases that are handled by the lookup table."""
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0


def test_fib4_case_4():
    """Test n=4 which triggers the loop for the first time."""
    assert fib4(4) == 2


def test_fib4_case_5():
    """Test n=5."""
    assert fib4(5) == 4


def test_fib4_case_6():
    """Test n=6."""
    assert fib4(6) == 8


def test_fib4_case_7():
    """Test n=7."""
    assert fib4(7) == 14


def test_fib4_case_10():
    """Test a larger value to ensure the sliding window works correctly."""
    # fib4(8) = 14 + 8 + 4 + 2 = 28
    # fib4(9) = 28 + 14 + 8 + 4 = 54
    # fib4(10) = 54 + 28 + 14 + 8 = 104
    assert fib4(10) == 104
