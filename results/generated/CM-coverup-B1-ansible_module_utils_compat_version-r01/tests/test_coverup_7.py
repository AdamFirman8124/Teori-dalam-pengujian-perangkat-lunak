# file: project/ansible/module_utils/compat/version.py:306-308
# asked: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}
# gained: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_init_parses_truthy_version_string():
    version = LooseVersion("1.5.2b2")

    assert version.vstring == "1.5.2b2"
    assert version.version == [1, 5, 2, "b", 2]
    assert str(version) == "1.5.2b2"


def test_loose_version_init_without_version_string_does_not_parse():
    version = LooseVersion()

    assert not hasattr(version, "vstring")
    assert not hasattr(version, "version")
