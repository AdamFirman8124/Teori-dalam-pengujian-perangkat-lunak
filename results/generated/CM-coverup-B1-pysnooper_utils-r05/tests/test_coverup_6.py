# file: project/pysnooper/utils.py:44-47
# asked: {"lines": [45, 46], "branches": []}
# gained: {"lines": [45, 46], "branches": []}

import pytest

from pysnooper.utils import shitcode


def test_shitcode_mixed_characters():
    s = 'abcé' + '\u4e2d\u6587' + '\x00' + 'xyz'
    result = shitcode(s)
    assert result == 'abcé???xyz'
    assert len(result) == len(s)


def test_shitcode_empty_string():
    assert shitcode('') == ''


def test_shitcode_all_replaced():
    assert shitcode('\u4e2d\u6587') == '??'
    assert shitcode('\x00') == '?'


def test_shitcode_boundaries():
    assert shitcode(chr(1) + chr(255)) == chr(1) + chr(255)
    assert shitcode(chr(0) + chr(256)) == '??'
