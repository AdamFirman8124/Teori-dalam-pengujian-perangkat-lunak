# file: project/f089/__init__.py:1-10
# asked: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

from f089 import encrypt


def test_encrypt_lowercase_shift():
    assert encrypt("abc") == "efg"
    assert encrypt("hello") == "lipps"


def test_encrypt_wrap_around():
    assert encrypt("wxyz") == "abcd"
    assert encrypt("z") == "d"
    assert encrypt("xyz") == "bcd"


def test_encrypt_preserves_non_lowercase():
    assert encrypt("ABC XYZ 123!?, ") == "ABC XYZ 123!?, "
    assert encrypt("Hello, World! 123") == "Hipps, Wsvph! 123"


def test_encrypt_empty_string():
    assert encrypt("") == ""
