# file: project/f067/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f067 import fruit_distribution


def test_fruit_distribution_sums_digit_tokens():
    assert fruit_distribution("5 apples and 2 oranges", 12) == 5


def test_fruit_distribution_ignores_non_digit_tokens():
    assert fruit_distribution("no fruit here", 7) == 7
