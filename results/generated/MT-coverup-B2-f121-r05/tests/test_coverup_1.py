# file: project/f121/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f121 import solution


def test_solution_sums_odd_values_at_even_indices():
    values = [1, 3, 2, 5, 7]

    result = solution(values)

    assert result == 8
    assert values == [1, 3, 2, 5, 7]
