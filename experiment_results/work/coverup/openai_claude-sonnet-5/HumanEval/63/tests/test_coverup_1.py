# file: script_63.py:1-21
# asked: {"lines": [15, 16, 17, 18, 19, 20, 21], "branches": [[15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21]]}
# gained: {"lines": [15, 16, 17, 18, 19, 20, 21], "branches": [[15, 16], [15, 17], [17, 18], [17, 19], [19, 20], [19, 21]]}

import pytest
import sys
import os

# Add the directory containing script_63.py to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from script_63 import fibfib


def test_fibfib_base_case_0():
    assert fibfib(0) == 0


def test_fibfib_base_case_1():
    assert fibfib(1) == 0


def test_fibfib_base_case_2():
    assert fibfib(2) == 1


def test_fibfib_recursive_case_3():
    assert fibfib(3) == 1


def test_fibfib_recursive_case_5():
    assert fibfib(5) == 4


def test_fibfib_recursive_case_8():
    assert fibfib(8) == 24
