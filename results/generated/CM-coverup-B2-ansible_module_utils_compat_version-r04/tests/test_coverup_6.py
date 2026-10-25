# file: project/ansible/module_utils/compat/version.py:310-322
# asked: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}
# gained: {"lines": [314, 315, 316, 317, 318, 319, 320, 322], "branches": [[316, 317], [316, 322]]}

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_parse_mixed_components():
    version = LooseVersion("1.alpha02")

    assert version.vstring == "1.alpha02"
    assert version.version == [1, "alpha", 2]
    assert str(version) == "1.alpha02"


def test_loose_version_parse_replaces_existing_state():
    version = LooseVersion("9")
    version.parse("10beta.003")

    assert version.vstring == "10beta.003"
    assert version.version == [10, "beta", 3]
    assert str(version) == "10beta.003"
