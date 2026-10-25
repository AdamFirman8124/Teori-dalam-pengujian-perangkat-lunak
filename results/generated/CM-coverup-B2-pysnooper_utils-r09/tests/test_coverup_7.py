# file: project/pysnooper/utils.py:44-47
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

import pytest

from pysnooper.utils import shitcode


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("abc\x01\xff", "abc\x01\xff"),
        ("\x00\u0100\U0001f600", "???"),
        ("a\x00\xff\u0100z", "a?\xff?z"),
        ("", ""),
    ],
)
def test_shitcode_replaces_characters_outside_supported_range(value, expected):
    assert shitcode(value) == expected
