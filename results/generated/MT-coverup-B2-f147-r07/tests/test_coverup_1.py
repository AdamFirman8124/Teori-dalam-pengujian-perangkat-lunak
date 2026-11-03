# file: project/f147/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 10], "branches": [[5, 6], [5, 10], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9]]}

"""Tests for f147.get_max_triples achieving full line and branch coverage.

get_max_triples is a pure function with no external state, I/O, or
module-level side effects, so no monkeypatching or cleanup is required;
each test leaves no state behind.
"""

from itertools import combinations

from f147 import get_max_triples


def _reference(n):
    """Independent brute-force implementation used to cross-check results."""
    A = [i * i - i + 1 for i in range(1, n + 1)]
    return sum(1 for a, b, c in combinations(A, 3) if (a + b + c) % 3 == 0)


def test_get_max_triples_n5_executes_all_lines_and_branches():
    # n=5 exercises every missing line (3-10):
    #   * line 3: list comprehension runs (A = [1, 3, 7, 13, 21])
    #   * lines 5-7: each loop body executes at least once AND each loop
    #     terminates (i=4 -> empty j-range, j=4 -> empty k-range), covering
    #     both the loop-entry and loop-exit branches
    #   * line 8: condition is True for the triple (1, 7, 13) (sum 21) and
    #     False for all other triples, covering both if-branches
    #   * line 9: executed when the condition is True
    #   * line 10: return statement executed
    result = get_max_triples(5)
    # A = [1, 3, 7, 13, 21]; the only valid triple is (1, 7, 13) because
    # 1 + 7 + 13 == 21 and 21 % 3 == 0.
    assert result == 1
    assert result == _reference(5)


def test_get_max_triples_various_sizes():
    # Edge cases where no triple can satisfy the condition, plus larger
    # sizes for extra confidence in the counting logic.
    assert get_max_triples(0) == 0 == _reference(0)  # empty array
    assert get_max_triples(1) == 0 == _reference(1)  # too few elements
    assert get_max_triples(2) == 0 == _reference(2)  # too few elements
    assert get_max_triples(3) == 0 == _reference(3)  # 1+3+7=11, not %3==0
    assert get_max_triples(4) == 1 == _reference(4)  # only (1, 7, 13)
    assert get_max_triples(6) == 4 == _reference(6)  # C(4,3) all-1-mod-3 picks
