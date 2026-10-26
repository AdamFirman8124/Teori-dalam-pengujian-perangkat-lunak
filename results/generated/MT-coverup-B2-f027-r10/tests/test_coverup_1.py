# file: project/f027/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f027 import flip_case


def test_flip_case():
    assert flip_case("hello") == "HELLO"
    assert flip_case("HELLO") == "hello"
    assert flip_case("Hello World") == "hELLO wORLD"
    assert flip_case("") == ""
    assert flip_case("123!@#") == "123!@#"
    assert flip_case("PyThOn") == "pYtHoN"
