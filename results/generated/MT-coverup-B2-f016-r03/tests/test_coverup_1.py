# file: project/f016/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f016 import count_distinct_characters


def test_count_distinct_characters_mixed_case():
    # Exercises line 3: the return statement, including the .lower() branch.
    assert count_distinct_characters("xyzXYZ") == 3
    assert count_distinct_characters("Jerry") == 4


def test_count_distinct_characters_empty_string():
    # Covers the edge case where set() is empty.
    assert count_distinct_characters("") == 0


def test_count_distinct_characters_repeated_characters():
    # Duplicates collapse in the set; case-insensitivity is verified.
    assert count_distinct_characters("aAaA") == 1
    assert count_distinct_characters("Hello, World!") == 10
