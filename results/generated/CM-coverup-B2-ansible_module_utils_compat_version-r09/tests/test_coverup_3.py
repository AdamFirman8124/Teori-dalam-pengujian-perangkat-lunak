# file: project/ansible/module_utils/compat/version.py:330-341
# asked: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 0], [340, 341]]}
# gained: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 341]]}

"""Tests covering LooseVersion._cmp in ansible/module_utils/compat/version.py.

These tests are pure (no global state, files, or environment changes are
touched), so no explicit teardown/monkeypatching is required.
"""

import pytest

from ansible.module_utils.compat.version import LooseVersion


def test_cmp_with_str_other_equal():
    """Lines 331-332 (str branch) and 336-337: a str other is coerced to
    LooseVersion and equal versions compare as 0."""
    lv = LooseVersion("1.5.1")
    result = lv._cmp("1.5.1")
    assert result == 0


def test_cmp_with_str_other_less_and_greater():
    """Lines 331-332 plus 338-341: str coercion followed by ordering
    comparisons in both directions."""
    lv = LooseVersion("1.5.1")
    assert lv._cmp("1.5.2") == -1  # self.version < other.version
    assert lv._cmp("1.5.0") == 1   # self.version > other.version


def test_cmp_with_looseversion_other():
    """Line 333 False branch: other is already a LooseVersion, so no
    coercion happens and ordering still works."""
    lv = LooseVersion("2.0.1")
    assert lv._cmp(LooseVersion("2.0.1")) == 0
    assert lv._cmp(LooseVersion("2.0.2")) == -1
    assert lv._cmp(LooseVersion("2.0.0")) == 1


def test_cmp_with_unsupported_type_returns_not_implemented():
    """Lines 333-334: other is neither str nor LooseVersion, so _cmp
    returns NotImplemented."""
    lv = LooseVersion("1.0")
    assert lv._cmp(42) is NotImplemented
    assert lv._cmp(None) is NotImplemented
    assert lv._cmp(["1", "0"]) is NotImplemented


def test_rich_comparison_operators_route_through_cmp():
    """The Version rich-comparison operators delegate to _cmp, so the
    str-coercion path is exercised through normal operator usage too."""
    lv = LooseVersion("1.5.1")
    assert lv == "1.5.1"
    assert lv == LooseVersion("1.5.1")
    assert lv < "1.5.2"
    assert lv <= "1.5.1"
    assert lv > "1.5.0"
    assert lv >= "1.5.1"
    assert not (lv == "1.5.2")


def test_comparison_with_incompatible_type():
    """Comparing against an unsupported type surfaces the NotImplemented
    result as a failed equality and a TypeError for ordering."""
    lv = LooseVersion("1.0")
    with pytest.raises(TypeError):
        lv < 42
    assert (lv == 42) is False
