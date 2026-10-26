# file: project/ansible/module_utils/compat/version.py:310-322
# asked: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}
# gained: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_parse_numeric_components():
    """Covers lines 314, 315, 316-318 (int conversion succeeds) and 322."""
    lv = LooseVersion('1.5.1')
    assert lv.vstring == '1.5.1'
    assert lv.version == [1, 5, 1]
    assert all(isinstance(c, int) for c in lv.version)


def test_loose_version_parse_mixed_components():
    """Covers lines 319-320 (ValueError branch: non-numeric component kept as str)."""
    lv = LooseVersion('2.2beta29')
    assert lv.vstring == '2.2beta29'
    assert lv.version == [2, 2, 'beta', 29]
    assert isinstance(lv.version[2], str)
    assert isinstance(lv.version[3], int)


def test_loose_version_parse_dots_filtered():
    """Line 315: '.' components are filtered out of the split result."""
    lv = LooseVersion('3.4j')
    assert lv.version == [3, 4, 'j']
    assert '.' not in lv.version


def test_loose_version_parse_empty_string():
    """parse('') yields an empty component list (no components to convert)."""
    lv = LooseVersion()
    lv.parse('')
    assert lv.vstring == ''
    assert lv.version == []


def test_loose_version_str_roundtrip():
    """__str__ uses vstring stored by parse (line 314 postcondition)."""
    vstring = '1.13++'
    lv = LooseVersion(vstring)
    assert str(lv) == vstring
