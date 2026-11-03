# file: project/ansible/module_utils/compat/version.py:158-167
# asked: {"lines": [159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}
# gained: {"lines": [159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}

"""Tests for StrictVersion.__str__ (ansible/module_utils/compat/version.py, lines 159-167).

These tests are pure: they only construct local StrictVersion objects and never
mutate module-level state, so no monkeypatching or cleanup fixtures are needed.
"""

from ansible.module_utils.compat.version import StrictVersion


def test_str_two_component_version():
    """Covers line 159 (version[2] == 0 is True), line 160, line 164 (prerelease falsy) and line 167."""
    version = StrictVersion("1.2")
    assert version.version == (1, 2, 0)
    assert version.prerelease is None
    assert str(version) == "1.2"


def test_str_three_component_version():
    """Covers line 159 (version[2] == 0 is False), line 162, line 164 (prerelease falsy) and line 167."""
    version = StrictVersion("1.2.3")
    assert version.version == (1, 2, 3)
    assert version.prerelease is None
    assert str(version) == "1.2.3"


def test_str_two_component_version_with_prerelease():
    """Covers lines 159-160 (version[2] == 0), lines 164-165 (prerelease truthy) and line 167."""
    version = StrictVersion("0.5a1")
    assert version.version == (0, 5, 0)
    assert version.prerelease == ("a", 1)
    assert str(version) == "0.5a1"


def test_str_three_component_version_with_prerelease():
    """Covers lines 161-162 (version[2] != 0), lines 164-165 (prerelease truthy) and line 167."""
    version = StrictVersion("1.0.4b3")
    assert version.version == (1, 0, 4)
    assert version.prerelease == ("b", 3)
    assert str(version) == "1.0.4b3"
