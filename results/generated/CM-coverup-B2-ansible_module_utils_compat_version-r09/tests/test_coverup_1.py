# file: project/ansible/module_utils/compat/version.py:169-203
# asked: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}
# gained: {"lines": [170, 171, 172, 173, 175, 178, 179, 181, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 201, 203], "branches": [[170, 171], [170, 172], [172, 173], [172, 175], [175, 178], [175, 189], [178, 179], [178, 181], [189, 190], [189, 191], [191, 192], [191, 193], [193, 194], [193, 195], [195, 196], [195, 203], [196, 197], [196, 198], [198, 199], [198, 201]]}

"""Coverage tests for StrictVersion._cmp (ansible/module_utils/compat/version.py, lines 170-203)."""

import pytest

from ansible.module_utils.compat.version import StrictVersion


def test_cmp_coerces_string_operand():
    """Lines 170-171: a str operand is converted into a StrictVersion."""
    assert StrictVersion("1.0") == "1.0"
    assert StrictVersion("1.0") == "1.0.0"
    assert not (StrictVersion("1.0") == "2.0")


def test_cmp_non_version_non_str_returns_not_implemented():
    """Lines 172-173: operands that are neither str nor StrictVersion give NotImplemented."""
    v = StrictVersion("1.0")
    assert v._cmp(object()) is NotImplemented
    assert v._cmp(42) is NotImplemented
    assert v._cmp(None) is NotImplemented
    # Rich comparison raises TypeError once both sides return NotImplemented.
    with pytest.raises(TypeError):
        v < 42


def test_cmp_numeric_less_than():
    """Lines 175, 178-179: self.version < other.version -> -1."""
    assert StrictVersion("1.0")._cmp(StrictVersion("2.0")) == -1
    assert StrictVersion("1.0") < StrictVersion("1.0.1")
    assert StrictVersion("1.0") <= StrictVersion("2.0")


def test_cmp_numeric_greater_than():
    """Lines 175, 180-181: self.version > other.version -> 1."""
    assert StrictVersion("2.0")._cmp(StrictVersion("1.0")) == 1
    assert StrictVersion("1.0.1") > StrictVersion("1.0")
    assert StrictVersion("2.0") >= StrictVersion("1.0")


def test_cmp_no_prerelease_equal():
    """Lines 189-190: neither side has a prerelease -> 0."""
    assert StrictVersion("1.0")._cmp(StrictVersion("1.0.0")) == 0
    assert StrictVersion("1.0") == StrictVersion("1.0.0")


def test_cmp_self_prerelease_other_plain():
    """Lines 191-192: self has a prerelease, other does not -> -1."""
    assert StrictVersion("1.0a1")._cmp(StrictVersion("1.0")) == -1
    assert StrictVersion("1.0a1") < StrictVersion("1.0")
    assert StrictVersion("1.0b2") <= StrictVersion("1.0")


def test_cmp_self_plain_other_prerelease():
    """Lines 193-194: other has a prerelease, self does not -> 1."""
    assert StrictVersion("1.0")._cmp(StrictVersion("1.0b2")) == 1
    assert StrictVersion("1.0") > StrictVersion("1.0b2")
    assert StrictVersion("1.0") >= StrictVersion("1.0a1")


def test_cmp_both_same_prerelease():
    """Lines 195-197: identical prereleases -> 0."""
    assert StrictVersion("1.0a1")._cmp(StrictVersion("1.0a1")) == 0
    assert StrictVersion("1.0b3") == StrictVersion("1.0b3")


def test_cmp_both_prerelease_self_lower():
    """Lines 195, 198-199: self's prerelease sorts before other's -> -1."""
    assert StrictVersion("1.0a1")._cmp(StrictVersion("1.0b1")) == -1
    assert StrictVersion("1.0a1") < StrictVersion("1.0b1")
    assert StrictVersion("1.0a1")._cmp(StrictVersion("1.0a2")) == -1
    assert StrictVersion("1.0a1") < StrictVersion("1.0a2")


def test_cmp_both_prerelease_self_higher():
    """Lines 195, 200-201: self's prerelease sorts after other's -> 1."""
    assert StrictVersion("1.0b2")._cmp(StrictVersion("1.0a1")) == 1
    assert StrictVersion("1.0b2") > StrictVersion("1.0a1")
    assert StrictVersion("1.0a2")._cmp(StrictVersion("1.0a1")) == 1
    assert StrictVersion("1.0a2") > StrictVersion("1.0a1")


def test_cmp_string_operands_exercise_all_branches():
    """Line 171 coercion feeding every downstream branch via str operands."""
    assert StrictVersion("1.0") < "2.0"        # 178-179
    assert StrictVersion("2.0") > "1.0"        # 180-181
    assert StrictVersion("1.0") == "1.0.0"     # 189-190
    assert StrictVersion("1.0a1") < "1.0"      # 191-192
    assert StrictVersion("1.0") > "1.0b2"      # 193-194
    assert StrictVersion("1.0a1") == "1.0a1"   # 195-197
    assert StrictVersion("1.0a1") < "1.0b1"    # 198-199
    assert StrictVersion("1.0b2") > "1.0a1"    # 200-201


def test_cmp_defensive_else_raises_assertion_error():
    """Lines 202-203: the defensive else clause.

    A prerelease attribute whose truthiness flips on every read makes all four
    prerelease branches evaluate false, forcing execution of the final else.
    The helper class is defined locally so no global state is polluted.
    """

    class FlippyPrerelease(StrictVersion):
        def __init__(self, vstring=None):
            super().__init__(vstring)
            self._flip = False

        @property
        def prerelease(self):
            self._flip = not self._flip
            return self._flip

        @prerelease.setter
        def prerelease(self, value):
            # Absorb the assignment performed by parse() during __init__.
            self._assigned = value

    flippy = FlippyPrerelease("1.0")
    plain = StrictVersion("1.0")

    # Sanity: numeric parts match so _cmp reaches the prerelease ladder.
    assert flippy.version == plain.version == (1, 0, 0)

    with pytest.raises(AssertionError, match="never get here"):
        flippy._cmp(plain)
