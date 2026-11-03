# file: project/f111/__init__.py:1-15
# asked: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}

"""Tests for f111.histogram covering all previously unexecuted lines/branches."""

from f111 import histogram


def test_histogram_returns_most_frequent_word_and_count():
    # Covers: dict init, split, loop, count>t True/False, i!='' True,
    # t>0 True, count==t True/False, dict assignment, return.
    result = histogram("apple banana apple")
    assert result == {"apple": 2}


def test_histogram_handles_ties():
    # Multiple words share the max count; both must be recorded.
    result = histogram("cat dog cat dog")
    assert result == {"cat": 2, "dog": 2}


def test_histogram_empty_string_returns_empty_dict():
    # "".split(" ") -> ['']; the i != '' guard keeps t at 0,
    # exercising the False branch of `if t > 0`.
    assert histogram("") == {}


def test_histogram_only_spaces_returns_empty_dict():
    # "   ".split(" ") -> ['', '', '']; every token is '' so t stays 0.
    assert histogram("   ") == {}


def test_histogram_skips_empty_tokens_when_computing_max():
    # "a  b".split(" ") -> ['a', '', 'b']: the '' token has count 1 > t=0
    # but is rejected by i != '' (False branch); 'a' then sets t=1.
    # NOTE: the second loop does NOT filter '', so '' ends up in the result.
    result = histogram("a  b")
    assert result == {"a": 1, "": 1, "b": 1}


def test_histogram_single_word():
    result = histogram("hello")
    assert result == {"hello": 1}
