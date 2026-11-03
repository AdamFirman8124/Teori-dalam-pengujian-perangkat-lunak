# file: project/f058/__init__.py:1-8
# asked: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8], "branches": [[4, 5], [4, 8], [5, 4], [5, 6], [6, 5], [6, 7]]}

import pytest

from f058 import common


def test_common_with_intersection_covers_all_lines():
    # Exercises: set creation, nested loops, equality branch (True),
    # ret.add, and the final sorted return.
    result = common([1, 2, 3], [2, 3, 4])
    assert result == [2, 3]
    assert isinstance(result, list)
    assert result == sorted(result)


def test_common_without_intersection():
    # Loops run and the equality branch is evaluated (False path),
    # returning an empty sorted list.
    result = common([1, 2], [3, 4])
    assert result == []
    assert isinstance(result, list)


def test_common_deduplicates_and_sorts():
    # Duplicated matches collapse via the set; result comes out sorted.
    result = common([3, 1, 3, 2], [2, 3, 3, 1])
    assert result == [1, 2, 3]
    assert len(result) == len(set(result))


def test_common_empty_inputs():
    # Empty l1 skips inner loop entirely; still returns a sorted list.
    assert common([], [1, 2]) == []
    # Non-empty l1 with empty l2 exercises outer loop only.
    assert common([1, 2], []) == []
