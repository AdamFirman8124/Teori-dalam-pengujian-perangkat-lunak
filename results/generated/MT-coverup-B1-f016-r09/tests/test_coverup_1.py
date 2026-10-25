# file: project/f016/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f016 import count_distinct_characters


def test_count_distinct_characters_basic():
    # Exercises line 3: the return statement.
    assert count_distinct_characters("abcde") == 5


def test_count_distinct_characters_case_insensitive():
    # Verifies the .lower() branch: mixed case collapses to distinct lowercase chars.
    assert count_distinct_characters("abcdeAaBb") == 5


def test_count_distinct_characters_duplicates_and_empty():
    assert count_distinct_characters("xyzXYZ   ") == 4  # x, y, z, space
    assert count_distinct_characters("") == 0
    assert count_distinct_characters("aA") == 1
