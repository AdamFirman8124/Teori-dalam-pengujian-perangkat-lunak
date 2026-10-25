# file: project/ansible/module_utils/compat/version.py:310-322
# asked: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}
# gained: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_parse_converts_numeric_components():
    version = LooseVersion("1.02.300")

    assert version.vstring == "1.02.300"
    assert version.version == [1, 2, 300]


def test_loose_version_parse_preserves_non_numeric_components():
    version = LooseVersion("2beta.03pl")

    assert version.vstring == "2beta.03pl"
    assert version.version == [2, "beta", 3, "pl"]
