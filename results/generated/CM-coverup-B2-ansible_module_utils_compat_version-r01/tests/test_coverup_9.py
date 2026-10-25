# file: project/ansible/module_utils/compat/version.py:327-328
# asked: {"lines": [328], "branches": []}
# gained: {"lines": [328], "branches": []}

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_repr():
    """Ensure LooseVersion.__repr__ (line 328) executes and returns the expected format."""
    version = LooseVersion("1.5.2b2")
    result = repr(version)
    assert result == "LooseVersion ('1.5.2b2')"


def test_loose_version_repr_matches_str():
    """Ensure __repr__ embeds the same string produced by __str__."""
    version = LooseVersion("3.4j")
    assert repr(version) == "LooseVersion ('%s')" % str(version)
    assert repr(version) == "LooseVersion ('3.4j')"
