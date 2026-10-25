# file: project/f151/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f151 import double_the_difference


def test_double_the_difference_basic():
    assert double_the_difference([1, 3, 5]) == 35


def test_double_the_difference_skips_non_positive_and_even():
    assert double_the_difference([-2, -1, 0, 2, 4]) == 0


def test_double_the_difference_skips_floats():
    assert double_the_difference([1.5, 3.0, 1, 3]) == 10


def test_double_the_difference_empty_list():
    assert double_the_difference([]) == 0


def test_double_the_difference_mixed():
    # 1^2 + 5^2 = 26; -3, 2, and 0.5 are filtered out
    assert double_the_difference([1, -3, 2, 5, 0.5]) == 26
