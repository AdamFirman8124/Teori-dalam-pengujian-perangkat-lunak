# file: project/ansible/module_utils/compat/version.py:324-325
# asked: {"lines": [325], "branches": []}
# gained: {"lines": [325], "branches": []}

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_str_returns_vstring():
    version = LooseVersion("1.2.3")
    assert version.vstring == "1.2.3"
    assert str(version) == "1.2.3"
    assert str(version) == version.vstring


def test_loose_version_str_preserves_original_formatting():
    raw = "1.0b1pl0"
    version = LooseVersion(raw)
    assert version.vstring == raw
    assert str(version) == raw


def test_loose_version_str_after_parse():
    version = LooseVersion()
    version.parse("2.2beta29")
    assert version.vstring == "2.2beta29"
    assert str(version) == "2.2beta29"


def test_loose_version_str_used_by_repr():
    version = LooseVersion("3.10a")
    assert str(version) == "3.10a"
    assert repr(version) == "LooseVersion ('3.10a')"


def test_loose_version_str_in_string_context():
    version = LooseVersion("0.960923")
    assert "{}".format(version) == "0.960923"
    assert "%s" % version == "0.960923"
    assert f"{version}" == "0.960923"
