# file: project/f027/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f027 import flip_case


def test_flip_case_mixed_case():
    """Executing line 3: swapcase flips upper to lower and vice versa."""
    assert flip_case("Hello World") == "hELLO wORLD"


def test_flip_case_empty_string():
    """Edge case: empty string returns empty string."""
    assert flip_case("") == ""


def test_flip_case_non_alpha_unchanged():
    """Digits and punctuation are unaffected by swapcase."""
    assert flip_case("PyThOn 123!@#") == "pYtHoN 123!@#"


def test_flip_case_all_upper():
    """All-uppercase input becomes all-lowercase."""
    assert flip_case("ABCDEF") == "abcdef"


def test_flip_case_all_lower():
    """All-lowercase input becomes all-uppercase."""
    assert flip_case("abcdef") == "ABCDEF"


def test_flip_case_returns_new_string():
    """Postcondition: result is a str and a new object (strings are immutable)."""
    original = "AbC"
    result = flip_case(original)
    assert isinstance(result, str)
    assert result == "aBc"
    assert original == "AbC"  # input unchanged
