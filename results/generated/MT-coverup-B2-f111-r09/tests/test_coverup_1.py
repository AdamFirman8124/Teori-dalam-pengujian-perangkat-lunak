# file: project/f111/__init__.py:1-15
# asked: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}

"""Tests for f111.histogram, covering every line and branch.

histogram is a pure function (no I/O, no module state, no side effects),
so no monkeypatching or teardown is required to avoid state pollution.
"""

from f111 import histogram


def test_histogram_tied_max_counts():
    # Every word reaches the maximum count, so all of them are stored
    # (covers the True branch of the second-loop comparison and the
    # dict assignment on line 14).
    result = histogram("a b b a")
    assert result == {"a": 2, "b": 2}


def test_histogram_single_most_frequent_word():
    # 'b' occurs once while the max is 2, exercising the False branch
    # of the second-loop comparison (line 12) as well as the False
    # branch of the first-loop comparison (count not greater than t).
    result = histogram("a a b")
    assert result == {"a": 2}


def test_histogram_single_word():
    # Minimal non-empty input: t becomes 1 and the single word is kept.
    result = histogram("hello")
    assert result == {"hello": 1}


def test_histogram_empty_string():
    # The only token is '', which is rejected by the i != '' guard
    # (False branch of the short-circuit condition), so t stays 0 and
    # the `if t > 0` body is skipped (False branch of line 10).
    assert histogram("") == {}


def test_histogram_only_spaces():
    # Splitting on spaces yields only empty tokens; none of them pass
    # the i != '' guard, so t remains 0 and the result is empty.
    assert histogram("   ") == {}
