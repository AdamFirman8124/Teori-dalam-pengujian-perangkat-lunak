# file: script_53.py:1-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

import pytest
from script_53 import add


def test_add_positive_numbers():
    """Test adding two positive numbers."""
    assert add(2, 3) == 5


def test_add_different_positive_numbers():
    """Test adding different positive numbers."""
    assert add(5, 7) == 12


def test_add_zero():
    """Test adding zero."""
    assert add(0, 5) == 5
    assert add(5, 0) == 5


def test_add_negative_numbers():
    """Test adding negative numbers."""
    assert add(-2, -3) == -5
    assert add(-5, 3) == -2
    assert add(5, -3) == 2


def test_add_large_numbers():
    """Test adding large numbers."""
    assert add(1000000, 2000000) == 3000000
