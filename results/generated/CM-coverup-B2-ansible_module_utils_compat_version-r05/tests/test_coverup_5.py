# file: project/ansible/module_utils/compat/version.py:158-167
# asked: {"lines": [159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}
# gained: {"lines": [159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


def test_str_two_component_version():
    """Covers line 159-160: version[2] == 0 branch, no prerelease."""
    v = StrictVersion('1.2')
    assert str(v) == '1.2'


def test_str_three_component_zero_patch():
    """Covers line 159-160: explicit zero patch, no prerelease."""
    v = StrictVersion('1.2.0')
    assert str(v) == '1.2'


def test_str_three_component_nonzero_patch():
    """Covers line 162: version[2] != 0 branch, no prerelease."""
    v = StrictVersion('1.2.3')
    assert str(v) == '1.2.3'


def test_str_with_prerelease():
    """Covers lines 164-165: prerelease appended to vstring."""
    v = StrictVersion('1.0.4a3')
    assert str(v) == '1.0.4a3'


def test_str_with_prerelease_and_zero_patch():
    """Covers lines 159-160 and 164-165 together."""
    v = StrictVersion('0.5b1')
    assert str(v) == '0.5b1'


def test_str_does_not_mutate_state():
    """__str__ must be side-effect free (no state pollution)."""
    v = StrictVersion('1.2.3a1')
    before = (v.version, v.prerelease)
    str(v)
    assert (v.version, v.prerelease) == before
