# file: project/f111/__init__.py:1-15
# asked: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}

import pytest

from f111 import histogram


def test_histogram_single_most_frequent_word():
    """The most frequent word is mapped to its count; less frequent words are excluded.

    Covers: dict/list/t initialisation, first loop true branch (count > t),
    first loop false branch (count <= t), t > 0 true branch,
    inner loop true and false branches, and the return statement.
    """
    result = histogram("hello world hello")
    assert result == {"hello": 2}


def test_histogram_tied_words_all_included():
    """All words tied at the maximum count are included in the result."""
    result = histogram("a b")
    assert result == {"a": 1, "b": 1}


def test_histogram_inner_loop_skips_below_max():
    """Words whose count is below the maximum are skipped by the inner loop."""
    result = histogram("a a b")
    assert result == {"a": 2}
    assert "b" not in result


def test_histogram_empty_string_returns_empty_dict():
    """An empty input leaves t == 0, so the t > 0 branch is not taken.

    Covers the false branch of the first-loop condition (i == '') and
    the false branch of the 'if t > 0' check.
    """
    result = histogram("")
    assert result == {}


def test_histogram_ignores_empty_tokens():
    """Empty tokens (from consecutive spaces) never update t even though they are frequent.

    Covers the false branch of the first-loop condition when count > t but i == '',
    and the false branch of the inner-loop condition for the empty token.
    """
    result = histogram("  x  ")
    # list1 == ['', '', 'x', '', '']; '' has count 4 but is skipped, so t == 1
    assert result == {"x": 1}
    assert "" not in result
