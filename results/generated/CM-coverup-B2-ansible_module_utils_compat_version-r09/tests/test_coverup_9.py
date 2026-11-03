# file: project/ansible/module_utils/compat/version.py:327-328
# asked: {"lines": [328], "branches": []}
# gained: {"lines": [328], "branches": []}

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_repr():
    """Execute LooseVersion.__repr__ (line 328) and verify its output format."""
    v = LooseVersion('1.5.2b2')
    result = repr(v)
    # Line 328: return "LooseVersion ('%s')" % str(self)
    assert result == "LooseVersion ('1.5.2b2')"
    # __repr__ delegates to __str__ for the version string
    assert str(v) == '1.5.2b2'


def test_loose_version_repr_numeric_version():
    """Cover line 328 with a purely numeric version string as well."""
    v = LooseVersion('1.5.1')
    assert repr(v) == "LooseVersion ('1.5.1')"
