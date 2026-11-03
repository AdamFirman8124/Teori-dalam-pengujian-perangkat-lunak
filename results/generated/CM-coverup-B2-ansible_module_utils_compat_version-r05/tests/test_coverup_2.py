# file: project/ansible/module_utils/compat/version.py:39-81
# asked: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}
# gained: {"lines": [47, 48, 51, 54, 55, 56, 57, 60, 61, 62, 63, 66, 67, 68, 69, 72, 73, 74, 75, 78, 79, 80, 81], "branches": [[47, 0], [47, 48], [55, 56], [55, 57], [61, 62], [61, 63], [67, 68], [67, 69], [73, 74], [73, 75], [79, 80], [79, 81]]}

"""Tests for ansible/module_utils/compat/version.py targeting the uncovered
lines/branches of the Version base class (lines 47-48, 51, 54-57, 60-63,
66-69, 72-75, 78-81).

Every test only creates local objects; no module or global state is mutated,
so no explicit cleanup (monkeypatch/mocker) is required.
"""

import pytest

from ansible.module_utils.compat.version import LooseVersion, StrictVersion, Version


def test_init_with_vstring_calls_parse():
    """Version.__init__ with a truthy vstring must delegate to self.parse (lines 47-48)."""

    class RecordingVersion(Version):
        def parse(self, vstring):
            self.parsed = vstring

    v = RecordingVersion('1.2.3')
    assert v.parsed == '1.2.3'


def test_init_without_vstring_does_not_parse():
    """Version.__init__ with no vstring or vstring=None must not invoke parse (line 47, falsy branch)."""

    class RecordingVersion(Version):
        def parse(self, vstring):
            self.parsed = vstring

    for v in (RecordingVersion(), RecordingVersion(vstring=None)):
        assert not hasattr(v, 'parsed')


def test_repr():
    """Version.__repr__ formats the class name plus str() of the instance (line 51)."""

    class StringyVersion(Version):
        def parse(self, vstring):
            self.vstring = vstring

        def __str__(self):
            return self.vstring

    v = StringyVersion('1.2.3')
    assert repr(v) == "%s ('1.2.3')" % type(v).__name__


def test_eq_both_branches():
    """Version.__eq__ (lines 54-57): equal, unequal and NotImplemented paths."""
    a = LooseVersion('1.2.3')
    same = LooseVersion('1.2.3')
    diff = LooseVersion('1.2.4')

    assert (a == same) is True              # c == 0 -> True (lines 54, 57)
    assert (a == diff) is False             # c != 0 -> False (lines 54, 57)
    assert (a != diff) is True

    assert a.__eq__(42) is NotImplemented   # unsupported other (lines 55-56)
    # Rich protocol falls back to identity comparison -> False, no exception.
    assert (a == 42) is False
    assert (a != 42) is True


def test_lt_both_branches():
    """Version.__lt__ (lines 60-63)."""
    low = LooseVersion('1.2')
    high = LooseVersion('1.3')

    assert (low < high) is True             # c < 0 -> True (lines 60, 63)
    assert (high < low) is False

    assert low.__lt__(42) is NotImplemented  # lines 61-62
    assert Version.__lt__(low, 42) is NotImplemented
    with pytest.raises(TypeError):
        low < 42


def test_le_both_branches():
    """Version.__le__ (lines 66-69)."""
    low = LooseVersion('1.2')
    high = LooseVersion('1.3')

    assert (low <= high) is True            # lines 66, 69
    assert (low <= low) is True
    assert (high <= low) is False

    assert low.__le__(42) is NotImplemented  # lines 67-68
    with pytest.raises(TypeError):
        high <= 42


def test_gt_both_branches():
    """Version.__gt__ (lines 72-75)."""
    low = LooseVersion('1.2')
    high = LooseVersion('1.3')

    assert (high > low) is True             # lines 72, 75
    assert (low > high) is False

    assert low.__gt__(42) is NotImplemented  # lines 73-74
    with pytest.raises(TypeError):
        low > 42


def test_ge_both_branches():
    """Version.__ge__ (lines 78-81)."""
    low = LooseVersion('1.2')
    high = LooseVersion('1.3')

    assert (low >= low) is True             # lines 78, 81
    assert (high >= low) is True
    assert (low >= high) is False

    assert low.__ge__(42) is NotImplemented  # lines 79-80
    with pytest.raises(TypeError):
        low >= 42


def test_strict_version_rich_comparisons_route_through_base_class():
    """StrictVersion has no rich comparisons of its own: exercise lines 54-81
    through StrictVersion._cmp return values (-1/0/1/NotImplemented)."""
    assert (StrictVersion('1.0.4') == StrictVersion('1.0.4')) is True
    assert (StrictVersion('1.0.4') == '1.0.4') is True      # str other is converted
    assert (StrictVersion('1.0.4') != StrictVersion('1.0.3')) is True

    assert (StrictVersion('0.5a1') < StrictVersion('0.5')) is True
    assert (StrictVersion('0.5') < StrictVersion('0.5a1')) is False

    assert (StrictVersion('0.5a1') <= StrictVersion('0.5b3')) is True
    assert (StrictVersion('0.5') <= StrictVersion('0.5a1')) is False

    assert (StrictVersion('0.5') > StrictVersion('0.5b3')) is True
    assert (StrictVersion('0.5a1') > StrictVersion('0.5')) is False

    assert (StrictVersion('0.5') >= StrictVersion('0.4.1')) is True
    assert (StrictVersion('0.4.1') >= StrictVersion('0.5')) is False

    assert StrictVersion('1.0.4').__eq__(object()) is NotImplemented
    assert StrictVersion('1.0.4').__lt__(object()) is NotImplemented
    assert StrictVersion('1.0.4').__le__(object()) is NotImplemented
    assert StrictVersion('1.0.4').__gt__(object()) is NotImplemented
    assert StrictVersion('1.0.4').__ge__(object()) is NotImplemented
