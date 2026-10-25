# file: project/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


class _BoolFlipper(object):
    """Truthiness that changes on each evaluation, used to reach the
    otherwise unreachable final ``else`` branch of StrictVersion._cmp."""

    def __init__(self, sequence):
        self._sequence = list(sequence)
        self._index = 0

    def __bool__(self):
        value = self._sequence[self._index]
        self._index += 1
        return value

    __nonzero__ = __bool__


def test_cmp_with_string_operand():
    """Line 170-171: a str operand is parsed into a StrictVersion."""
    left = StrictVersion('1.0')
    assert left._cmp('1.0') == 0
    assert left._cmp('2.0') == -1
    assert left._cmp('0.9') == 1
    # rich comparison routes through _cmp as well
    assert left == '1.0'
    assert left < '2.0'
    assert left > '0.9'


def test_cmp_with_incompatible_type_returns_notimplemented():
    """Lines 172-173: non-StrictVersion operands yield NotImplemented."""
    left = StrictVersion('1.0')
    assert left._cmp(1.0) is NotImplemented
    assert left._cmp(None) is NotImplemented
    assert left._cmp(object()) is NotImplemented
    # NotImplemented makes the rich comparison fall back to False
    assert (left == 1.0) is False
    assert (left != 1.0) is True


def test_cmp_numeric_version_mismatch():
    """Lines 175-181: differing numeric versions short-circuit."""
    assert StrictVersion('1.0')._cmp(StrictVersion('2.0')) == -1
    assert StrictVersion('2.0')._cmp(StrictVersion('1.0')) == 1
    assert StrictVersion('1.0.1')._cmp(StrictVersion('1.0.2')) == -1
    assert StrictVersion('1.0.2')._cmp(StrictVersion('1.0.1')) == 1


def test_cmp_neither_has_prerelease():
    """Lines 189-190: equal numeric versions without prerelease are equal."""
    left = StrictVersion('1.0')
    right = StrictVersion('1.0.0')
    assert left.version == right.version
    assert left.prerelease is None
    assert right.prerelease is None
    assert left._cmp(right) == 0
    assert left == right


def test_cmp_self_has_prerelease_only():
    """Lines 191-192: a prerelease sorts before the final release."""
    left = StrictVersion('1.0a1')
    right = StrictVersion('1.0')
    assert left.prerelease is not None
    assert right.prerelease is None
    assert left._cmp(right) == -1
    assert left < right


def test_cmp_other_has_prerelease_only():
    """Lines 193-194: the final release sorts after a prerelease."""
    left = StrictVersion('1.0')
    right = StrictVersion('1.0b2')
    assert left.prerelease is None
    assert right.prerelease is not None
    assert left._cmp(right) == 1
    assert left > right


def test_cmp_both_have_equal_prerelease():
    """Lines 195-197: identical prereleases compare equal."""
    left = StrictVersion('1.0a1')
    right = StrictVersion('1.0a1')
    assert left.prerelease == right.prerelease
    assert left._cmp(right) == 0
    assert left == right


def test_cmp_both_have_prerelease_less_than():
    """Lines 198-199: a smaller prerelease sorts first."""
    left = StrictVersion('1.0a1')
    right = StrictVersion('1.0b1')
    assert left.prerelease < right.prerelease
    assert left._cmp(right) == -1
    assert left < right


def test_cmp_both_have_prerelease_greater_than():
    """Lines 200-201: a larger prerelease sorts last."""
    left = StrictVersion('1.0b1')
    right = StrictVersion('1.0a1')
    assert left.prerelease > right.prerelease
    assert left._cmp(right) == 1
    assert left > right


def test_cmp_unreachable_else_raises_assertion_error(monkeypatch):
    """Line 203: the defensive ``else`` branch raises AssertionError.

    The branch is logically unreachable with real prerelease values, so the
    prerelease attributes are replaced with objects whose truthiness flips on
    each evaluation.  monkeypatch restores the original attributes afterwards.

    Note: the ``and``/``or`` conditions short-circuit, so ``other.prerelease``
    is only evaluated once (in the final ``elif``), while ``self.prerelease``
    is evaluated once per branch (four times total).
    """
    left = StrictVersion('1.0')
    right = StrictVersion('1.0')
    assert left.version == right.version

    # self.prerelease is evaluated in all four branches: True, False, True, True
    # makes every branch condition False.
    left_flipper = _BoolFlipper([True, False, True, True])
    # other.prerelease is only evaluated in the fourth branch (short-circuiting
    # skips it in the first three); False makes that condition False too.
    right_flipper = _BoolFlipper([False])

    monkeypatch.setattr(left, 'prerelease', left_flipper)
    monkeypatch.setattr(right, 'prerelease', right_flipper)

    with pytest.raises(AssertionError) as excinfo:
        left._cmp(right)

    assert 'never get here' in str(excinfo.value)
    # self.prerelease was evaluated once per branch (4 times);
    # other.prerelease was evaluated only in the final branch (1 time).
    assert left_flipper._index == 4
    assert right_flipper._index == 1
