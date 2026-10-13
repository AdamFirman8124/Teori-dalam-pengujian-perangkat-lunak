# file: script_10.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from script_10 import is_palindrome


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("racecar", True),
        ("python", False),
        ("", True),
        ("Aba", False),
    ],
)
def test_is_palindrome(value, expected):
    assert is_palindrome(value) is expected
