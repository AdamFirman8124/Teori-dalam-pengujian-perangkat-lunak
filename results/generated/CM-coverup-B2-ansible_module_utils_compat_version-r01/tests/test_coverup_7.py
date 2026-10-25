# file: project/ansible/module_utils/compat/version.py:306-308
# asked: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}
# gained: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_init_with_vstring_calls_parse(monkeypatch):
    """Lines 307-308: a truthy vstring must be passed to parse()."""
    calls = []
    original_parse = LooseVersion.parse

    def spy_parse(self, vstring):
        calls.append(vstring)
        return original_parse(self, vstring)

    monkeypatch.setattr(LooseVersion, "parse", spy_parse)

    version = LooseVersion("1.2.3")

    assert calls == ["1.2.3"]
    assert version.version == [1, 2, 3]
    assert str(version) == "1.2.3"


def test_loose_version_init_without_vstring_skips_parse(monkeypatch):
    """Branch 307->exit: falsy vstring must not call parse()."""
    calls = []

    def fail_parse(self, vstring):
        calls.append(vstring)
        raise AssertionError("parse() should not be called for falsy vstring")

    monkeypatch.setattr(LooseVersion, "parse", fail_parse)

    for falsy in (None, "", 0):
        version = LooseVersion(falsy)
        assert not hasattr(version, "version")

    assert calls == []


def test_loose_version_init_parses_real_vstring():
    """Postcondition check on the real (unpatched) implementation."""
    version = LooseVersion("1.5.2b2")

    assert version.version == [1, 5, 2, "b", 2]
    assert str(version) == "1.5.2b2"
    assert repr(version) == "LooseVersion ('1.5.2b2')"
    assert LooseVersion("1.5.2b2") == LooseVersion("1.5.2b2")
    assert LooseVersion("1.5.2b2") < LooseVersion("1.5.2b3")
