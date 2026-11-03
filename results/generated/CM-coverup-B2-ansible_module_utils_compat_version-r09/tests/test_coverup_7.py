# file: project/ansible/module_utils/compat/version.py:306-308
# asked: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}
# gained: {"lines": [307, 308], "branches": [[307, 0], [307, 308]]}

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_init_with_vstring_parses():
    """Lines 307-308: a truthy vstring must trigger self.parse(vstring)."""
    lv = LooseVersion("1.5.2b2")
    assert lv.vstring == "1.5.2b2"
    assert lv.version == [1, 5, 2, 'b', 2]


def test_loose_version_init_with_numeric_vstring():
    """Lines 307-308 with a purely numeric version string."""
    lv = LooseVersion("1.5.1")
    assert lv.vstring == "1.5.1"
    assert lv.version == [1, 5, 1]


def test_loose_version_init_without_vstring_skips_parse():
    """False branch of line 307: no vstring -> parse() is never called."""
    lv = LooseVersion()
    assert not hasattr(lv, "vstring")
    assert not hasattr(lv, "version")


def test_loose_version_init_with_falsy_vstring_skips_parse():
    """False branch of line 307: None and '' are falsy -> parse() skipped."""
    for falsy in (None, ""):
        lv = LooseVersion(falsy)
        assert not hasattr(lv, "vstring")
        assert not hasattr(lv, "version")
