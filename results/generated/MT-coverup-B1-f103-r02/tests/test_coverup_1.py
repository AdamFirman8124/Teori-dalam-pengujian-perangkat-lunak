# file: project/f103/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[3, 4], [3, 5], [6, 7], [6, 8]]}

from f103 import rounded_avg


def test_rounded_avg_returns_minus_one_for_reversed_range():
    assert rounded_avg(5, 1) == -1


def test_rounded_avg_returns_binary_rounded_average():
    assert rounded_avg(1, 5) == "0b11"
