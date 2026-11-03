# file: project/f115/__init__.py:1-4
# asked: {"lines": [2, 4], "branches": []}
# gained: {"lines": [2, 4], "branches": []}

import pytest

from f115 import max_fill


@pytest.mark.parametrize(
    "grid, capacity, expected",
    [
        # Classic HumanEval examples
        ([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1, 6),
        ([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2, 5),
        # Empty wells contribute zero trips
        ([[0, 0, 0], [0, 0, 0]], 5, 0),
        # Ceiling behaviour: partial bucket loads round up
        ([[1, 1, 1]], 2, 2),
        ([[1, 1, 1, 1]], 3, 2),
        # Exact multiples require no extra trip
        ([[1, 1, 1, 1]], 4, 1),
        # Single well, single unit
        ([[1]], 1, 1),
        # Empty grid -> no trips at all
        ([], 10, 0),
    ],
)
def test_max_fill(grid, capacity, expected):
    """max_fill must return the total number of bucket extractions,
    i.e. sum over wells of ceil(water_in_well / capacity)."""
    result = max_fill(grid, capacity)
    assert isinstance(result, int)
    assert result == expected


def test_max_fill_matches_manual_computation():
    """Verify against an independent manual computation."""
    grid = [[0, 1, 0, 1, 1], [1, 1, 1], [0, 0, 0]]
    capacity = 2
    # Well 1: 3 units -> ceil(3/2) = 2 trips
    # Well 2: 3 units -> ceil(3/2) = 2 trips
    # Well 3: 0 units -> ceil(0/2) = 0 trips
    expected = 2 + 2 + 0
    assert max_fill(grid, capacity) == expected


def test_max_fill_does_not_mutate_input():
    """The function must be side-effect free w.r.t. its argument."""
    grid = [[1, 0, 1], [0, 1, 0]]
    snapshot = [row[:] for row in grid]
    max_fill(grid, 1)
    assert grid == snapshot
