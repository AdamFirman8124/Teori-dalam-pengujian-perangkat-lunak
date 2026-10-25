# file: project/ansible/module_utils/compat/version.py:330-341
# asked: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 0], [340, 341]]}
# gained: {"lines": [331, 332, 333, 334, 336, 337, 338, 339, 340, 341], "branches": [[331, 332], [331, 333], [333, 334], [333, 336], [336, 337], [336, 338], [338, 339], [338, 340], [340, 0], [340, 341]]}

from ansible.module_utils.compat.version import LooseVersion


def test_loose_version_cmp_converts_string_and_detects_equality():
    assert LooseVersion("1.2")._cmp("1.2") == 0


def test_loose_version_cmp_returns_not_implemented_for_unsupported_type():
    assert LooseVersion("1.2")._cmp(object()) is NotImplemented


def test_loose_version_cmp_detects_lower_version():
    assert LooseVersion("1.2")._cmp(LooseVersion("1.3")) == -1


def test_loose_version_cmp_detects_higher_version():
    assert LooseVersion("1.3")._cmp(LooseVersion("1.2")) == 1


def test_loose_version_cmp_falls_through_for_incomparable_components(monkeypatch):
    class Incomparable:
        def __eq__(self, other):
            return False

        def __lt__(self, other):
            return False

        def __gt__(self, other):
            return False

    left = LooseVersion("1")
    right = LooseVersion("2")
    monkeypatch.setattr(left, "version", [Incomparable()])
    monkeypatch.setattr(right, "version", [Incomparable()])

    assert left._cmp(right) is None
