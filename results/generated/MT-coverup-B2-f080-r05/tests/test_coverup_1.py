# file: project/f080/__init__.py:1-10
# asked: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}

import pytest

from f080 import is_happy


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("", False),
        ("ab", False),
        ("aab", False),
        ("abb", False),
        ("aba", False),
        ("abc", True),
        ("abcd", True),
        ("abca", True),
        ("abcc", False),
    ],
)
def test_is_happy(value, expected):
    assert is_happy(value) is expected
