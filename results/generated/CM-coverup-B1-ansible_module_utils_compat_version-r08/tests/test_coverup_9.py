# file: project/ansible/module_utils/compat/version.py:327-328
# asked: {"lines": [328], "branches": []}
# gained: {"lines": [328], "branches": []}

from ansible.module_utils.compat.version import LooseVersion


def test_looseversion_repr_simple():
    v = LooseVersion('1.5.1')
    assert repr(v) == "LooseVersion ('1.5.1')"
    assert repr(v) == "LooseVersion ('%s')" % str(v)


def test_looseversion_repr_with_letters():
    v = LooseVersion('1.5.2b2')
    assert str(v) == '1.5.2b2'
    assert repr(v) == "LooseVersion ('1.5.2b2')"


def test_looseversion_repr_matches_str():
    v = LooseVersion('3.10a')
    expected = "LooseVersion ('%s')" % str(v)
    assert repr(v) == expected
    assert repr(v) == "LooseVersion ('3.10a')"
