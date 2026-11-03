# file: project/ansible/module_utils/compat/version.py:330-341
# asked: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 0], [340, 341]]}
# gained: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 341]]}

"""Tests for LooseVersion._cmp in ansible/module_utils/compat/version.py.

These tests exercise lines 331-341:
  - coercion of a str operand into a LooseVersion (331-332)
  - returning NotImplemented for unsupported operand types (333-334)
  - the equal / less-than / greater-than comparison outcomes (336-341)

The tests are side-effect free: they only build local objects and never
mutate module or global state, so no monkeypatching/cleanup is required.
"""
import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_cmp_coerces_string_operand():
    """Lines 331-332: a str operand is converted to a LooseVersion."""
    v = LooseVersion('1.0')

    # Comparing a list (self.version) against a str would raise TypeError,
    # so these results prove the str operand was really coerced.
    assert v._cmp('1.0') == 0
    assert v._cmp('2.0') == -1
    assert v._cmp('0.9') == 1

    # Same code paths exercised through the base-class rich comparisons,
    # which route to _cmp.
    assert v == '1.0'
    assert v < '2.0'
    assert v > '0.9'
    assert v <= '1.0'
    assert v >= '1.0'


def test_cmp_unsupported_type_returns_not_implemented():
    """Lines 333-334: non-str, non-LooseVersion operand -> NotImplemented."""
    v = LooseVersion('1.0')

    assert v._cmp(42) is NotImplemented
    assert v._cmp(None) is NotImplemented
    assert v._cmp(object()) is NotImplemented

    # Through the operators: __eq__ propagating NotImplemented falls back
    # to identity-based equality (False), while ordering raises TypeError.
    assert (v == 42) is False
    assert (v != 42) is True
    with pytest.raises(TypeError):
        v < 42
    with pytest.raises(TypeError):
        v > 42


def test_cmp_equal_versions():
    """Lines 336-337: equal versions compare as 0."""
    assert LooseVersion('1.0')._cmp(LooseVersion('1.0')) == 0
    assert LooseVersion('1.0') == LooseVersion('1.0')
    assert not LooseVersion('1.0') != LooseVersion('1.0')


def test_cmp_less_than():
    """Lines 338-339: a smaller version compares as -1."""
    assert LooseVersion('1.0')._cmp(LooseVersion('2.0')) == -1
    assert LooseVersion('1.0') < LooseVersion('2.0')
    assert LooseVersion('1.0') <= LooseVersion('2.0')
    assert not LooseVersion('1.0') > LooseVersion('2.0')


def test_cmp_greater_than():
    """Lines 340-341: a larger version compares as 1."""
    assert LooseVersion('2.0')._cmp(LooseVersion('1.0')) == 1
    assert LooseVersion('2.0') > LooseVersion('1.0')
    assert LooseVersion('2.0') >= LooseVersion('1.0')
    assert not LooseVersion('2.0') < LooseVersion('1.0')
