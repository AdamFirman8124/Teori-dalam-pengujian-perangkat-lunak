# file: project/ansible/module_utils/compat/version.py:324-325
# asked: {"lines": [325], "branches": []}
# gained: {"lines": [325], "branches": []}

"""Tests for ansible.module_utils.compat.version.LooseVersion.__str__ (line 325)."""

import pytest

from ansible.module_utils.compat.version import LooseVersion


@pytest.fixture
def version_strings():
    """Provide sample version strings; nothing persists after the test."""
    return [
        "1.5.1",
        "1.5.2b2",
        "161",
        "3.10a",
        "8.02",
        "3.4j",
        "1996.07.12",
        "3.2.pl0",
        "1.13++",
        "2.2beta29",
    ]


def test_str_returns_vstring_exactly(version_strings):
    """Line 325: __str__ must return the stored vstring unchanged."""
    for vstring in version_strings:
        version = LooseVersion(vstring)
        result = str(version)
        assert result == vstring
        # __str__ returns the very same object held in .vstring
        assert result is version.vstring


def test_str_via_dunder_call():
    """Calling __str__ directly also exercises line 325."""
    version = LooseVersion("2.0b1pl0")
    assert version.__str__() == "2.0b1pl0"


def test_str_after_explicit_parse():
    """A LooseVersion built empty then parsed manually still stringifies."""
    version = LooseVersion()
    assert not hasattr(version, "vstring")  # nothing parsed yet
    version.parse("5.5.kw")
    assert str(version) == "5.5.kw"
    assert version.version == [5, 5, "kw"]


def test_str_does_not_mutate_state(version_strings):
    """Stringification must not alter the parsed representation."""
    for vstring in version_strings:
        version = LooseVersion(vstring)
        before = list(version.version)
        str(version)
        assert version.version == before
        assert version.vstring == vstring
