# file: project/f016/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f016 import count_distinct_characters


def test_count_distinct_characters_basic():
    """Distinct characters in a simple string."""
    assert count_distinct_characters("abc") == 3


def test_count_distinct_characters_case_insensitive():
    """Uppercase and lowercase letters count as the same character."""
    assert count_distinct_characters("aAbB") == 2


def test_count_distinct_characters_repeated():
    """Repeated characters (in mixed case) are counted once."""
    assert count_distinct_characters("xyzXYZ") == 3


def test_count_distinct_characters_empty_string():
    """An empty string has zero distinct characters."""
    assert count_distinct_characters("") == 0


def test_count_distinct_characters_single_char():
    """A single-character string has exactly one distinct character."""
    assert count_distinct_characters("a") == 1


def test_count_distinct_characters_mixed_content():
    """Non-letter characters are handled and lowercased too."""
    # 'Hello, World!' lowercased -> 'hello, world!'
    # distinct: h, e, l, o, ',', ' ', w, r, d, '!' -> 10
    assert count_distinct_characters("Hello, World!") == 10
