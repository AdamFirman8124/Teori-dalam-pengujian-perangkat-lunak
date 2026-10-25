# file: project/ansible/module_utils/compat/version.py:158-167
# asked: {"lines": [159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}
# gained: {"lines": [159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


@pytest.mark.parametrize(
    "vstring, expected",
    [
        # version[2] == 0 branch (line 159-160), no prerelease (line 164 False)
        ("1.2", "1.2"),
        # version[2] == 0 branch, explicit .0 also collapses
        ("1.2.0", "1.2"),
        # version[2] != 0 branch (line 162), no prerelease
        ("1.2.3", "1.2.3"),
        # version[2] == 0 branch with prerelease (lines 165)
        ("1.2a1", "1.2a1"),
        # version[2] != 0 branch with prerelease
        ("1.2.3b2", "1.2.3b2"),
    ],
)
def test_strict_version_str(vstring, expected):
    version = StrictVersion(vstring)
    assert str(version) == expected
    # postcondition: str() round-trips through parse
    assert StrictVersion(str(version)) == version


def test_strict_version_str_prerelease_letter_and_number():
    version = StrictVersion("2.0.1a13")
    # prerelease is stored as a (letter, number) tuple
    assert version.prerelease == ("a", 13)
    assert str(version) == "2.0.1a13"
