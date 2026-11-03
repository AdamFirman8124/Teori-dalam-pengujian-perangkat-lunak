# file: project/f121/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f121 import solution


def test_solution_empty_list():
    """Exercises line 3 with an empty list: the comprehension loop exits
    immediately without evaluating the condition, covering the loop-exit
    branch of the comprehension."""
    assert solution([]) == 0


def test_solution_mixed_values():
    """Exercises line 3 with both matching and non-matching elements.

    - idx 0, x=1: idx%2==0 True, x%2==1 True   -> included
    - idx 1, x=2: idx%2==0 False (short-circuits the 'and') -> excluded
    - idx 2, x=3: idx%2==0 True, x%2==1 True   -> included
    - idx 3, x=4: idx%2==0 False (short-circuits the 'and') -> excluded

    Covers both True and False outcomes of the comprehension condition as
    well as the short-circuit branch of the 'and' operator.
    """
    assert solution([1, 2, 3, 4]) == 4


def test_solution_even_values_at_even_indices():
    """Exercises line 3 where idx%2==0 is True but x%2==1 is False, covering
    the False outcome of the second condition of the 'and' operator."""
    assert solution([2, 4, 6]) == 0
