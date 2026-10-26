# file: project/f151/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f151 import double_the_difference


def test_double_the_difference_executes_line_3():
    # Odd positives: 1^2 + 3^2 = 1 + 9 = 10
    assert double_the_difference([1, 3]) == 10


def test_double_the_difference_filters():
    # Negative, even, and float values must be excluded
    assert double_the_difference([-1, -3, 2, 4, 1.5, 0]) == 0


def test_double_the_difference_empty():
    assert double_the_difference([]) == 0


def test_double_the_difference_mixed():
    # 1^2 + 5^2 = 26; -3, 2, 4.0 excluded
    assert double_the_difference([1, 5, -3, 2, 4.0]) == 26
