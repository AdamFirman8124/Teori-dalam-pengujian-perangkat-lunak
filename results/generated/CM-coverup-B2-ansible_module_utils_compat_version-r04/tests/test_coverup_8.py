# file: project/ansible/module_utils/compat/version.py:324-325
# asked: {"lines": [325], "branches": []}
# gained: {"lines": [325], "branches": []}

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_str_returns_vstring():
    vstring = "1.5.2b2"
    version = LooseVersion(vstring)
    assert str(version) == vstring
    assert version.__str__() == vstring
    assert version.vstring == vstring
