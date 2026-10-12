# file: script_16.py:1-8
# asked: {"lines": [8], "branches": []}
# gained: {"lines": [8], "branches": []}

import pytest
from script_16 import count_distinct_characters


def test_count_distinct_characters_mixed_case():
    assert count_distinct_characters('xyzXYZ') == 3


def test_count_distinct_characters_with_repeats():
    assert count_distinct_characters('Jerry') == 4


def test_count_distinct_characters_empty_string():
    assert count_distinct_characters('') == 0


def test_count_distinct_characters_single_character():
    assert count_distinct_characters('a') == 1


def test_count_distinct_characters_all_same():
    assert count_distinct_characters('aaaa') == 1


def test_count_distinct_characters_all_same_mixed_case():
    assert count_distinct_characters('AaAa') == 1


def test_count_distinct_characters_all_unique():
    assert count_distinct_characters('abcdef') == 6


def test_count_distinct_characters_with_spaces():
    assert count_distinct_characters('a b c') == 4


def test_count_distinct_characters_with_numbers():
    assert count_distinct_characters('abc123') == 6


def test_count_distinct_characters_with_special_chars():
    assert count_distinct_characters('a!b@c#') == 6
