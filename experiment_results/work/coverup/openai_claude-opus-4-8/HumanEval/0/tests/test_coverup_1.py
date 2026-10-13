# file: script_0.py:4-19
# asked: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 19], "branches": [[12, 13], [12, 19], [13, 12], [13, 14], [14, 13], [14, 15], [16, 13], [16, 17]]}

import importlib

import pytest


@pytest.fixture
def has_close_elements():
    module = importlib.import_module("script_0")
    return module.has_close_elements


def test_returns_false_when_far_apart(has_close_elements):
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) is False


def test_returns_true_when_close_pair_exists(has_close_elements):
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) is True


def test_single_element_returns_false(has_close_elements):
    assert has_close_elements([1.0], 0.1) is False


def test_empty_list_returns_false(has_close_elements):
    assert has_close_elements([], 0.1) is False


def test_distance_exactly_equal_to_threshold_returns_false(has_close_elements):
    assert has_close_elements([1.0, 2.0], 1.0) is False


def test_negative_threshold_returns_false(has_close_elements):
    assert has_close_elements([1.0, 1.1, 2.0], -0.5) is False


def test_equal_elements_return_true(has_close_elements):
    assert has_close_elements([5.0, 5.0], 1e-9) is True


def test_input_list_is_not_mutated(has_close_elements):
    numbers = [3.0, 1.0, 2.0]
    assert has_close_elements(numbers, 1.5) is True
    assert numbers == [3.0, 1.0, 2.0]


def test_docstring_examples():
    module = importlib.import_module("script_0")
    doc = module.has_close_elements.__doc__
    assert "has_close_elements" in doc
