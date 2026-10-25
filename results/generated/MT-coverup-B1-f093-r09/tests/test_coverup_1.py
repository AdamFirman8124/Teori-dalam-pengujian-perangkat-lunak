# file: project/f093/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": []}
# gained: {"lines": [3, 4, 5, 6], "branches": []}

import pytest

from f093 import encode


def test_encode_swaps_case_and_shifts_vowels():
    assert encode("hello WORLD") == "HGLLQ wqrld"


def test_encode_all_vowels_both_cases():
    assert encode("aeiouAEIOU") == "CGKQWcgkqw"


def test_encode_non_letters_unchanged():
    assert encode("xyz 123 !?") == "XYZ 123 !?"


def test_encode_empty_string():
    assert encode("") == ""
