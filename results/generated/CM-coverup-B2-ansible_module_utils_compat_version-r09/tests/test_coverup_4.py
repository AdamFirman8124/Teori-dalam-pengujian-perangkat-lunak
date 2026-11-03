# file: project/ansible/module_utils/compat/version.py:140-156
# asked: {"lines": [141, 142, 143, 145, 146, 148, 149, 151, 153, 154, 156], "branches": [[142, 143], [142, 145], [148, 149], [148, 151], [153, 154], [153, 156]]}
# gained: {"lines": [141, 142, 143, 145, 146, 148, 149, 151, 153, 154, 156], "branches": [[142, 143], [142, 145], [148, 149], [148, 151], [153, 154], [153, 156]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


def test_parse_with_patch_and_no_prerelease():
    """Covers lines 141-149 (match, patch truthy) and 156 (prerelease falsy)."""
    version = StrictVersion()
    version.parse("1.2.3")
    assert version.version == (1, 2, 3)
    assert version.prerelease is None


def test_parse_without_patch_and_no_prerelease():
    """Covers line 151 (patch falsy) and 156 (prerelease falsy)."""
    version = StrictVersion()
    version.parse("2.7")
    assert version.version == (2, 7, 0)
    assert version.prerelease is None


def test_parse_prerelease_without_patch():
    """Covers line 151 (patch falsy) and lines 153-154 (prerelease truthy)."""
    version = StrictVersion()
    version.parse("1.5a1")
    assert version.version == (1, 5, 0)
    assert version.prerelease == ("a", 1)


def test_parse_prerelease_with_patch():
    """Covers lines 148-149 (patch truthy) and lines 153-154 (prerelease truthy)."""
    version = StrictVersion()
    version.parse("1.5.2b2")
    assert version.version == (1, 5, 2)
    assert version.prerelease == ("b", 2)


def test_parse_invalid_version_raises_value_error():
    """Covers lines 142-143 (no regex match -> ValueError)."""
    version = StrictVersion()
    with pytest.raises(ValueError, match="invalid version number '1\\.3\\.a4'"):
        version.parse("1.3.a4")


def test_parse_via_constructor():
    """Version.__init__ delegates to StrictVersion.parse when given a string."""
    version = StrictVersion("0.4.1")
    assert version.version == (0, 4, 1)
    assert version.prerelease is None
