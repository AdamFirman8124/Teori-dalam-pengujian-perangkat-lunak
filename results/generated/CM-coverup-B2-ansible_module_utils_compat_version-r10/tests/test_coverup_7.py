# file: project/ansible/module_utils/compat/version.py:306-308
# asked: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}
# gained: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_init_with_vstring_parses():
    """Covers lines 307-308: truthy vstring triggers self.parse(vstring)."""
    lv = LooseVersion('1.5.2b2')
    assert lv.vstring == '1.5.2b2'
    assert lv.version == [1, 5, 2, 'b', 2]


def test_loose_version_init_with_empty_string_does_not_parse():
    """Covers line 307 branch: empty string is falsy, parse is not called."""
    lv = LooseVersion('')
    assert not hasattr(lv, 'vstring')
    assert not hasattr(lv, 'version')


def test_loose_version_init_default_none_does_not_parse():
    """Covers line 307 branch: default vstring=None is falsy, parse is not called."""
    lv = LooseVersion()
    assert not hasattr(lv, 'vstring')
    assert not hasattr(lv, 'version')


def test_loose_version_init_calls_parse(monkeypatch):
    """Verifies line 308 executes by confirming parse is invoked with vstring."""
    calls = {}

    def fake_parse(self, vstring):
        calls['vstring'] = vstring

    monkeypatch.setattr(LooseVersion, 'parse', fake_parse)
    LooseVersion('3.4j')
    assert calls == {'vstring': '3.4j'}
