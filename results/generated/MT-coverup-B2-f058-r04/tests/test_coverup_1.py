# file: project/f058/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}

from f058 import common


def test_common_with_intersection():
    # Exercises lines 3-8: set creation, both nested loops, the True branch
    # of the equality check, ret.add, and the sorted return.
    assert common([1, 2, 3], [2, 3, 4]) == [2, 3]


def test_common_no_intersection():
    # Exercises the False branch of the equality check (line 6) with
    # non-empty inputs, so both loop bodies still run.
    assert common([1, 2], [3, 4]) == []


def test_common_empty_l1():
    # Exercises line 4 with an empty l1: the outer loop body (lines 5-7)
    # never runs, but line 8 still returns.
    assert common([], [1, 2, 3]) == []


def test_common_empty_l2():
    # Exercises line 5 with an empty l2: the inner loop body (lines 6-7)
    # never runs even though the outer loop does.
    assert common([1, 2, 3], []) == []


def test_common_both_empty():
    # Both loops skipped entirely; only lines 3 and 8 run.
    assert common([], []) == []


def test_common_duplicates_deduplicated():
    # The set (line 3) must deduplicate repeated matches before sorting.
    assert common([1, 1, 2, 2], [2, 2, 1, 1]) == [1, 2]


def test_common_result_is_sorted():
    # Verifies the sorted() call on line 8 orders the result regardless
    # of input ordering: every element of l1 appears in l2, but in
    # descending order, so the returned list must be ascending.
    assert common([5, 3, 1], [5, 3, 1]) == [1, 3, 5]
