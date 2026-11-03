# file: project/f111/__init__.py:1-15
# asked: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}

"""Tests for f111.histogram covering all lines and branches."""

from f111 import histogram


def test_histogram_returns_most_frequent_word():
    """Covers lines 3-15: loop, t update (true branch), t>0 (true branch),
    inner loop with both ==t and !=t branches, dict assignment and return."""
    result = histogram("hello world hello")
    assert result == {"hello": 2}


def test_histogram_all_words_tie():
    """Covers the case where every word reaches the max count (line 12 true
    branch for multiple items)."""
    result = histogram("a b c")
    assert result == {"a": 1, "b": 1, "c": 1}


def test_histogram_empty_string():
    """''.split(' ') -> ['']; the i != '' condition is False (line 8 false
    branch) so t stays 0, and the t > 0 branch (line 10) is False."""
    assert histogram("") == {}


def test_histogram_only_spaces():
    """'   '.split(' ') -> ['', '', '']; every element is '' so the
    i != '' guard keeps t at 0 and the empty dict is returned."""
    assert histogram("   ") == {}


def test_histogram_single_word():
    """Single word: first iteration sets t (line 9), inner loop assigns it
    (lines 12-14)."""
    assert histogram("solo") == {"solo": 1}


def test_histogram_mixed_spaces_and_words():
    """Consecutive spaces produce '' entries that must be skipped by the
    i != '' guard, while real words are still counted."""
    result = histogram("cat  dog cat")
    assert result == {"cat": 2}
