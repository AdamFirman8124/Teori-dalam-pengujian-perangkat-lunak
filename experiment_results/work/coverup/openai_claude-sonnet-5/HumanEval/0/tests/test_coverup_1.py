# file: script_0.py:4-19
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from script_0 import has_close_elements


def test_doctest_far_apart():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) is False


def test_doctest_close():
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) is True


def test_empty_and_single():
    assert has_close_elements([], 0.5) is False
    assert has_close_elements([1.0], 0.5) is False


def test_duplicate_values():
    assert has_close_elements([1.0, 1.0], 0.1) is True


def test_negative_and_order():
    assert has_close_elements([-1.0, -1.05, 5.0], 0.1) is True
    assert has_close_elements([-1.0, -1.05, 5.0], 0.01) is False


def test_threshold_boundary():
    # distance exactly equal to threshold (1.0) -> not closer -> False
    assert has_close_elements([1.0, 2.0], 1.0) is False
    # distance larger than threshold -> False
    assert has_close_elements([1.0, 2.0], 0.5) is False
    # distance smaller than threshold -> True
    assert has_close_elements([1.0, 2.0], 2.0) is True


def test_early_return_and_unequal_lengths():
    assert has_close_elements([0.0, 0.1, 10.0], 0.5) is True
