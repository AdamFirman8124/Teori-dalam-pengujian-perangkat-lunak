# file: project/f016/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f016 import count_distinct_characters


def test_count_distinct_characters_mixed_case():
    """Distinct characters are counted case-insensitively."""
    assert count_distinct_characters("xyzXYZ") == 3


def test_count_distinct_characters_empty_string():
    """An empty string has zero distinct characters."""
    assert count_distinct_characters("") == 0


def test_count_distinct_characters_repeated_chars():
    """Repeated characters (any case) count only once."""
    assert count_distinct_characters("Jerry") == 4
    assert count_distinct_characters("aAaA") == 1


def test_count_distinct_characters_all_unique():
    """All unique characters are counted."""
    assert count_distinct_characters("abcdef") == 6
