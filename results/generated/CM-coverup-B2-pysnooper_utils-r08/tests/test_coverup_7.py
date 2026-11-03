# file: project/pysnooper/utils.py:44-47
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

"""Tests for pysnooper.utils.shitcode, covering both branches of the
conditional expression on lines 45-46."""

import pytest

from pysnooper.utils import shitcode


def test_shitcode_keeps_ascii_characters():
    """Characters with 0 < ord(c) < 256 must be preserved unchanged."""
    result = shitcode('hello world!123')
    assert result == 'hello world!123'
    # Latin-1 high range (e.g. 'é' == chr(233)) is still < 256, so kept.
    assert shitcode('café') == 'café'


def test_shitcode_replaces_high_codepoints_with_question_mark():
    """Characters with ord(c) >= 256 must be replaced by '?'."""
    result = shitcode('a\u4f60b')  # '\u4f60' has ord 20320
    assert result == 'a?b'
    assert shitcode('\U0001f600') == '?'  # emoji, ord > 255


def test_shitcode_replaces_null_character():
    """A null character (ord == 0) fails the 0 < ord(c) check -> '?'."""
    assert shitcode('\x00') == '?'


def test_shitcode_mixed_string():
    """Mixed input exercises both branches in a single call."""
    result = shitcode('a\x00é中z')
    assert result == 'a?é?z'


def test_shitcode_empty_string():
    """Empty input yields empty output (generator produces nothing)."""
    assert shitcode('') == ''


def test_shitcode_returns_str_and_is_pure():
    """Postcondition: result is str; calling again gives same output."""
    source = 'ok\u2603'  # snowman has ord 9733
    first = shitcode(source)
    second = shitcode(source)
    assert isinstance(first, str)
    assert first == 'ok?'
    assert first == second
    # Purity check: original argument untouched.
    assert source == 'ok\u2603'
