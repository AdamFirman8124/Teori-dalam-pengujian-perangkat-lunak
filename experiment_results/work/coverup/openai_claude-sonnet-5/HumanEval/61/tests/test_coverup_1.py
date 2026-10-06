# file: script_61.py:1-22
# asked: {"lines": [14, 15, 16, 17, 19, 20, 21, 22], "branches": [[15, 16], [15, 22], [16, 17], [16, 19], [20, 15], [20, 21]]}
# gained: {"lines": [14, 15, 16, 17, 19, 20, 21, 22], "branches": [[15, 16], [15, 22], [16, 17], [16, 19], [20, 15], [20, 21]]}

import pytest
from script_61 import correct_bracketing


def test_correct_bracketing_empty_string():
    """Test empty string returns True (depth == 0)."""
    assert correct_bracketing("") == True


def test_correct_bracketing_single_open():
    """Test single opening bracket returns False."""
    assert correct_bracketing("(") == False


def test_correct_bracketing_single_close():
    """Test single closing bracket returns False (depth < 0)."""
    assert correct_bracketing(")") == False


def test_correct_bracketing_balanced_pair():
    """Test balanced pair returns True."""
    assert correct_bracketing("()") == True


def test_correct_bracketing_nested():
    """Test nested balanced brackets return True."""
    assert correct_bracketing("(()())") == True


def test_correct_bracketing_close_before_open():
    """Test closing bracket before opening returns False."""
    assert correct_bracketing(")(()") == False


def test_correct_bracketing_multiple_pairs():
    """Test multiple balanced pairs return True."""
    assert correct_bracketing("()()()") == True


def test_correct_bracketing_unbalanced_more_open():
    """Test more opening brackets than closing returns False."""
    assert correct_bracketing("(((") == False


def test_correct_bracketing_unbalanced_more_close():
    """Test more closing brackets than opening returns False."""
    assert correct_bracketing(")))") == False


def test_correct_bracketing_complex_balanced():
    """Test complex balanced structure returns True."""
    assert correct_bracketing("(()(()))") == True


def test_correct_bracketing_complex_unbalanced():
    """Test complex unbalanced structure returns False."""
    assert correct_bracketing("(()(()") == False
