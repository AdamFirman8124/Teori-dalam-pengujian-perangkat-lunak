# file: project/ansible/module_utils/compat/version.py:324-325
# asked: {"lines": [325], "branches": []}
# gained: {"lines": [325], "branches": []}

from ansible.module_utils.compat.version import LooseVersion


def test_looseversion_str_returns_vstring():
    v = LooseVersion("1.5.1")
    assert v.vstring == "1.5.1"
    assert str(v) == "1.5.1"
    assert str(v) == v.vstring


def test_looseversion_str_preserves_original_string():
    for s in ["1.5.2b2", "3.10a", "2.0b1pl0", "1.13++", "0.960923"]:
        v = LooseVersion(s)
        assert str(v) == s
