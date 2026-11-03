# file: project/f153/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}

import pytest

from f153 import Strongest_Extension


def test_first_extension_strongest_no_update_branch():
    """Later extensions never exceed the first one's strength,
    so the 'val > my_val' branch is always False (lines 3-7, 11-12)."""
    result = Strongest_Extension("MyClass", ["AA", "Aa", "aa"])
    # Strengths: "AA" -> 2 - 0 = 2, "Aa" -> 1 - 1 = 0, "aa" -> 0 - 2 = -2
    assert result == "MyClass.AA"


def test_tie_keeps_first_extension():
    """A tie must NOT replace the current strongest (strict '>' comparison)."""
    result = Strongest_Extension("my_class", ["CC", "Be", "DD"])
    # Strengths: "CC" -> 2, "Be" -> 0, "DD" -> 2 (tie, no update)
    assert result == "my_class.CC"


def test_update_branch_taken_once():
    """A later, stronger extension replaces the current one (lines 8-9)."""
    result = Strongest_Extension("My_class", ["Slices", "SErviNGSliCes", "SErviSnlgs"])
    # Strengths: "Slices" -> 1 - 5 = -4,
    #            "SErviNGSliCes" -> 6 - 7 = -1  (update happens here)
    #            "SErviSnlgs"    -> 4 - 5 = -1  (tie, no update)
    assert result == "My_class.SErviNGSliCes"


def test_update_branch_multiple_times_and_skips():
    """Both branches of the loop are exercised: updates on 2nd and 4th items,
    no update on 1st (== initial) and 3rd (weaker) items."""
    result = Strongest_Extension("Cls", ["B", "AA", "a", "CCC", "C"])
    # Strengths: "B" -> 1 (initial), "AA" -> 2 (update), "a" -> -1 (no update),
    #            "CCC" -> 3 (update), "C" -> 1 (no update)
    assert result == "Cls.CCC"


def test_single_extension_loop_runs_once():
    """Single-element list: loop body runs once, branch is False (val == my_val)."""
    result = Strongest_Extension("Solo", ["OnE"])
    # Strength: "OnE" -> 2 - 1 = 1
    assert result == "Solo.OnE"


def test_non_alpha_characters_ignored():
    """Non-alphabetic characters do not affect the strength computation."""
    result = Strongest_Extension("Num", ["123", "a!B?1"])
    # Strengths: "123" -> 0, "a!B?1" -> 1 - 1 = 0 (tie, no update)
    assert result == "Num.123"
