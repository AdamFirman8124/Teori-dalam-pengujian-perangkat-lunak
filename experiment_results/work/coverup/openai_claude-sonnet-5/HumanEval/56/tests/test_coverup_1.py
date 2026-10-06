# file: script_56.py:1-22
# asked: {"lines": [14, 15, 16, 17, 19, 20, 21, 22], "branches": [[15, 16], [15, 22], [16, 17], [16, 19], [20, 15], [20, 21]]}
# gained: {"lines": [14, 15, 16, 17, 19, 20, 21, 22], "branches": [[15, 16], [15, 22], [16, 17], [16, 19], [20, 15], [20, 21]]}

import pytest
from script_56 import correct_bracketing


def test_correct_bracketing_single_open():
    """Test single opening bracket returns False"""
    assert correct_bracketing("<") == False


def test_correct_bracketing_single_pair():
    """Test single pair of brackets returns True"""
    assert correct_bracketing("<>") == True


def test_correct_bracketing_nested():
    """Test nested brackets return True"""
    assert correct_bracketing("<<><>>") == True


def test_correct_bracketing_starts_with_close():
    """Test string starting with closing bracket returns False"""
    assert correct_bracketing("><<>") == False


def test_correct_bracketing_empty_string():
    """Test empty string returns True"""
    assert correct_bracketing("") == True


def test_correct_bracketing_single_close():
    """Test single closing bracket returns False"""
    assert correct_bracketing(">") == False


def test_correct_bracketing_multiple_open():
    """Test multiple opening brackets without closes returns False"""
    assert correct_bracketing("<<<") == False


def test_correct_bracketing_balanced_multiple():
    """Test multiple balanced pairs returns True"""
    assert correct_bracketing("<><><>") == True


def test_correct_bracketing_close_then_open():
    """Test closing before opening in middle returns False"""
    assert correct_bracketing("<>><<>") == False


def test_correct_bracketing_deeply_nested():
    """Test deeply nested brackets return True"""
    assert correct_bracketing("<<<>>>") == True


def test_correct_bracketing_unbalanced_more_opens():
    """Test more opens than closes returns False"""
    assert correct_bracketing("<<><") == False
