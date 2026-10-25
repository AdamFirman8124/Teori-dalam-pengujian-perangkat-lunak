# file: project/ansible/module_utils/compat/version.py:140-156
# asked: {"lines": [141, 142, 143, 145, 146, 148, 149, 151, 153, 154, 156], "branches": [[142, 143], [142, 145], [148, 149], [148, 151], [153, 154], [153, 156]]}
# gained: {"lines": [141, 142, 143, 145, 146, 148, 149, 151, 153, 154, 156], "branches": [[142, 143], [142, 145], [148, 149], [148, 151], [153, 154], [153, 156]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


def test_strict_version_parse_rejects_invalid_version():
    with pytest.raises(ValueError) as exc_info:
        StrictVersion("invalid")

    assert str(exc_info.value) == "invalid version number 'invalid'"


def test_strict_version_parse_with_patch_and_prerelease():
    version = StrictVersion("1.2.3b4")

    assert version.version == (1, 2, 3)
    assert version.prerelease == ("b", 4)


def test_strict_version_parse_without_patch_or_prerelease():
    version = StrictVersion("5.6")

    assert version.version == (5, 6, 0)
    assert version.prerelease is None
