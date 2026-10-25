# file: project/ansible/module_utils/compat/version.py:140-156
# asked: {"lines": [141, 142, 143, 145, 146, 148, 149, 151, 153, 154, 156], "branches": [[142, 143], [142, 145], [148, 149], [148, 151], [153, 154], [153, 156]]}
# gained: {"lines": [141, 142, 143, 145, 146, 148, 149, 151, 153, 154, 156], "branches": [[142, 143], [142, 145], [148, 149], [148, 151], [153, 154], [153, 156]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


def test_strictversion_invalid_string_raises():
    """Lines 142-143: non-matching version string raises ValueError."""
    with pytest.raises(ValueError, match="invalid version number '1.3.c4'"):
        StrictVersion("1.3.c4")


def test_strictversion_with_patch_and_no_prerelease():
    """Lines 148-149 and 156: three-component version, no prerelease tag."""
    v = StrictVersion("1.2.3")
    assert v.version == (1, 2, 3)
    assert v.prerelease is None


def test_strictversion_without_patch():
    """Line 151: two-component version gets implicit patch of 0."""
    v = StrictVersion("2.7")
    assert v.version == (2, 7, 0)
    assert v.prerelease is None


def test_strictversion_with_prerelease():
    """Lines 153-154: 'a'/'b' tag with number is parsed into prerelease tuple."""
    v = StrictVersion("1.0.4a3")
    assert v.version == (1, 0, 4)
    assert v.prerelease == ("a", 3)

    v2 = StrictVersion("0.5b12")
    assert v2.version == (0, 5, 0)
    assert v2.prerelease == ("b", 12)


def test_strictversion_prerelease_ordering():
    """Postcondition: prerelease sorts before the corresponding release."""
    assert StrictVersion("1.0.4a3") < StrictVersion("1.0.4")
    assert StrictVersion("1.0.4b1") < StrictVersion("1.0.4")
    assert StrictVersion("1.0.4a3") < StrictVersion("1.0.4b1")
