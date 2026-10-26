# file: project/pysnooper/utils.py:44-47
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

import pytest

from pysnooper.utils import shitcode


def test_shitcode_keeps_latin1_characters():
    # Characters with 0 < ord(c) < 256 are kept as-is (true branch).
    s = 'abcXYZ_19!'
    result = shitcode(s)
    assert result == s


def test_shitcode_replaces_non_latin1_characters():
    # Characters with ord(c) >= 256 are replaced by '?' (false branch).
    # Note: 'é' has ord 233 < 256, so it is kept; '☃' (ord 9731) is replaced.
    s = 'aé☃b'
    result = shitcode(s)
    assert result == 'aé?b'


def test_shitcode_replaces_null_character():
    # ord(c) == 0 fails the 0 < ord(c) condition, so it is replaced too.
    result = shitcode('a\x00b')
    assert result == 'a?b'


def test_shitcode_empty_string():
    assert shitcode('') == ''


def test_shitcode_mixed():
    s = 'héllo wörld ☃ \x00'
    result = shitcode(s)
    assert result == 'héllo wörld ? ?'
    assert all(0 < ord(c) < 256 for c in result)
