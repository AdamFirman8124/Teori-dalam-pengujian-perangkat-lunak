# file: project/f103/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

from f103 import rounded_avg


def test_rounded_avg_m_less_than_n():
    assert rounded_avg(5, 1) == -1
    assert rounded_avg(10, 5) == -1


def test_rounded_avg_normal_range():
    # 1+2+3+4+5=15, 15/5=3 -> bin(3) == '0b11'
    assert rounded_avg(1, 5) == "0b11"


def test_rounded_avg_single_element():
    # n == m: summation=5, count=1, avg=5 -> bin(5) == '0b101'
    assert rounded_avg(5, 5) == "0b101"
