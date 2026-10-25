# file: project/ansible/module_utils/compat/version.py:327-328
# asked: {"lines": [328], "branches": []}
# gained: {"lines": [328], "branches": []}

from ansible.module_utils.compat.version import LooseVersion


def test_looseversion_repr_simple():
    v = LooseVersion('1.5.1')
    assert str(v) == '1.5.1'
    assert repr(v) == "LooseVersion ('1.5.1')"


def test_looseversion_repr_uses_str():
    v = LooseVersion('2.0b1pl0')
    assert repr(v) == "LooseVersion ('%s')" % str(v)
    assert repr(v) == "LooseVersion ('2.0b1pl0')"
