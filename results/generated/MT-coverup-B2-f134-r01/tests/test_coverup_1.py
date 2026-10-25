# file: project/f134/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f134 import check_if_last_char_is_a_letter


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello a", True),
        ("Hello Z", True),
        ("Hello ab", False),
        ("Hello 1", False),
        ("Hello", False),
        ("Hello ", False),
    ],
)
def test_check_if_last_char_is_a_letter(text, expected):
    assert check_if_last_char_is_a_letter(text) is expected
