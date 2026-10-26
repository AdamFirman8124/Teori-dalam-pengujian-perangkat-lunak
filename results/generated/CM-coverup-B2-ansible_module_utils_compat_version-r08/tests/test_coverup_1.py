# file: project/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}

import pytest
from ansible.module_utils.compat.version import StrictVersion


def test_cmp_str_equal_covers_convert_and_no_prerelease():
    v = StrictVersion("1.0")
    result = v._cmp("1.0")
    assert result == 0


def test_cmp_str_less_covers_version_less_via_str():
    v = StrictVersion("1.0")
    result = v._cmp("2.0")
    assert result == -1


def test_cmp_str_greater_covers_version_greater_via_str():
    v = StrictVersion("2.0")
    result = v._cmp("1.0")
    assert result == 1


def test_cmp_non_strictversion_returns_notimplemented():
    v = StrictVersion("1.0")
    assert v._cmp(123) is NotImplemented
    assert v._cmp(None) is NotImplemented
    assert v._cmp(object()) is NotImplemented


def test_cmp_version_less():
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("2.0")
    assert v1.version != v2.version
    assert v1._cmp(v2) == -1


def test_cmp_version_greater():
    v1 = StrictVersion("2.0")
    v2 = StrictVersion("1.0")
    assert v1.version != v2.version
    assert v1._cmp(v2) == 1


def test_cmp_neither_has_prerelease_equal():
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("1.0")
    assert v1.version == v2.version
    assert not v1.prerelease and not v2.prerelease
    assert v1._cmp(v2) == 0


def test_cmp_self_has_prerelease_only():
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0")
    assert v1.version == v2.version
    assert v1.prerelease and not v2.prerelease
    assert v1._cmp(v2) == -1


def test_cmp_other_has_prerelease_only():
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("1.0a1")
    assert v1.version == v2.version
    assert not v1.prerelease and v2.prerelease
    assert v1._cmp(v2) == 1


def test_cmp_both_prerelease_equal():
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0a1")
    assert v1.version == v2.version
    assert v1.prerelease and v2.prerelease
    assert v1.prerelease == v2.prerelease
    assert v1._cmp(v2) == 0


def test_cmp_both_prerelease_less():
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0a2")
    assert v1.version == v2.version
    assert v1.prerelease and v2.prerelease
    assert v1.prerelease != v2.prerelease
    assert v1.prerelease < v2.prerelease
    assert v1._cmp(v2) == -1


def test_cmp_both_prerelease_greater():
    v1 = StrictVersion("1.0b1")
    v2 = StrictVersion("1.0a2")
    assert v1.version == v2.version
    assert v1.prerelease and v2.prerelease
    assert v1.prerelease != v2.prerelease
    assert not (v1.prerelease < v2.prerelease)
    assert v1._cmp(v2) == 1


def test_cmp_both_prerelease_greater_same_letter():
    v1 = StrictVersion("1.0a2")
    v2 = StrictVersion("1.0a1")
    assert v1._cmp(v2) == 1


def test_cmp_unreachable_else_raises_assertion(monkeypatch):
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("1.0")
    assert v1.version == v2.version

    class Flapping:
        def __init__(self):
            self.calls = 0

        def __bool__(self):
            self.calls += 1
            # True, False, True, False -> makes all four prerelease
            # conditions False so else branch is reached
            return (self.calls % 2) == 1

        __nonzero__ = __bool__

    flapping = Flapping()
    monkeypatch.setattr(v1, "prerelease", flapping)
    with pytest.raises(AssertionError):
        v1._cmp(v2)
    # 4 boolean evaluations: cond1, cond2, cond3, cond4
    assert flapping.calls == 4
