# file: project/f153/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}

import pytest

from f153 import Strongest_Extension


def test_later_extension_stronger_updates_strong():
    # "aA" -> 1 upper - 1 lower = 0; "AAA" -> 3 - 0 = 3 > 0, so the
    # branches at lines 7-9 (val > my_val) must fire and update `strong`.
    result = Strongest_Extension("my_class", ["aA", "AAA"])
    assert result == "my_class.AAA"


def test_first_extension_remains_strongest():
    # "AAA" -> 3; "aA" -> 0; "zz" -> -2. None of the later values exceed 3,
    # so the comparison at line 7 is False every time and `strong` stays
    # as the first extension (line 3 initialization is used).
    result = Strongest_Extension("my_class", ["AAA", "aA", "zz"])
    assert result == "my_class.AAA"


def test_tie_keeps_first_occurrence():
    # "AA" and "BB" both have strength 2; the strict `>` comparison is
    # False, so the first occurrence must be kept.
    result = Strongest_Extension("C", ["AA", "BB"])
    assert result == "C.AA"


def test_single_extension_skips_update_branch():
    # A single-element list still exercises lines 3-6, line 7 (False) and
    # the return at lines 11-12, but never the update at lines 8-9.
    result = Strongest_Extension("Single", ["Se1!"])
    assert result == "Single.Se1!"


def test_non_alpha_characters_are_ignored():
    # "S1e2!@" -> 1 upper - 1 lower = 0 (digits/punctuation ignored);
    # "AA!!"  -> 2 - 0 = 2, which is stronger, so the update branch runs
    # while verifying the comprehension filters only alphabetic chars.
    result = Strongest_Extension("X", ["S1e2!@", "AA!!"])
    assert result == "X.AA!!"


def test_class_name_is_prefixed_verbatim():
    # Exercises line 11/12 concatenation and return with a name that itself
    # contains characters whose case must not be considered.
    result = Strongest_Extension("CapuCCino", ["a"])
    assert result == "CapuCCino.a"
