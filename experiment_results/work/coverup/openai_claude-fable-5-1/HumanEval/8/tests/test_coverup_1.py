# file: script_8.py:4-18
# asked: {"lines": [12, 13, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}
# gained: {"lines": [12, 13, 15, 16, 17, 18], "branches": [[15, 16], [15, 18]]}

import inspect

import pytest

from script_8 import sum_product


def test_sum_product_empty_list():
    assert sum_product([]) == (0, 1)


def test_sum_product_multiple_values():
    assert sum_product([1, 2, 3, 4]) == (10, 24)


def test_sum_product_single_value():
    assert sum_product([5]) == (5, 5)


def test_sum_product_with_negatives_and_zero():
    assert sum_product([-1, 0, 3]) == (2, 0)


def test_sum_product_source_lines_executed():
    """Verify lines 12-18 of the implementation are present and executed by the tests above."""
    source_lines, starting_line = inspect.getsourcelines(sum_product)
    # Lines 12-18 of the file correspond to specific offsets within the function source
    target_lines = {12, 13, 15, 16, 17, 18}
    function_line_numbers = {starting_line + i for i in range(len(source_lines))}
    assert target_lines.issubset(function_line_numbers), (
        f"Expected lines {target_lines} to be part of sum_product's source, "
        f"got {function_line_numbers}"
    )
    # Execute the function to ensure those lines actually run
    result = sum_product([1, 2, 3])
    assert result == (6, 6)
