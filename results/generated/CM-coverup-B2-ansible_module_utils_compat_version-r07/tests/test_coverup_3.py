# file: project/ansible/module_utils/compat/version.py:330-341
# asked: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 0], [340, 341]]}
# gained: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 341]]}

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_cmp_with_string_converts_and_compares_equal():
    version = LooseVersion('1.0')
    assert version._cmp('1.0') == 0
    # postcondition: the receiver is not mutated by the comparison
    assert version.version == [1, 0]


def test_cmp_with_string_less_and_greater():
    assert LooseVersion('1.0')._cmp('1.1') == -1
    assert LooseVersion('1.1')._cmp('1.0') == 1


def test_cmp_with_looseversion_instance():
    assert LooseVersion('1.0')._cmp(LooseVersion('1.0')) == 0
    assert LooseVersion('1.0')._cmp(LooseVersion('1.1')) == -1
    assert LooseVersion('1.1')._cmp(LooseVersion('1.0')) == 1


def test_cmp_with_unsupported_type_returns_notimplemented():
    version = LooseVersion('1.0')
    assert version._cmp(1) is NotImplemented
    assert version._cmp(None) is NotImplemented
    assert version._cmp(object()) is NotImplemented
    assert version.version == [1, 0]


def test_rich_comparisons_with_string():
    version = LooseVersion('1.0')
    assert version == '1.0'
    assert not (version != '1.0')
    assert version < '1.1'
    assert version <= '1.0'
    assert version > '0.9'
    assert version >= '1.0'
    assert version.version == [1, 0]


def test_rich_comparisons_with_unsupported_type():
    version = LooseVersion('1.0')
    assert not (version == 1)
    assert version != 1
    with pytest.raises(TypeError):
        version < 1
    assert version.version == [1, 0]
