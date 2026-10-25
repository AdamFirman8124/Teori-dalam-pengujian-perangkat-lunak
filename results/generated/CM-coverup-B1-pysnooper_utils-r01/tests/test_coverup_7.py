# file: project/pysnooper/utils.py:44-47
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

import pytest

from pysnooper.utils import shitcode


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("\x01A\xff", "\x01A\xff"),
        ("\x00\u0100", "??"),
    ],
)
def test_shitcode_replaces_characters_outside_byte_range(value, expected):
    assert shitcode(value) == expected
