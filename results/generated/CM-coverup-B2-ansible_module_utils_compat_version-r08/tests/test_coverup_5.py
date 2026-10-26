# file: project/ansible/module_utils/compat/version.py:158-167
# asked: {"lines": [159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}
# gained: {"lines": [159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}

from ansible.module_utils.compat.version import StrictVersion


def test_strict_version_str_omits_zero_patch_component():
    version = StrictVersion("1.2")

    assert version.version == (1, 2, 0)
    assert version.prerelease is None
    assert str(version) == "1.2"


def test_strict_version_str_includes_patch_and_prerelease():
    version = StrictVersion("1.2.3b4")

    assert version.version == (1, 2, 3)
    assert version.prerelease == ("b", 4)
    assert str(version) == "1.2.3b4"


def test_strict_version_str_zero_patch_with_prerelease():
    version = StrictVersion("1.2a1")

    assert version.version == (1, 2, 0)
    assert version.prerelease == ("a", 1)
    assert str(version) == "1.2a1"


def test_strict_version_str_nonzero_patch_without_prerelease():
    version = StrictVersion("1.2.3")

    assert version.version == (1, 2, 3)
    assert version.prerelease is None
    assert str(version) == "1.2.3"
