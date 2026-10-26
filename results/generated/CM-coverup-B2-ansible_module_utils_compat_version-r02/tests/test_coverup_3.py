# file: project/ansible/module_utils/compat/version.py:330-341
# asked: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 0], [340, 341]]}
# gained: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 341]]}

import pytest
from ansible.module_utils.compat.version import LooseVersion


def test_cmp_str_equal_returns_zero():
    v = LooseVersion("1.5.1")
    result = v._cmp("1.5.1")
    assert result == 0
    assert v.version == LooseVersion("1.5.1").version


def test_cmp_str_less_returns_minus_one():
    v = LooseVersion("1.5.1")
    result = v._cmp("1.5.2")
    assert result == -1
    assert v.version < LooseVersion("1.5.2").version


def test_cmp_str_greater_returns_one():
    v = LooseVersion("1.5.2")
    result = v._cmp("1.5.1")
    assert result == 1
    assert v.version > LooseVersion("1.5.1").version


def test_cmp_looseversion_equal_returns_zero():
    v = LooseVersion("1.5.1")
    other = LooseVersion("1.5.1")
    assert v._cmp(other) == 0


def test_cmp_looseversion_less_returns_minus_one():
    v = LooseVersion("1.5.1")
    other = LooseVersion("1.5.2b2")
    assert v._cmp(other) == -1


def test_cmp_looseversion_greater_returns_one():
    v = LooseVersion("161")
    other = LooseVersion("11g")
    # 161 -> [161], 11g -> [11, 'g'], so [161] > [11, 'g']
    assert v._cmp(other) == 1


def test_cmp_invalid_type_returns_not_implemented():
    v = LooseVersion("1.5.1")
    assert v._cmp(123) is NotImplemented
    assert v._cmp(None) is NotImplemented
    assert v._cmp(object()) is NotImplemented
    assert v._cmp(["1.5.1"]) is NotImplemented
