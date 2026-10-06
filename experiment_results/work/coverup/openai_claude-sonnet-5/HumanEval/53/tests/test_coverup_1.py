# file: script_53.py:1-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

import pytest
from script_53 import add


def test_add_positive_numbers():
    """Test adding two positive numbers."""
    result = add(2, 3)
    assert result == 5


def test_add_different_positive_numbers():
    """Test adding different positive numbers."""
    result = add(5, 7)
    assert result == 12


def test_add_zero():
    """Test adding zero."""
    result = add(0, 0)
    assert result == 0


def test_add_negative_numbers():
    """Test adding negative numbers."""
    result = add(-5, -3)
    assert result == -8


def test_add_mixed_signs():
    """Test adding positive and negative numbers."""
    result = add(10, -3)
    assert result == 7
