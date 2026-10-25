# file: project/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [196, 197], [196, 198], [198, 199], [198, 201]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


class TestStrictVersionCmp:
    """Cover all branches of StrictVersion._cmp (lines 170-203)."""

    def test_cmp_with_string_other(self):
        # line 170-171: other is a str -> converted to StrictVersion
        result = StrictVersion('1.0')._cmp('1.0')
        assert result == 0

    def test_cmp_with_invalid_other_type_returns_not_implemented(self):
        # line 172-173: other is neither str nor StrictVersion
        result = StrictVersion('1.0')._cmp(123)
        assert result is NotImplemented

    def test_cmp_self_version_less_than_other(self):
        # line 178-179: numeric versions differ, self < other
        assert StrictVersion('1.0')._cmp(StrictVersion('2.0')) == -1

    def test_cmp_self_version_greater_than_other(self):
        # line 181: numeric versions differ, self > other
        assert StrictVersion('2.0')._cmp(StrictVersion('1.0')) == 1

    def test_cmp_equal_no_prerelease(self):
        # line 189-190: neither has prerelease -> equal
        assert StrictVersion('1.0')._cmp(StrictVersion('1.0.0')) == 0

    def test_cmp_self_prerelease_other_not(self):
        # line 191-192: self has prerelease, other doesn't -> self is lesser
        assert StrictVersion('1.0a1')._cmp(StrictVersion('1.0')) == -1

    def test_cmp_self_not_prerelease_other_prerelease(self):
        # line 193-194: other has prerelease, self doesn't -> self is greater
        assert StrictVersion('1.0')._cmp(StrictVersion('1.0a1')) == 1

    def test_cmp_both_prerelease_equal(self):
        # line 196-197: both prerelease, identical -> equal
        assert StrictVersion('1.0a1')._cmp(StrictVersion('1.0a1')) == 0

    def test_cmp_both_prerelease_self_less(self):
        # line 198-199: both prerelease, self's is smaller
        assert StrictVersion('1.0a1')._cmp(StrictVersion('1.0b1')) == -1

    def test_cmp_both_prerelease_self_greater(self):
        # line 201: both prerelease, self's is larger
        assert StrictVersion('1.0b1')._cmp(StrictVersion('1.0a1')) == 1

    def test_comparison_operators_with_string(self):
        # exercise _cmp via rich comparisons with a str operand
        assert StrictVersion('1.0') == '1.0'
        assert StrictVersion('1.0a1') < '1.0'
        assert StrictVersion('1.0') > '1.0a1'

    def test_comparison_with_unsupported_type(self):
        # NotImplemented propagates so Python raises TypeError
        with pytest.raises(TypeError):
            StrictVersion('1.0') < 123
        with pytest.raises(TypeError):
            StrictVersion('1.0') > object()
