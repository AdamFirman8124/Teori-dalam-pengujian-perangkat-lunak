# file: project/pysnooper/utils.py:44-47
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

from pysnooper.utils import shitcode


def test_shitcode_replaces_characters_outside_byte_range():
    value = chr(0) + chr(1) + "A" + chr(255) + chr(256) + "\U0001f600"

    result = shitcode(value)

    assert result == "?" + chr(1) + "A" + chr(255) + "??"
