# file: project/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


def test_cmp_string_other_is_converted():
    """Lines 170-171: a str other is converted to StrictVersion before comparing."""
    version = StrictVersion('1.0')

    # equal after conversion (falls through to the prerelease checks)
    assert version._cmp('1.0') == 0
    # converted other is numerically smaller
    assert version._cmp('0.9') == 1
    # converted other is numerically greater
    assert version._cmp('1.0.1') == -1
    # converted other carries a prerelease, self does not -> self is greater
    assert version._cmp('1.0a1') == 1


def test_cmp_unsupported_type_returns_not_implemented():
    """Lines 172-173: non-str, non-StrictVersion others yield NotImplemented."""
    version = StrictVersion('1.0')

    assert version._cmp(42) is NotImplemented
    assert version._cmp(None) is NotImplemented
    assert version._cmp(()) is NotImplemented
    assert version._cmp(object()) is NotImplemented
    # NotImplemented propagates through the rich comparison protocol
    assert (version == 42) is False


def test_cmp_numeric_version_less():
    """Lines 175, 178-179: self.version < other.version -> -1."""
    assert StrictVersion('1.0')._cmp(StrictVersion('1.0.1')) == -1
    assert StrictVersion('1.0')._cmp(StrictVersion('2.0')) == -1


def test_cmp_numeric_version_greater():
    """Lines 175, 180-181: self.version > other.version -> 1."""
    assert StrictVersion('1.0.1')._cmp(StrictVersion('1.0')) == 1
    assert StrictVersion('2.0')._cmp(StrictVersion('1.0')) == 1


def test_cmp_equal_versions_no_prerelease():
    """Lines 189-190: neither side has a prerelease -> 0."""
    assert StrictVersion('1.0')._cmp(StrictVersion('1.0.0')) == 0


def test_cmp_self_prerelease_other_release():
    """Lines 191-192: self has a prerelease, other does not -> -1."""
    assert StrictVersion('1.0a1')._cmp(StrictVersion('1.0')) == -1


def test_cmp_self_release_other_prerelease():
    """Lines 193-194: other has a prerelease, self does not -> 1."""
    assert StrictVersion('1.0')._cmp(StrictVersion('1.0b2')) == 1


def test_cmp_both_prerelease_equal():
    """Lines 195-197: both prereleases equal -> 0."""
    assert StrictVersion('1.0a1')._cmp(StrictVersion('1.0a1')) == 0


def test_cmp_both_prerelease_self_less():
    """Lines 198-199: both prereleases, self's is smaller -> -1."""
    assert StrictVersion('1.0a1')._cmp(StrictVersion('1.0a2')) == -1
    assert StrictVersion('1.0a1')._cmp(StrictVersion('1.0b1')) == -1


def test_cmp_both_prerelease_self_greater():
    """Lines 200-201: both prereleases, self's is greater -> 1."""
    assert StrictVersion('1.0a2')._cmp(StrictVersion('1.0a1')) == 1
    assert StrictVersion('1.0b2')._cmp(StrictVersion('1.0a1')) == 1


def test_rich_comparisons_delegate_to_cmp():
    """The Version rich operators route through _cmp (lines 170-201)."""
    assert StrictVersion('1.0') == StrictVersion('1.0.0')
    assert StrictVersion('1.0a1') < StrictVersion('1.0')
    assert StrictVersion('1.0') > StrictVersion('1.0a1')
    assert StrictVersion('1.0') <= StrictVersion('1.0')
    assert StrictVersion('1.0') >= StrictVersion('1.0')
    assert StrictVersion('0.9') < StrictVersion('1.0')
    assert StrictVersion('1.1') > StrictVersion('1.0')


def test_cmp_final_else_guard_raises():
    """Line 203: the trailing else is unreachable for consistently-truthy
    prerelease values; a stateful prerelease object makes every branch test
    fail so the AssertionError guard is finally executed."""
    class FlakyPrerelease:
        def __init__(self):
            self.bool_checks = 0

        def __bool__(self):
            self.bool_checks += 1
            # truthy on the first check, falsy on every later one
            return self.bool_checks == 1

    self_version = StrictVersion('1.0')   # prerelease is None (always falsy)
    other_version = StrictVersion('1.0')
    other_version.prerelease = FlakyPrerelease()

    with pytest.raises(AssertionError, match='never get here'):
        self_version._cmp(other_version)

    # both truthiness evaluations of other.prerelease actually happened
    assert other_version.prerelease.bool_checks == 2
