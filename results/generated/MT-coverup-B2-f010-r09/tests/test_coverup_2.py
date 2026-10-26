# file: project/f010/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f010 import is_palindrome


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("racecar", True),
        ("python", False),
        ("", True),
    ],
)
def test_is_palindrome_returns_expected_result(value, expected):
    assert is_palindrome(value) is expected
