# file: script_83.py:1-7
# asked: {"lines": [6, 7], "branches": [[6, 6], [6, 7]]}
# gained: {"lines": [6, 7], "branches": [[6, 6], [6, 7]]}

import pytest
from script_83 import starts_one_ends


def test_starts_one_ends_n_equals_1():
    """Test when n is 1, should return 1 (only the digit 1 itself)"""
    assert starts_one_ends(1) == 1


def test_starts_one_ends_n_equals_2():
    """Test when n is 2, should return 18"""
    assert starts_one_ends(2) == 18


def test_starts_one_ends_n_equals_3():
    """Test when n is 3, should return 180"""
    assert starts_one_ends(3) == 180


def test_starts_one_ends_n_equals_4():
    """Test when n is 4, should return 1800"""
    assert starts_one_ends(4) == 1800
