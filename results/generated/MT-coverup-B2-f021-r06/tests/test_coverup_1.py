# file: project/f021/__init__.py:4-8
# asked: {"lines": [6, 7, 8], "branches": []}
# gained: {"lines": [6, 7, 8], "branches": []}

import pytest

from f021 import rescale_to_unit


def test_rescale_to_unit_basic_range():
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = rescale_to_unit(numbers)

    assert result == pytest.approx([0.0, 0.25, 0.5, 0.75, 1.0])
    assert min(result) == pytest.approx(0.0)
    assert max(result) == pytest.approx(1.0)
    assert len(result) == len(numbers)


def test_rescale_to_unit_negative_and_unsorted():
    numbers = [-5.0, 10.0, 0.0]
    result = rescale_to_unit(numbers)

    assert result == pytest.approx([0.0, 1.0, 1.0 / 3.0])
    assert min(result) == pytest.approx(0.0)
    assert max(result) == pytest.approx(1.0)


def test_rescale_to_unit_does_not_mutate_input():
    numbers = [3.0, 1.0, 2.0]
    original = list(numbers)

    rescale_to_unit(numbers)

    assert numbers == original


def test_rescale_to_unit_single_element_raises_zero_division():
    with pytest.raises(ZeroDivisionError):
        rescale_to_unit([42.0])


def test_rescale_to_unit_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        rescale_to_unit([])
