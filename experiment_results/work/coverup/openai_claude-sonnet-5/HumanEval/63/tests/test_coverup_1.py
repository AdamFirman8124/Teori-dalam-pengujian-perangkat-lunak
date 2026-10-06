# file: script_63.py:1-21
# asked: {"lines": [15, 16, 17, 18, 19, 20, 21], "branches": [[15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21]]}
# gained: {"lines": [15, 16, 17, 18, 19, 20, 21], "branches": [[15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21]]}

import sys
import pytest


def test_fibfib_base_case_0():
    """Test base case n=0"""
    from script_63 import fibfib
    assert fibfib(0) == 0


def test_fibfib_base_case_1():
    """Test base case n=1"""
    from script_63 import fibfib
    assert fibfib(1) == 0


def test_fibfib_base_case_2():
    """Test base case n=2"""
    from script_63 import fibfib
    assert fibfib(2) == 1


def test_fibfib_recursive_case():
    """Test recursive case with n=3"""
    from script_63 import fibfib
    assert fibfib(3) == 1


def test_fibfib_larger_value():
    """Test with n=5"""
    from script_63 import fibfib
    assert fibfib(5) == 4


def test_fibfib_even_larger_value():
    """Test with n=8"""
    from script_63 import fibfib
    assert fibfib(8) == 24
