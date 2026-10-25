# file: project/f115/__init__.py:1-4
# asked: {"lines": [2, 4], "branches": []}
# gained: {"lines": [2, 4], "branches": []}

from f115 import max_fill


def test_max_fill_rounds_up_each_row():
    assert max_fill([[1, 2], [3, 4], []], 3) == 4


def test_max_fill_empty_grid():
    assert max_fill([], 5) == 0
