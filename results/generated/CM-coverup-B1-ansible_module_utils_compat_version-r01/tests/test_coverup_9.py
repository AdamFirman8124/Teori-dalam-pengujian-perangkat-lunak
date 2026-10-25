# file: project/ansible/module_utils/compat/version.py:327-328
# asked: {"lines": [328], "branches": []}
# gained: {"lines": [328], "branches": []}

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_repr():
    version = LooseVersion("1.2.3")
    assert repr(version) == "LooseVersion ('1.2.3')"
