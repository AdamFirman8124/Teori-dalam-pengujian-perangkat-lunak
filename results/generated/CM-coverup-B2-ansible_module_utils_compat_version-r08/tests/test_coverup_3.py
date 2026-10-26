# file: project/ansible/module_utils/compat/version.py:330-341
# asked: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 0], [340, 341]]}
# gained: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 341]]}

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_cmp_with_string_equal():
    v = LooseVersion('1.0')
    assert v._cmp('1.0') == 0
    # postcondition: receiver is unchanged
    assert v.version == [1, 0]
    assert str(v) == '1.0'


def test_cmp_with_string_less():
    v = LooseVersion('1.0')
    assert v._cmp('1.1') == -1
    assert v.version == [1, 0]


def test_cmp_with_string_greater():
    v = LooseVersion('1.1')
    assert v._cmp('1.0') == 1
    assert v.version == [1, 1]


def test_cmp_with_looseversion_equal():
    a = LooseVersion('2.3.4')
    b = LooseVersion('2.3.4')
    assert a._cmp(b) == 0
    assert b._cmp(a) == 0
    assert a.version == [2, 3, 4]
    assert b.version == [2, 3, 4]


def test_cmp_with_looseversion_less():
    a = LooseVersion('2.3.4')
    b = LooseVersion('2.3.5')
    assert a._cmp(b) == -1
    assert b._cmp(a) == 1


def test_cmp_with_looseversion_greater():
    a = LooseVersion('3.0')
    b = LooseVersion('2.9')
    assert a._cmp(b) == 1
    assert b._cmp(a) == -1


@pytest.mark.parametrize('other', [1, 1.0, None, object(), [1, 0], (1, 0)])
def test_cmp_with_unsupported_type_returns_notimplemented(other):
    v = LooseVersion('1.0')
    assert v._cmp(other) is NotImplemented
    # postcondition: receiver untouched
    assert v.version == [1, 0]


def test_rich_comparison_with_unsupported_type():
    v = LooseVersion('1.0')
    # NotImplemented from _cmp makes Python fall back to identity comparison
    assert (v == 1) is False
    assert (v != 1) is True
    with pytest.raises(TypeError):
        v < 1
    with pytest.raises(TypeError):
        v > 1
    assert v.version == [1, 0]


def test_rich_comparison_with_string():
    v = LooseVersion('1.0')
    assert v == '1.0'
    assert v <= '1.0'
    assert v >= '1.0'
    assert v < '1.1'
    assert v > '0.9'
    assert v.version == [1, 0]
