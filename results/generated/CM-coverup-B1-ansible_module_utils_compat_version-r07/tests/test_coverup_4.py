# file: project/ansible/module_utils/compat/version.py:140-156
# asked: {"lines": [141, 142, 143, 145, 146, 148, 149, 151, 153, 154, 156], "branches": [[142, 143], [142, 145], [148, 149], [148, 151], [153, 154], [153, 156]]}
# gained: {"lines": [141, 142, 143, 145, 146, 148, 149, 151, 153, 154, 156], "branches": [[142, 143], [142, 145], [148, 149], [148, 151], [153, 154], [153, 156]]}

import pytest
from ansible.module_utils.compat.version import StrictVersion


def test_strict_version_invalid_raises():
    with pytest.raises(ValueError, match="invalid version number '1'"):
        StrictVersion("1")


def test_strict_version_invalid_four_components_raises():
    with pytest.raises(ValueError, match="invalid version number"):
        StrictVersion("2.7.2.2")


def test_strict_version_two_components_no_prerelease():
    v = StrictVersion("0.4")
    assert v.version == (0, 4, 0)
    assert v.prerelease is None
    assert str(v) == "0.4"


def test_strict_version_three_components_no_prerelease():
    v = StrictVersion("0.4.1")
    assert v.version == (0, 4, 1)
    assert v.prerelease is None
    assert str(v) == "0.4.1"


def test_strict_version_two_components_with_prerelease_a():
    v = StrictVersion("0.5a1")
    assert v.version == (0, 5, 0)
    assert v.prerelease == ("a", 1)
    assert str(v) == "0.5a1"


def test_strict_version_two_components_with_prerelease_b():
    v = StrictVersion("0.5b3")
    assert v.version == (0, 5, 0)
    assert v.prerelease == ("b", 3)
    assert str(v) == "0.5b3"


def test_strict_version_three_components_with_prerelease():
    v = StrictVersion("1.0.4a3")
    assert v.version == (1, 0, 4)
    assert v.prerelease == ("a", 3)
    assert str(v) == "1.0.4a3"


def test_strict_version_three_components_with_prerelease_b():
    v = StrictVersion("1.0.4b1")
    assert v.version == (1, 0, 4)
    assert v.prerelease == ("b", 1)
    assert str(v) == "1.0.4b1"
