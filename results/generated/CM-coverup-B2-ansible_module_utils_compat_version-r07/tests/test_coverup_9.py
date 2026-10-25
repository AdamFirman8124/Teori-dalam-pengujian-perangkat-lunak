# file: project/ansible/module_utils/compat/version.py:327-328
# asked: {"lines": [328], "branches": []}
# gained: {"lines": [328], "branches": []}

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_repr():
    """Ensure LooseVersion.__repr__ (line 328) executes and returns the expected format."""
    version = LooseVersion('1.5.1')
    result = repr(version)
    assert result == "LooseVersion ('1.5.1')"
    # Also verify str() used inside __repr__ works as expected
    assert str(version) == '1.5.1'
