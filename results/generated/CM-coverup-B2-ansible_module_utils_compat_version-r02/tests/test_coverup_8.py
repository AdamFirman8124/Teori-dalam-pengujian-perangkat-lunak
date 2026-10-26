# file: project/ansible/module_utils/compat/version.py:324-325
# asked: {"lines": [325], "branches": []}
# gained: {"lines": [325], "branches": []}

from ansible.module_utils.compat.version import LooseVersion


def test_looseversion_str_returns_vstring():
    v = LooseVersion("1.5.1")
    assert v.vstring == "1.5.1"
    assert str(v) == "1.5.1"
    assert v.__str__() == "1.5.1"


def test_looseversion_str_after_parse():
    v = LooseVersion()
    v.parse("2.0b1pl0")
    assert v.vstring == "2.0b1pl0"
    assert str(v) == "2.0b1pl0"
    assert v.__str__() == v.vstring
