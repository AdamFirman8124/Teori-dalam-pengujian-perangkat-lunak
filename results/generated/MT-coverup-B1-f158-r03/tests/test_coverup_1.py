# file: project/f158/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f158 import find_max


def test_find_max_unique_chars_tie_broken_lexicographically():
    # "apple": {a, p, l, e} = 4 unique; "apply": {a, p, l, y} = 4 unique
    # Tie broken lexicographically: "apple" < "apply"
    assert find_max(["apply", "apple", "cat"]) == "apple"


def test_find_max_picks_most_unique_chars():
    # "name" = 4 unique, "of" = 2 unique, "string" = 6 unique
    assert find_max(["name", "of", "string"]) == "string"


def test_find_max_single_element():
    assert find_max(["hello"]) == "hello"


def test_find_max_duplicates_reduced_by_set():
    # "aabb": {a, b} = 2 unique; "ab": {a, b} = 2 unique
    # Tie broken lexicographically: "aabb" < "ab"
    assert find_max(["ab", "aabb"]) == "aabb"
