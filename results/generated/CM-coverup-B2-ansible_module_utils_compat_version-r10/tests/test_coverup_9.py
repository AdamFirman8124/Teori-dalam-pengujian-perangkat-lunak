# file: project/ansible/module_utils/compat/version.py:327-328
# asked: {"lines": [328], "branches": []}
# gained: {"lines": [328], "branches": []}

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_looseversion_repr():
    """Cover LooseVersion.__repr__ (line 328)."""
    version = LooseVersion("1.5.1")
    result = repr(version)
    assert result == "LooseVersion ('1.5.1')"
    # str() is used inside __repr__, verify it matches the parsed version string
    assert str(version) == "1.5.1"
