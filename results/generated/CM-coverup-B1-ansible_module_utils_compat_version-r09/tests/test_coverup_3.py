# file: project/ansible/module_utils/compat/version.py:330-341
# asked: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 0], [340, 341]]}
# gained: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 341]]}

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_cmp_with_string_other():
    """Lines 331-332: str other is converted to LooseVersion."""
    assert LooseVersion('1.5.0')._cmp('1.5.0') == 0
    assert LooseVersion('1.5.0')._cmp('1.4.0') == 1
    assert LooseVersion('1.5.0')._cmp('1.6.0') == -1


def test_cmp_with_loose_version_other():
    """Line 333 falls through: other is already a LooseVersion."""
    assert LooseVersion('2.0')._cmp(LooseVersion('2.0')) == 0
    assert LooseVersion('2.0')._cmp(LooseVersion('1.9')) == 1
    assert LooseVersion('2.0')._cmp(LooseVersion('2.1')) == -1


def test_cmp_with_unsupported_type_returns_not_implemented():
    """Lines 333-334: non-str, non-LooseVersion other -> NotImplemented."""
    assert LooseVersion('1.0')._cmp(42) is NotImplemented
    assert LooseVersion('1.0')._cmp(None) is NotImplemented
    assert LooseVersion('1.0')._cmp([1, 0]) is NotImplemented


def test_rich_comparisons_with_unsupported_type():
    """NotImplemented from _cmp propagates through the rich comparisons.

    __eq__/__ne__ return NotImplemented internally, so Python falls back
    to identity comparison and yields False/True. Ordering comparisons
    fall back to the reflected int operation, which raises TypeError.
    """
    lv = LooseVersion('1.0')

    # __eq__ returns NotImplemented internally; the == operator then
    # falls back to identity comparison, yielding False.
    assert (lv == 42) is False
    assert (lv != 42) is True

    # Ordering falls back to the reflected int operation, which raises.
    with pytest.raises(TypeError):
        lv < 42
    with pytest.raises(TypeError):
        lv > 42
    with pytest.raises(TypeError):
        lv <= 42
    with pytest.raises(TypeError):
        lv >= 42


def test_cmp_equal_branch():
    """Lines 336-337: equal versions return 0."""
    assert LooseVersion('1.2.3')._cmp(LooseVersion('1.2.3')) == 0


def test_cmp_less_branch():
    """Lines 338-339: self < other returns -1."""
    assert LooseVersion('1.2.3')._cmp(LooseVersion('1.2.4')) == -1


def test_cmp_greater_branch():
    """Lines 340-341: self > other returns 1."""
    assert LooseVersion('1.2.4')._cmp(LooseVersion('1.2.3')) == 1
