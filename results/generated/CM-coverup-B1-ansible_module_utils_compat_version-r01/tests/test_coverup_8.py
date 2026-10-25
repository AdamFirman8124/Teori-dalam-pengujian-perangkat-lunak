# file: project/ansible/module_utils/compat/version.py:324-325
# asked: {"lines": [325], "branches": []}
# gained: {"lines": [325], "branches": []}

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_str_returns_original_version_string():
    version_string = "1.13++"
    version = LooseVersion(version_string)

    assert version.vstring == version_string
    assert str(version) == version_string
