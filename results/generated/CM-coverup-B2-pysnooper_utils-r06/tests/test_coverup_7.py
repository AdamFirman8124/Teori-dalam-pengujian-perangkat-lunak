# file: project/pysnooper/utils.py:44-47
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

from pysnooper.utils import shitcode


def test_shitcode_preserves_latin1_characters():
    assert shitcode("Aéÿ") == "Aéÿ"


def test_shitcode_replaces_out_of_range_characters():
    assert shitcode("\x00\u0100😀") == "???"
