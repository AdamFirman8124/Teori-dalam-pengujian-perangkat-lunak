# file: script_46.py:1-24
# asked: {"lines": [16, 17, 18, 20, 21, 22, 24], "branches": [[17, 18], [17, 20], [20, 21], [20, 24]]}
# gained: {"lines": [16, 17, 18, 20, 21, 22, 24], "branches": [[17, 18], [17, 20], [20, 21], [20, 24]]}

import pytest
from script_46 import fib4


def test_fib4_base_cases():
    """Test base cases that are covered by existing tests."""
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0


def test_fib4_n_equals_4():
    """Test n=4 to trigger the loop execution (lines 16-24)."""
    assert fib4(4) == 2  # 0 + 0 + 2 + 0


def test_fib4_n_equals_5():
    """Test n=5 to execute loop logic."""
    assert fib4(5) == 4  # 0 + 2 + 0 + 2


def test_fib4_n_equals_6():
    """Test n=6 to execute loop logic."""
    assert fib4(6) == 8  # 2 + 0 + 2 + 4


def test_fib4_n_equals_7():
    """Test n=7 to execute loop logic."""
    assert fib4(7) == 14  # 0 + 2 + 4 + 8


def test_fib4_larger_value():
    """Test a larger value to ensure loop executes multiple times."""
    assert fib4(10) == 104
