# file: project/ansible/module_utils/compat/version.py:158-167
# asked: {"lines": [159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}
# gained: {"lines": [159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


@pytest.mark.parametrize(
    "vstring,expected",
    [
        # version[2] == 0 -> two-component string (lines 159-160)
        ("1.2", "1.2"),
        ("1.2.0", "1.2"),
        # version[2] != 0 -> three-component string (lines 161-162)
        ("1.2.3", "1.2.3"),
        # prerelease branch taken (lines 164-165)
        ("1.2a1", "1.2a1"),
        ("1.2.3b3", "1.2.3b3"),
        # prerelease branch not taken (line 164 false branch)
        ("0.4.1", "0.4.1"),
    ],
)
def test_strict_version_str(vstring, expected):
    version = StrictVersion(vstring)
    assert str(version) == expected
    # postcondition: __str__ output round-trips through parse
    reparsed = StrictVersion(str(version))
    assert reparsed.version == version.version
    assert reparsed.prerelease == version.prerelease


def test_strict_version_str_patch_zero():
    version = StrictVersion("2.7.0")
    assert version.version == (2, 7, 0)
    assert version.prerelease is None
    assert str(version) == "2.7"


def test_strict_version_str_patch_nonzero():
    version = StrictVersion("2.7.9")
    assert version.version == (2, 7, 9)
    assert str(version) == "2.7.9"


def test_strict_version_str_prerelease():
    version = StrictVersion("1.0.4a3")
    assert version.version == (1, 0, 4)
    assert version.prerelease == ("a", 3)
    assert str(version) == "1.0.4a3"


def test_strict_version_str_prerelease_patch_zero():
    version = StrictVersion("0.5b3")
    assert version.version == (0, 5, 0)
    assert version.prerelease == ("b", 3)
    assert str(version) == "0.5b3"
