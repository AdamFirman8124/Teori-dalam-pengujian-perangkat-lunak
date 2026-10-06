# file: script_27.py:1-6
# asked: {"lines": [6], "branches": []}
# gained: {"lines": [6], "branches": []}

import pytest
from script_27 import flip_case


def test_flip_case_mixed():
    """Test flipping case with mixed uppercase and lowercase."""
    assert flip_case('Hello') == 'hELLO'


def test_flip_case_all_lowercase():
    """Test flipping case with all lowercase characters."""
    assert flip_case('hello') == 'HELLO'


def test_flip_case_all_uppercase():
    """Test flipping case with all uppercase characters."""
    assert flip_case('HELLO') == 'hello'


def test_flip_case_empty_string():
    """Test flipping case with an empty string."""
    assert flip_case('') == ''


def test_flip_case_numbers_and_special_chars():
    """Test flipping case with numbers and special characters."""
    assert flip_case('Hello123!@#') == 'hELLO123!@#'


def test_flip_case_spaces():
    """Test flipping case with spaces."""
    assert flip_case('Hello World') == 'hELLO wORLD'
