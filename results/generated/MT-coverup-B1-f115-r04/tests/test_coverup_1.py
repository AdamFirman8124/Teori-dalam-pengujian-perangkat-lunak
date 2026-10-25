# file: project/f115/__init__.py:1-4
# asked: {"lines": [2, 4], "branches": []}
# gained: {"lines": [2, 4], "branches": []}

from f115 import max_fill


def test_max_fill_with_nonempty_grid():
    assert max_fill([[2, 3, 1], [4, 2], [1]], capacity=4) == 5


def test_max_fill_with_empty_grid():
    assert max_fill([], capacity=4) == 0
