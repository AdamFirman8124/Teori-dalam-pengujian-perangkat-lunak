# file: project/f115/__init__.py:1-4
# asked: {"lines": [2, 4], "branches": []}
# gained: {"lines": [2, 4], "branches": []}

def test_max_fill_calculates_required_capacity_units():
    from f115 import max_fill

    grid = [[0, 0], [1, 2], [3, 4]]

    assert max_fill(grid, capacity=3) == 4
    assert grid == [[0, 0], [1, 2], [3, 4]]
