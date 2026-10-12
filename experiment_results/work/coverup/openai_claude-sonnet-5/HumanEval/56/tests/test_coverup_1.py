# file: script_56.py:1-22
# asked: {"lines": [14, 15, 16, 17, 19, 20, 21, 22], "branches": [[15, 16], [15, 22], [16, 17], [16, 19], [20, 15], [20, 21]]}
# gained: {"lines": [14, 15, 16, 17, 19, 20, 21, 22], "branches": [[15, 16], [15, 22], [16, 17], [16, 19], [20, 15], [20, 21]]}

import pytest
from script_56 import correct_bracketing


def test_correct_bracketing_single_opening():
    """Test single opening bracket returns False"""
    assert correct_bracketing("<") == False


def test_correct_bracketing_single_pair():
    """Test single matched pair returns True"""
    assert correct_bracketing("<>") == True


def test_correct_bracketing_nested():
    """Test nested brackets return True"""
    assert correct_bracketing("<<><>>") == True


def test_correct_bracketing_closing_first():
    """Test closing bracket before opening returns False"""
    assert correct_bracketing("><<>") == False


def test_correct_bracketing_empty():
    """Test empty string returns True"""
    assert correct_bracketing("") == True


def test_correct_bracketing_multiple_opening():
    """Test multiple opening brackets without closing returns False"""
    assert correct_bracketing("<<<") == False


def test_correct_bracketing_multiple_closing():
    """Test multiple closing brackets returns False"""
    assert correct_bracketing(">>>") == False


def test_correct_bracketing_balanced_complex():
    """Test complex balanced brackets return True"""
    assert correct_bracketing("<<>><<>>") == True


def test_correct_bracketing_unbalanced_extra_closing():
    """Test extra closing bracket returns False"""
    assert correct_bracketing("<><>>") == False


def test_correct_bracketing_unbalanced_extra_opening():
    """Test extra opening bracket returns False"""
    assert correct_bracketing("<<><") == False
