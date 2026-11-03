# file: project/f111/__init__.py:1-15
# asked: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}
# gained: {"lines": [3, 4, 5, 7, 8, 9, 10, 11, 12, 14, 15], "branches": [[7, 8], [7, 10], [8, 7], [8, 9], [10, 11], [10, 15], [11, 12], [11, 15], [12, 11], [12, 14]]}

from f111 import histogram


def test_histogram_most_common_word():
    """Covers lines 3-15: initialisation, the counting loop with both
    outcomes of the ``count > t and i != ''`` test, the ``t > 0`` branch,
    both outcomes of the equality test, the dict assignment and the return.
    """
    assert histogram("a b b") == {"b": 2}


def test_histogram_empty_tokens_are_ignored():
    """Empty tokens (produced by consecutive spaces) never raise ``t``
    because of the ``i != ''`` guard, but a real word still sets ``t > 0``
    and is reported.
    """
    assert histogram("  a") == {"a": 1}


def test_histogram_only_spaces_yields_empty_dict():
    """With nothing but empty tokens ``t`` stays 0, so the ``t > 0`` branch
    is skipped and an empty dict is returned.
    """
    assert histogram(" ") == {}
    assert histogram("") == {}


def test_histogram_all_words_tied():
    """When every word occurs exactly once, all words are reported with
    count 1.
    """
    assert histogram("a b c") == {"a": 1, "b": 1, "c": 1}


def test_histogram_single_word():
    """A single word maps to itself with count 1."""
    assert histogram("hello") == {"hello": 1}
