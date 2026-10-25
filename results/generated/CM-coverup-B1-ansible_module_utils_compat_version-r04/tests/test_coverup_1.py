# file: project/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}

import pytest
from ansible.module_utils.compat.version import StrictVersion


def test_cmp_str_equal():
    v = StrictVersion('1.0')
    assert v._cmp('1.0') == 0


def test_cmp_str_less():
    v = StrictVersion('1.0')
    assert v._cmp('2.0') == -1


def test_cmp_str_greater():
    v = StrictVersion('2.0')
    assert v._cmp('1.0') == 1


def test_cmp_str_prerelease():
    v = StrictVersion('1.0a1')
    assert v._cmp('1.0') == -1
    assert StrictVersion('1.0')._cmp('1.0a1') == 1


def test_cmp_not_implemented():
    v = StrictVersion('1.0')
    assert v._cmp(123) is NotImplemented
    assert v._cmp(None) is NotImplemented
    assert v._cmp(object()) is NotImplemented
    assert v._cmp(['1.0']) is NotImplemented


def test_cmp_numeric_less():
    assert StrictVersion('1.0')._cmp(StrictVersion('2.0')) == -1


def test_cmp_numeric_greater():
    assert StrictVersion('2.0')._cmp(StrictVersion('1.0')) == 1


def test_cmp_no_prerelease_equal():
    assert StrictVersion('1.0')._cmp(StrictVersion('1.0')) == 0


def test_cmp_self_prerelease_other_not():
    assert StrictVersion('1.0a1')._cmp(StrictVersion('1.0')) == -1


def test_cmp_self_no_prerelease_other_has():
    assert StrictVersion('1.0')._cmp(StrictVersion('1.0a1')) == 1


def test_cmp_both_prerelease_equal():
    assert StrictVersion('1.0a1')._cmp(StrictVersion('1.0a1')) == 0
    assert StrictVersion('1.0b1')._cmp(StrictVersion('1.0b1')) == 0


def test_cmp_both_prerelease_less():
    assert StrictVersion('1.0a1')._cmp(StrictVersion('1.0b1')) == -1
    assert StrictVersion('1.0a1')._cmp(StrictVersion('1.0a2')) == -1


def test_cmp_both_prerelease_greater():
    assert StrictVersion('1.0b1')._cmp(StrictVersion('1.0a1')) == 1
    assert StrictVersion('1.0a2')._cmp(StrictVersion('1.0a1')) == 1


def test_cmp_unreachable_else_raises():
    class FlakyStrictVersion(StrictVersion):
        def __init__(self, version, seq):
            self.version = version
            self._seq = list(seq)
            self._idx = 0

        @property
        def prerelease(self):
            val = self._seq[self._idx % len(self._seq)]
            self._idx += 1
            return val

        @prerelease.setter
        def prerelease(self, value):
            pass

    other = StrictVersion('1.0')
    flaky = FlakyStrictVersion(other.version, [('a', 1), None, ('a', 1), None])
    assert flaky.version == other.version
    with pytest.raises(AssertionError, match='never get here'):
        flaky._cmp(other)
