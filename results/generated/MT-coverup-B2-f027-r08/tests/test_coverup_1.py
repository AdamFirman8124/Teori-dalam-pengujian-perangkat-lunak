# file: project/f027/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f027 import flip_case


def test_flip_case_lowercase():
    assert flip_case("hello") == "HELLO"


def test_flip_case_uppercase():
    assert flip_case("HELLO") == "hello"


def test_flip_case_mixed():
    assert flip_case("Hello World") == "hELLO wORLD"


def test_flip_case_empty_and_nonalpha():
    assert flip_case("") == ""
    assert flip_case("123!@#") == "123!@#"
    assert flip_case("aBc123XyZ") == "AbC123xYz"
