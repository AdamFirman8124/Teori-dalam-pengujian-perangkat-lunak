# file: project/f115/__init__.py:1-4
# asked: {"lines": [2, 4], "branches": []}
# gained: {"lines": [2, 4], "branches": []}

def test_max_fill_rounds_each_row_up_to_capacity():
    from f115 import max_fill

    grid = [[1, 2, 3], [4], [], [5, 5]]

    assert max_fill(grid, capacity=4) == 6
