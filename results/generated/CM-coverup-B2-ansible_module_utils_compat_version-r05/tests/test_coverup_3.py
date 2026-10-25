# file: project/ansible/module_utils/compat/version.py:330-341
# asked: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 0], [340, 341]]}
# gained: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 341]]}

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_cmp_with_string_argument():
    """Line 331-332: str argument is converted to LooseVersion."""
    v = LooseVersion('1.5')
    assert v._cmp('1.5') == 0
    assert v._cmp('1.4') == 1
    assert v._cmp('1.6') == -1


def test_cmp_with_non_version_type_returns_not_implemented():
    """Line 333-334: unsupported type yields NotImplemented."""
    v = LooseVersion('1.5')
    assert v._cmp(42) is NotImplemented
    assert v._cmp(3.14) is NotImplemented
    assert v._cmp(b'1.5') is NotImplemented


def test_rich_comparison_with_unsupported_type():
    """Rich comparisons fall back gracefully when _cmp returns NotImplemented."""
    v = LooseVersion('1.5')
    assert (v == 42) is False
    assert (v != 42) is True
    with pytest.raises(TypeError):
        v < 42


def test_cmp_equal_versions():
    """Line 336-337: equal versions return 0."""
    assert LooseVersion('1.5.1')._cmp(LooseVersion('1.5.1')) == 0
    assert LooseVersion('1.5.1') == LooseVersion('1.5.1')


def test_cmp_less_than():
    """Line 338-339: smaller version returns -1."""
    assert LooseVersion('1.4')._cmp(LooseVersion('1.5')) == -1
    assert LooseVersion('1.4') < LooseVersion('1.5')


def test_cmp_greater_than():
    """Line 340-341: larger version returns 1."""
    assert LooseVersion('2.0')._cmp(LooseVersion('1.9.9')) == 1
    assert LooseVersion('2.0') > LooseVersion('1.9.9')
