# file: project/f027/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f027 import flip_case


def test_flip_case_basic():
    assert flip_case("Hello, World!") == "hELLO, wORLD!"


def test_flip_case_empty_string():
    assert flip_case("") == ""


def test_flip_case_mixed():
    assert flip_case("PyThOn 123 !@#") == "pYtHoN 123 !@#"


def test_flip_case_all_upper():
    assert flip_case("ABC") == "abc"


def test_flip_case_all_lower():
    assert flip_case("xyz") == "XYZ"


def test_flip_case_unicode():
    assert flip_case("Ünïcödé") == "üNÏCÖDÉ"


def test_flip_case_returns_new_string():
    original = "abc"
    result = flip_case(original)
    assert result == "ABC"
    assert original == "abc"  # input unchanged
    assert result is not original
