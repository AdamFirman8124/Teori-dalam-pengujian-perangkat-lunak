# file: project/f016/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f016 import count_distinct_characters


def test_count_distinct_characters_basic():
    """Execute line 3 and verify correct distinct-character counts."""
    # Mixed case: 'A' and 'a' collapse to one distinct character.
    assert count_distinct_characters("AaBb") == 2
    # All distinct characters.
    assert count_distinct_characters("abcdef") == 6
    # Repeated characters collapse.
    assert count_distinct_characters("aaaa") == 1
    # Empty string has zero distinct characters.
    assert count_distinct_characters("") == 0
    # Digits and punctuation are counted too.
    assert count_distinct_characters("a1!a1!") == 3
    # Spaces count as characters.
    assert count_distinct_characters("a b c") == 4
