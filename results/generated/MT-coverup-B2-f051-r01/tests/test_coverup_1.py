# file: project/f051/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f051 import remove_vowels


def test_remove_vowels_removes_all_vowels():
    result = remove_vowels("Hello World")
    assert result == "Hll Wrld"


def test_remove_vowels_handles_case_insensitivity():
    assert remove_vowels("AEIOUaeiou") == ""


def test_remove_vowels_keeps_non_vowels():
    assert remove_vowels("rhythm") == "rhythm"


def test_remove_vowels_empty_string():
    assert remove_vowels("") == ""
