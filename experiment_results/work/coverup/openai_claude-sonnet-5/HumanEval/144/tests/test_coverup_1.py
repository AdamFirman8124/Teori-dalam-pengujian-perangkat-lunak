# file: script_144.py:1-19
# asked: {"lines": [13, 14, 15, 16, 17, 18, 19], "branches": [[17, 18], [17, 19]]}
# gained: {"lines": [13, 14, 15, 16, 17, 18, 19], "branches": [[17, 18], [17, 19]]}

import pytest
from script_144 import simplify


def test_simplify_true_case():
    """Test case where x * n evaluates to a whole number"""
    assert simplify("1/5", "5/1") is True


def test_simplify_false_case():
    """Test case where x * n does not evaluate to a whole number"""
    assert simplify("1/6", "2/1") is False


def test_simplify_false_case_2():
    """Test another case where x * n does not evaluate to a whole number"""
    assert simplify("7/10", "10/2") is False


def test_simplify_whole_number_result():
    """Test case where multiplication results in a whole number"""
    assert simplify("2/4", "4/2") is True


def test_simplify_large_fractions_true():
    """Test with larger numbers that result in whole number"""
    assert simplify("10/20", "40/2") is True


def test_simplify_large_fractions_false():
    """Test with larger numbers that do not result in whole number"""
    assert simplify("3/7", "5/11") is False


def test_simplify_one_over_one():
    """Test with 1/1 fractions"""
    assert simplify("1/1", "1/1") is True
