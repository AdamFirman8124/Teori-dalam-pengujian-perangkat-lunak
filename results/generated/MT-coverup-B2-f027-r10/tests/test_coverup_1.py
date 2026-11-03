# file: project/f027/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f027 import flip_case


def test_flip_case_lower_to_upper():
    assert flip_case("hello") == "HELLO"


def test_flip_case_upper_to_lower():
    assert flip_case("WORLD") == "world"


def test_flip_case_mixed():
    assert flip_case("Hello World") == "hELLO wORLD"


def test_flip_case_empty_string():
    assert flip_case("") == ""


def test_flip_case_non_alpha_unchanged():
    assert flip_case("123 !@# \t\n") == "123 !@# \t\n"


def test_flip_case_unicode():
    assert flip_case("ñÁÑé") == "ÑáñÉ"


@pytest.mark.parametrize(
    "value",
    ["abc", "ABC", "AbC", "", "a1! b2?", "MiXeD CaSe 123", "ñÁÑé"],
)
def test_flip_case_is_involution(value):
    # swapcase applied twice returns the original string
    assert flip_case(flip_case(value)) == value
