# file: project/f023/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

import pytest

from f023 import strlen


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("", 0),
        ("hello", 5),
        ("é", 1),
    ],
)
def test_strlen_returns_string_length(value, expected):
    assert strlen(value) == expected
