# file: project/pysnooper/utils.py:44-47
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

from pysnooper.utils import shitcode


def test_shitcode_replaces_characters_outside_one_byte_range():
    assert shitcode("A\xff\x00\u0100") == "A\xff??"
