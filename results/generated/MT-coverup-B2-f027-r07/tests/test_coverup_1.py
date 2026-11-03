# file: project/f027/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f027 import flip_case


def test_flip_case_basic():
    """Executing line 3: swapcase on a mixed-case string."""
    result = flip_case("Hello, World!")
    assert result == "hELLO, wORLD!"
    assert result == "Hello, World!".swapcase()


def test_flip_case_empty_string():
    """Executing line 3 with an empty string input."""
    assert flip_case("") == ""


def test_flip_case_no_alpha():
    """Executing line 3 with a string containing no letters."""
    assert flip_case("123 !@#") == "123 !@#"


def test_flip_case_all_upper():
    """Executing line 3 with an all-uppercase string."""
    assert flip_case("ABC") == "abc"


def test_flip_case_all_lower():
    """Executing line 3 with an all-lowercase string."""
    assert flip_case("abc") == "ABC"


def test_flip_case_idempotent():
    """Executing line 3 and verifying swapcase is its own inverse."""
    s = "PyThOn 3.12 Is GrEaT!"
    assert flip_case(flip_case(s)) == s
