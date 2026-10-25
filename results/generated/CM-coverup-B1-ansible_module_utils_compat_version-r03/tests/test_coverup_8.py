# file: project/ansible/module_utils/compat/version.py:324-325
# asked: {"lines": [325], "branches": []}
# gained: {"lines": [325], "branches": []}

import pytest

from ansible.module_utils.compat.version import LooseVersion


@pytest.mark.parametrize("vstring", ["1.5.1", "2.2beta29", "1.13++", "161"])
def test_loose_version_str_returns_vstring(vstring):
    version = LooseVersion(vstring)
    assert str(version) == vstring
    assert version.vstring == vstring


def test_loose_version_str_matches_parsed_string():
    vstring = "3.4j"
    version = LooseVersion(vstring)
    # __str__ must return the exact original string, not the parsed components
    assert version.__str__() == vstring
    assert isinstance(version.__str__(), str)
