# file: project/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


def test_cmp_with_string_operand():
    """Lines 170-171: a str operand is converted into a StrictVersion."""
    v = StrictVersion('1.0')
    assert v == '1.0'
    assert v < '1.1'
    assert v > '0.9'
    assert v._cmp('1.0') == 0


def test_cmp_with_unsupported_operand_returns_not_implemented():
    """Lines 172-173: operands that are neither str nor StrictVersion yield NotImplemented."""
    v = StrictVersion('1.0')
    assert v._cmp(object()) is NotImplemented
    # NotImplemented propagates out of __eq__/__lt__, so Python falls back
    # to the default (identity/reflected) behaviour.
    assert (v == object()) is False
    with pytest.raises(TypeError):
        v < object()


def test_cmp_numeric_version_mismatch():
    """Lines 175-181: differing numeric versions decide the outcome; prereleases are ignored."""
    assert StrictVersion('1.0') < StrictVersion('2.0')
    assert StrictVersion('2.0') > StrictVersion('1.0')
    # prerelease stuff doesn't matter when numeric versions differ
    assert StrictVersion('1.0b2') < StrictVersion('1.1')


def test_cmp_equal_versions_without_prerelease():
    """Lines 189-190: neither side has a prerelease -> they are equal."""
    assert StrictVersion('1.0') == StrictVersion('1.0.0')


def test_cmp_self_prerelease_other_release():
    """Lines 191-192: self has a prerelease, other does not -> self is smaller."""
    assert StrictVersion('1.0a1') < StrictVersion('1.0')


def test_cmp_self_release_other_prerelease():
    """Lines 193-194: other has a prerelease, self does not -> self is greater."""
    assert StrictVersion('1.0') > StrictVersion('1.0a1')


def test_cmp_both_same_prerelease():
    """Lines 195-197: both have identical prereleases -> equal."""
    assert StrictVersion('1.0a1') == StrictVersion('1.0a1')


def test_cmp_both_prerelease_self_smaller():
    """Lines 198-199: self's prerelease sorts before other's -> self is smaller."""
    assert StrictVersion('1.0a1') < StrictVersion('1.0b2')


def test_cmp_both_prerelease_self_greater():
    """Line 201: self's prerelease sorts after other's -> self is greater."""
    assert StrictVersion('1.0b2') > StrictVersion('1.0a1')


def test_cmp_defensive_else_raises_assertion_error():
    """Line 203: the defensive else is unreachable with stable truthiness, because the
    if/elif chain covers every truthiness combination.  It only fires when
    self.prerelease flips its truthiness between evaluations, so feed it an
    object whose __bool__ alternates True/False/True/False..."""

    class FlippingPrerelease:
        def __init__(self):
            self.calls = 0

        def __bool__(self):
            self.calls += 1
            return self.calls % 2 == 1

    v1 = StrictVersion('1.0')
    v2 = StrictVersion('1.0')
    v1.prerelease = FlippingPrerelease()

    with pytest.raises(AssertionError, match='never get here'):
        v1 == v2

    # each of the four chain conditions short-circuited on self.prerelease
    assert v1.prerelease.calls == 4
