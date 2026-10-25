# file: project/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}

import pytest
from ansible.module_utils.compat.version import StrictVersion


def test_cmp_str_operand_less():
    v = StrictVersion("1.0")
    assert v._cmp("2.0") == -1


def test_cmp_str_operand_greater():
    v = StrictVersion("2.0")
    assert v._cmp("1.0") == 1


def test_cmp_not_strictversion_returns_notimplemented():
    v = StrictVersion("1.0")
    assert v._cmp(123) is NotImplemented
    assert v._cmp(None) is NotImplemented
    assert v._cmp(["1.0"]) is NotImplemented


def test_cmp_version_less():
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("2.0")
    assert v1._cmp(v2) == -1


def test_cmp_version_greater():
    v1 = StrictVersion("2.0")
    v2 = StrictVersion("1.0")
    assert v1._cmp(v2) == 1


def test_cmp_no_prerelease_equal():
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("1.0")
    assert v1.version == v2.version
    assert v1.prerelease is None
    assert v2.prerelease is None
    assert v1._cmp(v2) == 0


def test_cmp_self_has_prerelease():
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0")
    assert v1.version == v2.version
    assert v1.prerelease and not v2.prerelease
    assert v1._cmp(v2) == -1


def test_cmp_other_has_prerelease():
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("1.0a1")
    assert v1.version == v2.version
    assert (not v1.prerelease) and v2.prerelease
    assert v1._cmp(v2) == 1


def test_cmp_both_prerelease_equal():
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0a1")
    assert v1.version == v2.version
    assert v1.prerelease == v2.prerelease
    assert v1._cmp(v2) == 0


def test_cmp_both_prerelease_less():
    v1 = StrictVersion("1.0a1")
    v2 = StrictVersion("1.0a2")
    assert v1.version == v2.version
    assert v1.prerelease != v2.prerelease
    assert v1.prerelease < v2.prerelease
    assert v1._cmp(v2) == -1


def test_cmp_both_prerelease_greater():
    v1 = StrictVersion("1.0b1")
    v2 = StrictVersion("1.0a1")
    assert v1.version == v2.version
    assert v1.prerelease != v2.prerelease
    assert not (v1.prerelease < v2.prerelease)
    assert v1._cmp(v2) == 1


class _FlakyPrerelease:
    def __init__(self):
        self.calls = 0

    def __bool__(self):
        self.calls += 1
        return self.calls in (1, 3)

    __nonzero__ = __bool__


def test_cmp_unreachable_else_raises():
    v1 = StrictVersion("1.0")
    v2 = StrictVersion("1.0")
    assert v1.version == v2.version
    flaky = _FlakyPrerelease()
    v1.prerelease = flaky
    with pytest.raises(AssertionError):
        v1._cmp(v2)
    assert flaky.calls == 4
