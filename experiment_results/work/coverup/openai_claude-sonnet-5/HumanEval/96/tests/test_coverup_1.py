# file: script_96.py:1-21
# asked: {"lines": [12, 13, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[13, 14], [13, 21], [15, 16], [15, 19], [16, 15], [16, 17], [19, 13], [19, 20]]}
# gained: {"lines": [12, 13, 14, 15, 16, 17, 18, 19, 20, 21], "branches": [[13, 14], [13, 21], [15, 16], [15, 19], [16, 15], [16, 17], [19, 13], [19, 20]]}

import pytest
from script_96 import count_up_to


def test_count_up_to_5():
    """Test that count_up_to(5) returns [2, 3]"""
    result = count_up_to(5)
    assert result == [2, 3]


def test_count_up_to_11():
    """Test that count_up_to(11) returns [2, 3, 5, 7]"""
    result = count_up_to(11)
    assert result == [2, 3, 5, 7]


def test_count_up_to_0():
    """Test that count_up_to(0) returns []"""
    result = count_up_to(0)
    assert result == []


def test_count_up_to_20():
    """Test that count_up_to(20) returns [2, 3, 5, 7, 11, 13, 17, 19]"""
    result = count_up_to(20)
    assert result == [2, 3, 5, 7, 11, 13, 17, 19]


def test_count_up_to_1():
    """Test that count_up_to(1) returns []"""
    result = count_up_to(1)
    assert result == []


def test_count_up_to_18():
    """Test that count_up_to(18) returns [2, 3, 5, 7, 11, 13, 17]"""
    result = count_up_to(18)
    assert result == [2, 3, 5, 7, 11, 13, 17]


def test_count_up_to_2():
    """Test edge case: count_up_to(2) returns []"""
    result = count_up_to(2)
    assert result == []


def test_count_up_to_3():
    """Test that count_up_to(3) returns [2]"""
    result = count_up_to(3)
    assert result == [2]


def test_count_up_to_4():
    """Test that count_up_to(4) returns [2, 3] - includes composite number"""
    result = count_up_to(4)
    assert result == [2, 3]


def test_count_up_to_composite():
    """Test with composite numbers to ensure branch coverage"""
    result = count_up_to(10)
    assert result == [2, 3, 5, 7]
    assert 4 not in result
    assert 6 not in result
    assert 8 not in result
    assert 9 not in result
