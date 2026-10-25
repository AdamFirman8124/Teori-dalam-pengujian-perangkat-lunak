# file: project/ansible/module_utils/compat/version.py:158-167
# asked: {"lines": [159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}
# gained: {"lines": [159, 160, 162, 164, 165, 167], "branches": [[159, 160], [159, 162], [164, 165], [164, 167]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


@pytest.mark.parametrize(
    ("version_string", "expected"),
    [
        ("1.2", "1.2"),
        ("1.2.3a4", "1.2.3a4"),
    ],
)
def test_strict_version_str_covers_component_and_prerelease_branches(
    version_string, expected
):
    version = StrictVersion(version_string)

    assert str(version) == expected
