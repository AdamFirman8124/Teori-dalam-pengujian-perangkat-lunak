# file: project/ansible/module_utils/compat/version.py:330-341
# asked: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 0], [340, 341]]}
# gained: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 341]]}

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_cmp_converts_string_and_returns_equal():
    assert LooseVersion("1.0")._cmp("1.0") == 0


def test_loose_version_cmp_returns_not_implemented_for_unsupported_type():
    assert LooseVersion("1.0")._cmp(object()) is NotImplemented


def test_loose_version_cmp_returns_less_than_and_greater_than():
    lower = LooseVersion("1.0")
    higher = LooseVersion("2.0")

    assert lower._cmp(higher) == -1
    assert higher._cmp(lower) == 1
