# file: project/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [196, 197], [196, 198], [198, 199], [198, 201]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


class TestStrictVersionCmp:
    def test_cmp_with_string_other(self):
        # covers lines 170-171: str converted to StrictVersion
        assert StrictVersion('1.0') == '1.0'
        assert StrictVersion('1.0') < '1.1'
        assert StrictVersion('1.1') > '1.0'

    def test_cmp_with_unsupported_type_returns_not_implemented(self):
        # covers lines 172-173: non-str, non-StrictVersion -> NotImplemented
        assert StrictVersion('1.0')._cmp(object()) is NotImplemented

    def test_cmp_numeric_less(self):
        # covers lines 175-179: versions differ, self < other
        assert StrictVersion('1.0') < StrictVersion('2.0')
        assert StrictVersion('1.0.0') < StrictVersion('1.0.1')

    def test_cmp_numeric_greater(self):
        # covers lines 180-181: versions differ, self > other
        assert StrictVersion('2.0') > StrictVersion('1.0')
        assert StrictVersion('1.0.1') > StrictVersion('1.0.0')

    def test_cmp_equal_no_prerelease(self):
        # covers lines 189-190: neither has prerelease
        assert StrictVersion('1.0') == StrictVersion('1.0.0')
        assert not (StrictVersion('1.0') < StrictVersion('1.0.0'))
        assert not (StrictVersion('1.0') > StrictVersion('1.0.0'))

    def test_cmp_self_prerelease_other_not(self):
        # covers lines 191-192: self has prerelease, other doesn't
        assert StrictVersion('1.0a1') < StrictVersion('1.0')

    def test_cmp_self_not_other_prerelease(self):
        # covers lines 193-194: other has prerelease, self doesn't
        assert StrictVersion('1.0') > StrictVersion('1.0a1')

    def test_cmp_both_prerelease_equal(self):
        # covers lines 195-197: both prerelease, identical
        assert StrictVersion('1.0a1') == StrictVersion('1.0a1')

    def test_cmp_both_prerelease_self_less(self):
        # covers lines 198-199: both prerelease, self < other
        assert StrictVersion('1.0a1') < StrictVersion('1.0b1')
        assert StrictVersion('1.0a1') < StrictVersion('1.0a2')

    def test_cmp_both_prerelease_self_greater(self):
        # covers lines 200-201: both prerelease, self > other
        assert StrictVersion('1.0b1') > StrictVersion('1.0a1')
        assert StrictVersion('1.0a2') > StrictVersion('1.0a1')

    def test_cmp_direct_string_equivalence(self):
        # _cmp with a string must match _cmp with an equivalent StrictVersion
        v = StrictVersion('1.0b2')
        assert v._cmp('1.0b2') == v._cmp(StrictVersion('1.0b2'))
        assert v._cmp('1.0b1') == v._cmp(StrictVersion('1.0b1'))
        assert v._cmp('1.0b3') == v._cmp(StrictVersion('1.0b3'))
