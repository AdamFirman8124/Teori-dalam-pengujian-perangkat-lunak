# file: project/f067/__init__.py:1-7
# asked: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}
# gained: {"lines": [3, 4, 5, 6, 7], "branches": [[4, 5], [4, 7], [5, 4], [5, 6]]}

import pytest

from f067 import fruit_distribution


def test_fruit_distribution_with_digits():
    """Covers lines 3-7: digits present, both branches of isdigit taken."""
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8


def test_fruit_distribution_with_zero_and_one():
    """Covers digit branch with '0' and '1' tokens."""
    assert fruit_distribution("0 apples and 1 oranges", 3) == 2


def test_fruit_distribution_no_digits():
    """Covers the False branch of isdigit for every token (line 5 False)."""
    assert fruit_distribution("two apples and three oranges", 5) == 5


def test_fruit_distribution_empty_string():
    """Covers loop body never executing (empty split result)."""
    assert fruit_distribution("", 10) == 10


def test_fruit_distribution_only_digits():
    """Covers consecutive digit tokens summed correctly."""
    assert fruit_distribution("1 2 3", 10) == 4


def test_fruit_distribution_mixed_tokens():
    """Covers mixed digit/non-digit tokens in one string."""
    assert fruit_distribution("apples 7 and 4 oranges 2", 20) == 7
