# file: project/ansible/module_utils/compat/version.py:306-308
# asked: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}
# gained: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}

import pytest

from ansible.module_utils.compat.version import LooseVersion


@pytest.fixture
def parse_spy(monkeypatch):
    """Record calls to LooseVersion.parse without changing its behavior."""
    calls = []
    original_parse = LooseVersion.parse

    def spy(self, vstring):
        calls.append(vstring)
        return original_parse(self, vstring)

    monkeypatch.setattr(LooseVersion, "parse", spy)
    return calls


def test_loose_version_with_vstring_calls_parse(parse_spy):
    """Lines 307-308: a truthy vstring must be parsed during construction."""
    version = LooseVersion("1.2.3")

    assert parse_spy == ["1.2.3"]
    assert version.vstring == "1.2.3"
    assert version.version == [1, 2, 3]
    assert str(version) == "1.2.3"
    assert version == LooseVersion("1.2.3")
    assert version > LooseVersion("1.2.2")


def test_loose_version_without_vstring_skips_parse(parse_spy):
    """Branch 307->exit: no vstring means parse is never called."""
    version = LooseVersion()

    assert parse_spy == []
    assert not hasattr(version, "version")
    assert not hasattr(version, "vstring")


def test_loose_version_with_empty_vstring_skips_parse(parse_spy):
    """Branch 307->exit: an empty (falsy) vstring must not be parsed."""
    version = LooseVersion("")

    assert parse_spy == []
    assert not hasattr(version, "version")
    assert not hasattr(version, "vstring")
