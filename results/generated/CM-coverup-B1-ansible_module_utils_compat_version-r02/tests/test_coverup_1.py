# file: project/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [196, 197], [196, 198], [198, 199], [198, 201]]}

import pytest

from ansible.module_utils.compat.version import StrictVersion


class TestStrictVersionCmp:
    """Cover all branches of StrictVersion._cmp (lines 170-201).

    Note: line 203 (the final ``raise AssertionError``) is unreachable
    dead code: the preceding ``elif self.prerelease and other.prerelease``
    is exhaustive over the remaining cases, so no input can reach the
    trailing ``else``.
    """

    # --- string coercion (lines 170-171) ---
    def test_cmp_with_string_other(self):
        assert StrictVersion('1.0') < '1.1'
        assert StrictVersion('1.1') > '1.0'
        assert StrictVersion('1.0') == '1.0'

    # --- NotImplemented for unsupported types (lines 172-173) ---
    def test_cmp_with_unsupported_type_returns_not_implemented(self):
        assert StrictVersion('1.0')._cmp(42) is NotImplemented
        assert StrictVersion('1.0')._cmp(3.14) is NotImplemented
        assert StrictVersion('1.0')._cmp(None) is NotImplemented
        # __eq__ propagates NotImplemented -> Python falls back to
        # identity comparison, which is False (no exception).
        assert (StrictVersion('1.0') == 42) is False
        # __lt__ propagates NotImplemented and int has no matching
        # reflected operator -> Python raises TypeError.
        with pytest.raises(TypeError):
            StrictVersion('1.0') < 42

    # --- numeric version comparison (lines 175-181) ---
    def test_numeric_less_than(self):
        assert StrictVersion('1.0')._cmp(StrictVersion('2.0')) == -1
        assert StrictVersion('1.0') < StrictVersion('1.0.1')

    def test_numeric_greater_than(self):
        assert StrictVersion('2.0')._cmp(StrictVersion('1.0')) == 1
        assert StrictVersion('1.0.1') > StrictVersion('1.0')

    # --- prerelease case 1: neither has prerelease (lines 189-190) ---
    def test_equal_no_prerelease(self):
        assert StrictVersion('1.0')._cmp(StrictVersion('1.0')) == 0
        # 1.0 and 1.0.0 are equivalent
        assert StrictVersion('1.0') == StrictVersion('1.0.0')

    # --- prerelease case 2: self has prerelease, other doesn't (191-192) ---
    def test_prerelease_less_than_release(self):
        assert StrictVersion('1.0a1')._cmp(StrictVersion('1.0')) == -1
        assert StrictVersion('1.0b2') < StrictVersion('1.0')

    # --- prerelease case 3: self has no prerelease, other does (193-194) ---
    def test_release_greater_than_prerelease(self):
        assert StrictVersion('1.0')._cmp(StrictVersion('1.0a1')) == 1
        assert StrictVersion('1.0') > StrictVersion('1.0b1')

    # --- prerelease case 4: both have prerelease (195-201) ---
    def test_both_prerelease_equal(self):
        assert StrictVersion('1.0a1')._cmp(StrictVersion('1.0a1')) == 0
        assert StrictVersion('1.0a1') == StrictVersion('1.0a1')

    def test_both_prerelease_self_lesser(self):
        assert StrictVersion('1.0a1')._cmp(StrictVersion('1.0b1')) == -1
        assert StrictVersion('1.0a1') < StrictVersion('1.0a2')

    def test_both_prerelease_self_greater(self):
        assert StrictVersion('1.0b1')._cmp(StrictVersion('1.0a1')) == 1
        assert StrictVersion('1.0a2') > StrictVersion('1.0a1')

    # --- string coercion combined with prerelease branches ---
    def test_string_other_with_prerelease(self):
        assert StrictVersion('1.0a1') < '1.0'
        assert StrictVersion('1.0') > '1.0a1'
        assert StrictVersion('1.0a1') == '1.0a1'
