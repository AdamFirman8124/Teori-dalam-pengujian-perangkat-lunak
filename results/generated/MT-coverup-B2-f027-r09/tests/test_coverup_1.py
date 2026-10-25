# file: project/f027/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f027 import flip_case


def test_flip_case_swaps_case():
    assert flip_case("Hello World") == "hELLO wORLD"


def test_flip_case_empty_string():
    assert flip_case("") == ""


def test_flip_case_non_alpha_unchanged():
    assert flip_case("aBc123!@#") == "AbC123!@#"
