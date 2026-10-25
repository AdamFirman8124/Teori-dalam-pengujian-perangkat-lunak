# file: project/pysnooper/utils.py:44-47
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

import pytest

from pysnooper.utils import shitcode


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("ASCII", "ASCII"),
        ("\x01", "\x01"),
        ("\x00", "?"),
        ("\u0100", "?"),
        ("A\x00\u0100B", "A??B"),
    ],
)
def test_shitcode_replaces_characters_outside_byte_range(value, expected):
    assert shitcode(value) == expected
