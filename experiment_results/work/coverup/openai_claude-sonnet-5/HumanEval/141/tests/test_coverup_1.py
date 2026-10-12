# file: script_141.py:1-28
# asked: {"lines": [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], "branches": [[17, 18], [17, 19], [19, 20], [19, 21], [21, 22], [21, 23], [23, 24], [23, 25], [26, 27], [26, 28]]}
# gained: {"lines": [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], "branches": [[17, 18], [17, 19], [19, 20], [19, 21], [21, 22], [21, 23], [23, 24], [23, 25], [26, 27], [26, 28]]}

import pytest
from script_141 import file_name_check


def test_file_name_check_valid_txt():
    """Test valid file name with .txt extension"""
    assert file_name_check("example.txt") == 'Yes'


def test_file_name_check_valid_exe():
    """Test valid file name with .exe extension"""
    assert file_name_check("file.exe") == 'Yes'


def test_file_name_check_valid_dll():
    """Test valid file name with .dll extension"""
    assert file_name_check("program.dll") == 'Yes'


def test_file_name_check_invalid_starts_with_digit():
    """Test invalid file name starting with digit"""
    assert file_name_check("1example.dll") == 'No'


def test_file_name_check_invalid_multiple_dots():
    """Test invalid file name with multiple dots"""
    assert file_name_check("file.name.txt") == 'No'


def test_file_name_check_invalid_no_dots():
    """Test invalid file name with no dots"""
    assert file_name_check("filename") == 'No'


def test_file_name_check_invalid_extension():
    """Test invalid file name with wrong extension"""
    assert file_name_check("file.pdf") == 'No'


def test_file_name_check_empty_name_before_dot():
    """Test invalid file name with empty substring before dot"""
    assert file_name_check(".txt") == 'No'


def test_file_name_check_starts_with_special_char():
    """Test invalid file name starting with special character"""
    assert file_name_check("_file.txt") == 'No'


def test_file_name_check_more_than_three_digits():
    """Test invalid file name with more than 3 digits"""
    assert file_name_check("file1234.txt") == 'No'


def test_file_name_check_exactly_three_digits():
    """Test valid file name with exactly 3 digits"""
    assert file_name_check("file123.txt") == 'Yes'


def test_file_name_check_uppercase_start():
    """Test valid file name starting with uppercase letter"""
    assert file_name_check("File.exe") == 'Yes'


def test_file_name_check_lowercase_start():
    """Test valid file name starting with lowercase letter"""
    assert file_name_check("file.dll") == 'Yes'
