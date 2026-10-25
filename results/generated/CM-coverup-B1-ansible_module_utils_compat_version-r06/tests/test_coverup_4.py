# file: project/ansible/module_utils/compat/version.py:140-156
# asked: {"lines": [141, 142, 143, 145, 146, 148, 149, 151, 153, 154, 156], "branches": [[142, 143], [142, 145], [148, 149], [148, 151], [153, 154], [153, 156]]}
# gained: {"lines": [141, 142, 143, 145, 146, 148, 149, 151, 153, 154, 156], "branches": [[142, 143], [142, 145], [148, 149], [148, 151], [153, 154], [153, 156]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


@pytest.mark.parametrize(
    "vstring,expected_version,expected_prerelease",
    [
        # patch present, prerelease present
        ("1.0.4a3", (1, 0, 4), ("a", 3)),
        ("1.0.4b1", (1, 0, 4), ("b", 1)),
        # patch present, no prerelease
        ("1.0.4", (1, 0, 4), None),
        ("0.9.6", (0, 9, 6), None),
        # no patch, prerelease present
        ("0.5a1", (0, 5, 0), ("a", 1)),
        ("0.5b3", (0, 5, 0), ("b", 3)),
        # no patch, no prerelease
        ("0.4", (0, 4, 0), None),
        ("1.0", (1, 0, 0), None),
    ],
)
def test_strict_version_parse_valid(vstring, expected_version, expected_prerelease):
    """All four combinations of the patch / prerelease branches."""
    version = StrictVersion(vstring)

    assert version.version == expected_version
    assert version.prerelease == expected_prerelease


def test_strict_version_parse_called_directly():
    """parse() can be invoked on an instance built without a vstring."""
    version = StrictVersion()
    assert not hasattr(version, "version")

    version.parse("2.7.18b2")

    assert version.version == (2, 7, 18)
    assert version.prerelease == ("b", 2)


@pytest.mark.parametrize(
    "vstring",
    [
        "1",           # too few components
        "2.7.2.2",     # too many components
        "1.3.a4",      # non-numeric patch
        "1.3pl1",      # unknown suffix
        "1.3c4",       # invalid prerelease letter
        "not-a-version",
    ],
)
def test_strict_version_parse_invalid_raises_value_error(vstring):
    """The no-match branch raises ValueError mentioning the bad string."""
    with pytest.raises(ValueError) as excinfo:
        StrictVersion(vstring)

    assert vstring in str(excinfo.value)


def test_strict_version_parse_invalid_leaves_instance_unparsed():
    """A failed parse must not leave partial state behind."""
    version = StrictVersion()

    with pytest.raises(ValueError):
        version.parse("1.3.a4")

    assert not hasattr(version, "version")
    assert not hasattr(version, "prerelease")


def test_strict_version_empty_string_is_not_parsed():
    """An empty vstring is falsy, so __init__ never calls parse()."""
    version = StrictVersion("")

    assert not hasattr(version, "version")
    assert not hasattr(version, "prerelease")
