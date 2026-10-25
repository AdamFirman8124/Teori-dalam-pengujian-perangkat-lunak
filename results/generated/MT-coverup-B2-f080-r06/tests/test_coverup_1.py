# file: project/f080/__init__.py:1-10
# asked: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}
# gained: {"lines": [3, 4, 6, 8, 9, 10], "branches": [[3, 4], [3, 6], [6, 8], [6, 10], [8, 6], [8, 9]]}

import pytest

from f080 import is_happy


@pytest.mark.parametrize("value", ["", "a", "ab"])
def test_is_happy_rejects_values_shorter_than_three(value):
    assert is_happy(value) is False


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("aab", False),
        ("abb", False),
        ("aba", False),
        ("abcc", False),
        ("abc", True),
        ("abcdef", True),
    ],
)
def test_is_happy_checks_every_three_item_window(value, expected):
    assert is_happy(value) is expected
