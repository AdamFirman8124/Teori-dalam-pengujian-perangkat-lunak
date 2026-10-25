# file: project/ansible/module_utils/compat/version.py:306-308
# asked: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}
# gained: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_init_with_vstring():
    """Covers lines 307-308: truthy vstring triggers parse()."""
    lv = LooseVersion('1.5.2b2')
    assert lv.vstring == '1.5.2b2'
    assert lv.version == [1, 5, 2, 'b', 2]


def test_loose_version_init_with_empty_string():
    """Covers the falsy branch of line 307: empty string does not parse."""
    lv = LooseVersion('')
    assert not hasattr(lv, 'vstring')
    assert not hasattr(lv, 'version')


def test_loose_version_init_default_none():
    """Covers the falsy branch of line 307: default None does not parse."""
    lv = LooseVersion()
    assert not hasattr(lv, 'vstring')
    assert not hasattr(lv, 'version')


def test_loose_version_init_parse_called(monkeypatch):
    """Verifies parse() is actually invoked for a truthy vstring."""
    called = []

    def fake_parse(self, vstring):
        called.append(vstring)
        self.vstring = vstring
        self.version = ['parsed']

    monkeypatch.setattr(LooseVersion, 'parse', fake_parse)
    lv = LooseVersion('2.0')
    assert called == ['2.0']
    assert lv.vstring == '2.0'
    assert lv.version == ['parsed']


def test_loose_version_init_parse_not_called(monkeypatch):
    """Verifies parse() is not invoked for a falsy vstring."""
    called = []

    def fake_parse(self, vstring):
        called.append(vstring)

    monkeypatch.setattr(LooseVersion, 'parse', fake_parse)
    lv = LooseVersion(None)
    assert called == []
    assert not hasattr(lv, 'vstring')
