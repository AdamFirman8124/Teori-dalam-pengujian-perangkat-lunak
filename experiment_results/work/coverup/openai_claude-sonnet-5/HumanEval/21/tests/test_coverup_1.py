# file: script_21.py:4-12
# asked: {"lines": [10, 11, 12], "branches": []}
# gained: {"lines": [10, 11, 12], "branches": []}

import pytest
from typing import List
from script_21 import rescale_to_unit


def test_rescale_to_unit_basic():
    result = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    assert result == [0.0, 0.25, 0.5, 0.75, 1.0]


def test_rescale_to_unit_two_elements():
    result = rescale_to_unit([10.0, 20.0])
    assert result == [0.0, 1.0]


def test_rescale_to_unit_negative_numbers():
    result = rescale_to_unit([-5.0, 0.0, 5.0])
    assert result == [0.0, 0.5, 1.0]


def test_rescale_to_unit_all_same_except_one():
    result = rescale_to_unit([1.0, 1.0, 2.0])
    assert result == [0.0, 0.0, 1.0]


def test_rescale_to_unit_floats_with_precision():
    result = rescale_to_unit([0.5, 1.5, 2.5])
    assert len(result) == 3
    assert result[0] == 0.0
    assert result[1] == 0.5
    assert result[2] == 1.0
