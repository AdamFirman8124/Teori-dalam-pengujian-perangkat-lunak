# file: project/f134/__init__.py:1-4
# asked: {"lines": [3, 4], "branches": []}
# gained: {"lines": [3, 4], "branches": []}

import pytest

from f134 import check_if_last_char_is_a_letter


@pytest.mark.parametrize(
    "txt, expected",
    [
        # True branch: last word is a single lowercase letter
        ("apple pie a", True),
        # True branch: last word is a single uppercase letter (lower() maps into range)
        ("apple pie A", True),
        # True branch: whole string is a single letter
        ("z", True),
        # False branch: last word has length > 1 (short-circuits before ord check)
        ("apple pie", False),
        # False branch: last word is a single char but not a lowercase letter (digit)
        ("apple pie 1", False),
        # False branch: single char, non-letter (punctuation)
        ("!", False),
        # False branch: empty string -> split yields [''], len 0
        ("", False),
        # False branch: trailing space -> last token is empty string
        ("apple pie ", False),
        # False branch: only spaces -> last token is empty string
        ("   ", False),
    ],
)
def test_check_if_last_char_is_a_letter(txt, expected):
    result = check_if_last_char_is_a_letter(txt)
    assert result is expected
