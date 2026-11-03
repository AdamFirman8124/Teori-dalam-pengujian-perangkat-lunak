# file: project/f027/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f027 import flip_case


def test_flip_case_basic():
    assert flip_case("Hello, World!") == "hELLO, wORLD!"


def test_flip_case_empty():
    assert flip_case("") == ""


def test_flip_case_all_lower():
    assert flip_case("abc") == "ABC"


def test_flip_case_all_upper():
    assert flip_case("ABC") == "abc"


def test_flip_case_mixed_and_symbols():
    assert flip_case("PyThOn 123 !@#") == "pYtHoN 123 !@#"


def test_flip_case_unicode():
    assert flip_case("ñÁç") == "ÑáÇ"


def test_flip_case_involution():
    s = "MiXeD CaSe 123"
    assert flip_case(flip_case(s)) == s
