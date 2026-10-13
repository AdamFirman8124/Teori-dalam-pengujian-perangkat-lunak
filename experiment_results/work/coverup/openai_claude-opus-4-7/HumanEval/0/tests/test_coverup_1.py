# file: script_0.py:4-19
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}

from typing import List

from script_0 import has_close_elements


def test_has_close_elements_no_close_pairs():
    # Executes the loops, the idx != idx2 branch, and falls through to line 19.
    numbers: List[float] = [1.0, 2.0, 3.0]
    threshold = 0.5
    result = has_close_elements(numbers, threshold)
    assert result is False


def test_has_close_elements_finds_close_pair():
    # Executes the return True path (line 17).
    numbers: List[float] = [1.0, 2.8, 3.0, 4.0, 5.0, 2.0]
    threshold = 0.3
    result = has_close_elements(numbers, threshold)
    assert result is True


def test_has_close_elements_empty_list():
    # The enumerate loops never iterate; line 19 executes.
    result = has_close_elements([], 1.0)
    assert result is False


def test_has_close_elements_single_element():
    # The inner loop iterates once, idx == idx2 is always true, so the
    # if-branch body (lines 15-17) is skipped and line 19 executes.
    result = has_close_elements([42.0], 1.0)
    assert result is False


def test_has_close_elements_duplicate_values():
    # Duplicate equal elements produce distance 0 < threshold -> return True.
    result = has_close_elements([5.0, 5.0], 0.1)
    assert result is True


def test_has_close_elements_negative_values():
    # Distance is computed with abs, covering negative operands -> return True.
    result = has_close_elements([-1.0, -1.05], 0.1)
    assert result is True


def test_has_close_elements_threshold_boundary_not_close():
    # distance == threshold is NOT less than threshold -> line 19 executes.
    result = has_close_elements([0.0, 1.0], 1.0)
    assert result is False


def test_has_close_elements_pair_far_apart():
    # idx != idx2 is reached for all pairs but distance >= threshold -> line 19.
    result = has_close_elements([10.0, 20.0, 30.0], 1.0)
    assert result is False
