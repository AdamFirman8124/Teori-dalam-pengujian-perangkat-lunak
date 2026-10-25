# file: project/ansible/module_utils/compat/version.py:140-156
# asked: {"lines": [141, 142, 143, 145, 146, 148, 149, 151, 153, 154, 156], "branches": [[142, 143], [142, 145], [148, 149], [148, 151], [153, 154], [153, 156]]}
# gained: {"lines": [141, 142, 143, 145, 146, 148, 149, 151, 153, 154, 156], "branches": [[142, 143], [142, 145], [148, 149], [148, 151], [153, 154], [153, 156]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


@pytest.mark.parametrize(
    ("vstring", "expected_version", "expected_prerelease"),
    [
        ("1.2.3a4", (1, 2, 3), ("a", 4)),
        ("5.6", (5, 6, 0), None),
    ],
)
def test_strict_version_parse_valid_versions(
    vstring, expected_version, expected_prerelease
):
    version = StrictVersion(vstring)

    assert version.version == expected_version
    assert version.prerelease == expected_prerelease


def test_strict_version_parse_rejects_invalid_version():
    with pytest.raises(ValueError, match=r"^invalid version number '1\.2\.3\.4'$"):
        StrictVersion("1.2.3.4")
