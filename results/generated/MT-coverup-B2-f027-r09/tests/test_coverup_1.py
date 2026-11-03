# file: project/f027/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f027 import flip_case


def test_flip_case_basic():
    """flip_case should swap upper- and lower-case characters."""
    assert flip_case("Hello, World!") == "hELLO, wORLD!"


def test_flip_case_empty_string():
    """An empty string should remain empty."""
    assert flip_case("") == ""


def test_flip_case_no_alpha_characters():
    """Strings without letters should be unchanged."""
    assert flip_case("123 !@#") == "123 !@#"


def test_flip_case_returns_new_string():
    """flip_case should return a new string, not mutate the input."""
    original = "PyThOn"
    result = flip_case(original)
    assert original == "PyThOn"
    assert result == "pYtHoN"
    assert result is not original
