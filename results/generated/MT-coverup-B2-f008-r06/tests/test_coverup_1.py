# file: project/f008/__init__.py:4-12
# asked: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}
# gained: {"lines": [6, 7, 9, 10, 11, 12], "branches": [[9, 10], [9, 12]]}

from f008 import sum_product


def test_sum_product_empty_list_skips_loop_body():
    # Empty input: lines 6-7 and 12 execute, loop body (9-11) does not.
    result = sum_product([])
    assert result == (0, 1)
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_sum_product_single_element_executes_loop_body():
    # One element: loop body executes exactly once.
    assert sum_product([5]) == (5, 5)


def test_sum_product_multiple_elements():
    # Multiple elements: loop body executes repeatedly, accumulating both values.
    numbers = [1, 2, 3, 4]
    total, product = sum_product(numbers)
    assert total == 10
    assert product == 24
    assert (total, product) == (sum(numbers), 24)


def test_sum_product_with_zero_and_negatives():
    # Zero makes the product zero; negatives exercise sign handling.
    assert sum_product([0, 7]) == (7, 0)
    assert sum_product([-2, -3, 4]) == (-1, 24)


def test_sum_product_does_not_mutate_input():
    numbers = [2, 3, 5]
    original = list(numbers)
    sum_product(numbers)
    assert numbers == original
