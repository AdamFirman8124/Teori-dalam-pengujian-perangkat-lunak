# file: project/f067/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

from f067 import fruit_distribution


def test_fruit_distribution_counts_only_numeric_tokens():
    assert fruit_distribution("5 apples and 6 oranges", 20) == 9


def test_fruit_distribution_with_no_numeric_tokens():
    assert fruit_distribution("apples and oranges", 20) == 20
