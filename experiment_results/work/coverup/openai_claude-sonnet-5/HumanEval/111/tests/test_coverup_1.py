# file: script_111.py:1-26
# asked: {"lines": [14, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26], "branches": [[18, 19], [18, 21], [19, 18], [19, 20], [21, 22], [21, 26], [22, 23], [22, 26], [23, 22], [23, 25]]}
# gained: {"lines": [14, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26], "branches": [[18, 19], [18, 21], [19, 18], [19, 20], [21, 22], [21, 26], [22, 23], [22, 26], [23, 22], [23, 25]]}

import pytest
from script_111 import histogram


def test_histogram_empty_string():
    """Test histogram with empty string"""
    assert histogram('') == {}


def test_histogram_single_occurrence():
    """Test histogram with single occurrence of each letter"""
    assert histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}


def test_histogram_two_occurrences():
    """Test histogram with two occurrences"""
    assert histogram('a b b a') == {'a': 2, 'b': 2}


def test_histogram_mixed_occurrences():
    """Test histogram with mixed occurrences returning max"""
    assert histogram('a b c a b') == {'a': 2, 'b': 2}


def test_histogram_single_max():
    """Test histogram with single letter having max occurrences"""
    assert histogram('b b b b a') == {'b': 4}


def test_histogram_with_extra_spaces():
    """Test histogram with extra spaces between letters"""
    result = histogram('a  b  a')
    assert result == {'a': 2, '': 2}


def test_histogram_single_letter():
    """Test histogram with single letter"""
    assert histogram('x') == {'x': 1}


def test_histogram_all_same_letter():
    """Test histogram with all same letters"""
    assert histogram('z z z') == {'z': 3}


def test_histogram_three_way_tie():
    """Test histogram with three letters tied for max"""
    assert histogram('a a b b c c') == {'a': 2, 'b': 2, 'c': 2}
