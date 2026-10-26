# file: project/ansible/module_utils/compat/version.py:306-308
# asked: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}
# gained: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}

from ansible.module_utils.compat.version import LooseVersion


def test_looseversion_init_with_vstring_parses():
    lv = LooseVersion("1.2.3")
    assert lv.vstring == "1.2.3"
    assert lv.version == [1, 2, 3]


def test_looseversion_init_without_vstring_skips_parse():
    lv = LooseVersion()
    assert not hasattr(lv, "vstring")
    assert not hasattr(lv, "version")


def test_looseversion_init_with_none_skips_parse():
    lv = LooseVersion(None)
    assert not hasattr(lv, "vstring")
    assert not hasattr(lv, "version")


def test_looseversion_init_with_empty_string_skips_parse():
    lv = LooseVersion("")
    assert not hasattr(lv, "vstring")
    assert not hasattr(lv, "version")
