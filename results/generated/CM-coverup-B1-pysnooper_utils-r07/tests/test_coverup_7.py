# file: project/pysnooper/utils.py:44-47
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

import pytest

from pysnooper.utils import shitcode


def test_shitcode_mixed_characters():
    """Covers both branches: latin-1 chars kept, others replaced with '?'."""
    s = 'abcé' + '\u4e2d\u6587' + '\x00' + 'xyz'
    result = shitcode(s)
    # 'abcé' and 'xyz' have 0 < ord(c) < 256 -> kept as-is
    # '\u4e2d', '\u6587' have ord > 255 -> replaced with '?'
    # '\x00' has ord == 0 -> replaced with '?'
    assert result == 'abcé???xyz'
    assert len(result) == len(s)


def test_shitcode_empty_string():
    assert shitcode('') == ''


def test_shitcode_all_replaced():
    assert shitcode('\u4e2d\u6587') == '??'
    assert shitcode('\x00') == '?'


def test_shitcode_boundaries():
    # ord == 1 (smallest valid) and ord == 255 (largest valid) are kept
    assert shitcode(chr(1) + chr(255)) == chr(1) + chr(255)
    # ord == 0 and ord == 256 are replaced
    assert shitcode(chr(0) + chr(256)) == '??'
