# file: project/ansible/module_utils/compat/version.py:306-308
# asked: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}
# gained: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_init_with_vstring_parses():
    """Constructing with a non-empty vstring must execute lines 307-308
    (the ``if vstring: self.parse(vstring)`` branch) and populate the
    version attribute."""
    version = LooseVersion("1.5.1")
    assert version.version == [1, 5, 1]
    assert str(version) == "1.5.1"


def test_loose_version_init_with_alphanumeric_vstring_parses():
    """A vstring with alphabetic components also goes through parse()."""
    version = LooseVersion("2.2beta29")
    assert version.version == [2, 2, "beta", 29]
    assert str(version) == "2.2beta29"


def test_loose_version_init_without_vstring_leaves_version_unset():
    """The falsy branch (vstring=None) must not call parse(), so no
    version attribute is set."""
    version = LooseVersion()
    assert not hasattr(version, "version")


def test_loose_version_init_with_empty_string_does_not_parse(monkeypatch):
    """An empty string is falsy, so parse() must not be invoked."""
    called = []

    def fake_parse(self, vstring):
        called.append(vstring)

    monkeypatch.setattr(LooseVersion, "parse", fake_parse)
    version = LooseVersion("")
    assert called == []
    assert not hasattr(version, "version")
