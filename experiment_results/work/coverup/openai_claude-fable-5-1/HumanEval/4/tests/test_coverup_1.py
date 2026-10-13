# file: script_4.py:4-14
# asked: {"lines": [13, 14], "branches": []}
# gained: {"lines": [13, 14], "branches": []}

from script_4 import mean_absolute_deviation

def test_mean_absolute_deviation_basic():
    assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0

def test_mean_absolute_deviation_single_element():
    assert mean_absolute_deviation([5.0]) == 0.0

def test_mean_absolute_deviation_symmetric():
    assert mean_absolute_deviation([0.0, 10.0]) == 5.0
