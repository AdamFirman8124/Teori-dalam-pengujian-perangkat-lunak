# file: project/ansible/module_utils/compat/version.py:330-341
# asked: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 0], [340, 341]]}
# gained: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 341]]}

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_cmp_with_strings():
    assert LooseVersion("1.0")._cmp("1.0") == 0
    assert LooseVersion("1.0")._cmp("2.0") == -1
    assert LooseVersion("2.0")._cmp("1.0") == 1


def test_loose_version_cmp_with_loose_version():
    left = LooseVersion("1.0")
    right = LooseVersion("1.0")

    assert left._cmp(right) == 0


def test_loose_version_cmp_with_unsupported_type():
    version = LooseVersion("1.0")

    assert version._cmp(object()) is NotImplemented
