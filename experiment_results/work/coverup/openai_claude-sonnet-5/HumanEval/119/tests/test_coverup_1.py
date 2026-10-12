# file: script_119.py:1-29
# asked: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}
# gained: {"lines": [16, 17, 18, 19, 20, 22, 23, 24, 25, 27, 28, 29], "branches": [[18, 19], [18, 25], [19, 20], [19, 22], [23, 18], [23, 24]]}

import pytest
from script_119 import match_parens


def test_match_parens_valid_concatenation_order1():
    """Test case where first order creates valid parentheses."""
    assert match_parens(['()(', ')']) == 'Yes'


def test_match_parens_valid_concatenation_order2():
    """Test case where second order creates valid parentheses."""
    assert match_parens(['(', ')']) == 'Yes'


def test_match_parens_both_closing():
    """Test case where both strings are closing parentheses."""
    assert match_parens([')', ')']) == 'No'


def test_match_parens_both_opening():
    """Test case where both strings are opening parentheses."""
    assert match_parens(['(', '(']) == 'No'


def test_match_parens_unbalanced_total():
    """Test case where total parentheses cannot be balanced."""
    assert match_parens(['((', ')']) == 'No'


def test_match_parens_balanced_each():
    """Test case where each string is already balanced."""
    assert match_parens(['()', '()']) == 'Yes'


def test_match_parens_complex_valid():
    """Test case with more complex valid concatenation."""
    assert match_parens(['((', '))']) == 'Yes'


def test_match_parens_early_negative():
    """Test case where balance goes negative early."""
    assert match_parens(['))(', '(()']) == 'No'


def test_match_parens_empty_strings():
    """Test case with empty strings."""
    assert match_parens(['', '']) == 'Yes'


def test_match_parens_one_empty():
    """Test case with one empty string."""
    assert match_parens(['()', '']) == 'Yes'


def test_match_parens_closing_then_opening():
    """Test case where we need the right order to avoid early negative."""
    assert match_parens(['(()(', '))']) == 'Yes'


def test_match_parens_three_opening_three_closing():
    """Test case with multiple pairs."""
    assert match_parens(['(((', ')))']) == 'Yes'
