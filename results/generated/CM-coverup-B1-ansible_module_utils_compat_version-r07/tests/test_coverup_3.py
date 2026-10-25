# file: project/ansible/module_utils/compat/version.py:330-341
# asked: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 0], [340, 341]]}
# gained: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 341]]}

import pytest

from ansible.module_utils.compat.version import LooseVersion


@pytest.fixture
def loose():
    """A LooseVersion instance that must not be mutated by comparisons."""
    return LooseVersion('1.0')


def test_cmp_with_string_equal(loose):
    assert loose._cmp('1.0') == 0
    # postcondition: comparing against a str must not mutate self
    assert loose.vstring == '1.0'
    assert loose.version == [1, 0]


def test_cmp_with_string_less(loose):
    assert loose._cmp('1.1') == -1
    assert loose.vstring == '1.0'
    assert loose.version == [1, 0]


def test_cmp_with_string_greater(loose):
    assert loose._cmp('0.9') == 1
    assert loose.vstring == '1.0'
    assert loose.version == [1, 0]


def test_cmp_with_string_subclass(loose):
    class MyStr(str):
        pass

    assert loose._cmp(MyStr('1.0')) == 0
    assert loose._cmp(MyStr('2.0')) == -1


def test_cmp_equal_loose_versions():
    assert LooseVersion('1.0')._cmp(LooseVersion('1.0')) == 0


def test_cmp_less_loose_versions():
    assert LooseVersion('1.0')._cmp(LooseVersion('1.0.1')) == -1


def test_cmp_greater_loose_versions():
    assert LooseVersion('2.0')._cmp(LooseVersion('1.9')) == 1


def test_cmp_with_loose_version_subclass():
    class MyLooseVersion(LooseVersion):
        pass

    assert LooseVersion('1.0')._cmp(MyLooseVersion('1.0')) == 0
    assert LooseVersion('1.0')._cmp(MyLooseVersion('1.1')) == -1
    assert LooseVersion('1.1')._cmp(MyLooseVersion('1.0')) == 1


@pytest.mark.parametrize('other', [1, 1.0, None, object(), [1, 0], (1, 0)])
def test_cmp_returns_not_implemented_for_other_types(loose, other):
    result = loose._cmp(other)
    assert result is NotImplemented
    assert loose.vstring == '1.0'
    assert loose.version == [1, 0]


def test_operators_accept_strings(loose):
    assert loose == '1.0'
    assert not (loose != '1.0')
    assert loose < '1.1'
    assert loose <= '1.0'
    assert loose > '0.9'
    assert loose >= '1.0'
    assert loose.vstring == '1.0'
    assert loose.version == [1, 0]


def test_operators_with_incomparable_type(loose):
    # _cmp returns NotImplemented, so equality falls back to identity
    assert (loose == 1) is False
    assert (loose != 1) is True
    with pytest.raises(TypeError):
        loose < 1
    with pytest.raises(TypeError):
        loose > 1
    assert loose.vstring == '1.0'
    assert loose.version == [1, 0]
