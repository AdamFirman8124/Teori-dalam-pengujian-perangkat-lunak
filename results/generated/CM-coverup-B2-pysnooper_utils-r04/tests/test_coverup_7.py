# file: project/pysnooper/utils.py:44-47
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

import pytest

from pysnooper.utils import shitcode


def test_shitcode_keeps_ascii_characters():
    """Characters with 0 < ord(c) < 256 are kept unchanged (true branch)."""
    result = shitcode('abcXYZ_019 !?')
    assert result == 'abcXYZ_019 !?'


def test_shitcode_replaces_high_codepoints():
    """Characters with ord(c) >= 256 are replaced with '?' (false branch)."""
    result = shitcode('a€b中c')
    assert result == 'a?b?c'


def test_shitcode_replaces_null_character():
    """The null character (ord == 0) fails 0 < ord(c) and becomes '?'."""
    result = shitcode('a\x00b')
    assert result == 'a?b'


def test_shitcode_boundaries():
    """Check the exact boundaries of the 0 < ord(c) < 256 condition."""
    # chr(1) and chr(255) are inside the range and kept.
    assert shitcode(chr(1) + chr(255)) == chr(1) + chr(255)
    # chr(0) and chr(256) are outside the range and replaced.
    assert shitcode(chr(0) + chr(256)) == '??'


def test_shitcode_latin1_characters_kept():
    """Latin-1 accented characters (ord < 256) are preserved."""
    assert shitcode('héllo wörld') == 'héllo wörld'


def test_shitcode_empty_string():
    """The empty string yields the empty string."""
    assert shitcode('') == ''


def test_shitcode_mixed_content():
    """A mix of kept and replaced characters in one string."""
    result = shitcode('a\x00b€cÿ')
    assert result == 'a?b?cÿ'
