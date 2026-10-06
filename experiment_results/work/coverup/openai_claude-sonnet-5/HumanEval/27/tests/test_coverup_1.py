# file: script_27.py:1-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest
from script_27 import flip_case


def test_flip_case_mixed():
    """Test flip_case with mixed case string."""
    assert flip_case('Hello') == 'hELLO'


def test_flip_case_lowercase():
    """Test flip_case with all lowercase string."""
    assert flip_case('hello') == 'HELLO'


def test_flip_case_uppercase():
    """Test flip_case with all uppercase string."""
    assert flip_case('HELLO') == 'hello'


def test_flip_case_empty():
    """Test flip_case with empty string."""
    assert flip_case('') == ''


def test_flip_case_numbers_and_special():
    """Test flip_case with numbers and special characters."""
    assert flip_case('Test123!@#') == 'tEST123!@#'


def test_flip_case_only_numbers():
    """Test flip_case with only numbers."""
    assert flip_case('12345') == '12345'


def test_flip_case_spaces():
    """Test flip_case with spaces."""
    assert flip_case('Hello World') == 'hELLO wORLD'
