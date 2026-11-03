# file: project/f111/__init__.py:1-15
# asked: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}

"""Tests for f111.histogram — covering lines 3-15 and all branches.

The function is pure (no I/O, no module state), so no monkeypatching or
cleanup fixtures are required; each test only relies on its own inputs.
"""

from f111 import histogram


def test_histogram_single_most_frequent_word():
    """A single word dominates: covers lines 3-5, the loop 7-9 (both the True
    branch when a new max is found and the False branch when count <= t),
    the True branch of `t > 0`, the loop 11-12 (True and False branches,
    since 'banana' is skipped), line 14 and the return on line 15."""
    result = histogram("apple banana apple")
    assert result == {"apple": 2}


def test_histogram_ties_multiple_words():
    """Several words tie at the maximum count: exercises repeated updates of
    `t` in lines 7-9 and the False branch of `list1.count(i) == t` when 'c'
    (count 1) is skipped in the second loop."""
    result = histogram("a b a b c")
    assert result == {"a": 2, "b": 2}


def test_histogram_maximum_increases_progressively():
    """The running maximum `t` is raised more than once (1 -> 2 -> 3),
    exercising line 9 repeatedly before the second loop runs."""
    result = histogram("x y y z z z")
    assert result == {"z": 3}


def test_histogram_empty_string_returns_empty_dict():
    """An empty string splits to [''], so the `i != ''` guard is False and
    `t` stays 0; the False branch of `t > 0` is taken and an empty dict is
    returned (line 15 reached without entering the second loop)."""
    result = histogram("")
    assert result == {}
    assert isinstance(result, dict)
