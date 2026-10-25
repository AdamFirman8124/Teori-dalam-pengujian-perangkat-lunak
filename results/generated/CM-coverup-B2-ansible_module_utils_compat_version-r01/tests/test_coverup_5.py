# file: project/ansible/module_utils/compat/version.py:158-167
# asked: {"lines": [159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}
# gained: {"lines": [159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


def test_str_two_component_version_omits_zero_patch():
    """Covers line 159-160: version[2] == 0 and no prerelease."""
    version = StrictVersion('0.4')

    assert version.version == (0, 4, 0)
    assert version.prerelease is None
    assert str(version) == '0.4'


def test_str_explicit_zero_patch_is_normalized():
    """Covers line 159-160: '0.4.0' parses to patch 0 and prints as '0.4'."""
    version = StrictVersion('0.4.0')

    assert version.version == (0, 4, 0)
    assert str(version) == '0.4'


def test_str_three_component_version_keeps_patch():
    """Covers line 162: version[2] != 0 and no prerelease."""
    version = StrictVersion('1.0.4')

    assert version.version == (1, 0, 4)
    assert version.prerelease is None
    assert str(version) == '1.0.4'


def test_str_prerelease_with_zero_patch():
    """Covers lines 159-160 and 164-165: zero patch plus prerelease."""
    version = StrictVersion('0.5a1')

    assert version.version == (0, 5, 0)
    assert version.prerelease == ('a', 1)
    assert str(version) == '0.5a1'


def test_str_prerelease_with_nonzero_patch():
    """Covers lines 162 and 164-165: nonzero patch plus prerelease."""
    version = StrictVersion('1.0.4b1')

    assert version.version == (1, 0, 4)
    assert version.prerelease == ('b', 1)
    assert str(version) == '1.0.4b1'


def test_str_roundtrip_for_all_documented_forms():
    """Covers line 167 return for every documented valid form."""
    for vstring in ('0.4', '0.4.1', '0.5a1', '0.5b3', '0.5', '0.9.6', '1.0', '1.0.4a3', '1.0.4b1', '1.0.4'):
        assert str(StrictVersion(vstring)) == vstring


def test_str_does_not_mutate_state():
    """Postcondition: repeated __str__ calls are stable and side-effect free."""
    version = StrictVersion('1.0.4b1')
    first = str(version)
    second = str(version)

    assert first == second == '1.0.4b1'
    assert version.version == (1, 0, 4)
    assert version.prerelease == ('b', 1)
