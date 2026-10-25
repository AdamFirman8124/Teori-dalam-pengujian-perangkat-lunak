# file: project/f152/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f152 import compare


def test_compare_returns_absolute_pairwise_differences():
    assert compare([1, 5, -2], [4, 3, 2]) == [3, 2, 4]
