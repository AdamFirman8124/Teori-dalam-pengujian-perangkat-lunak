# file: project/f153/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}

"""Tests for f153.Strongest_Extension.

The function under test is pure (no I/O, no globals, no side effects),
so no monkeypatching or teardown is required to avoid state pollution.
The tests below exercise every line (3-12) and both outcomes of the
`if val > my_val` branch.
"""

from f153 import Strongest_Extension


def test_first_extension_is_strongest():
    """The first extension already has the maximal strength, so the loop
    body never reassigns `strong` (the `if val > my_val` branch is False),
    while lines 3-7 and 11-12 all execute.

    Strengths: "SErviNGSliCes" -> 6 upper - 7 lower = -1 (max),
               "Cheese"        -> 1 - 5 = -4,
               "StuFfed"       -> 2 - 5 = -3.
    """
    result = Strongest_Extension("Slices", ["SErviNGSliCes", "Cheese", "StuFfed"])
    assert result == "Slices.SErviNGSliCes"


def test_later_extension_is_strongest():
    """A later extension has a strictly greater strength, so the if-branch
    (lines 8-9) executes and both `strong` and `my_val` are reassigned.

    Strengths: "aa" -> -2, "BB" -> 2 (beats -2, branch taken),
               "Cc" -> 0 (does not beat 2).
    """
    result = Strongest_Extension("my_class", ["aa", "BB", "Cc"])
    assert result == "my_class.BB"


def test_tie_keeps_first_extension():
    """Equal strengths must not trigger the if-branch; the first wins.

    Strengths: "Ab" -> 0, "Cd" -> 0 (tie, branch not taken).
    """
    result = Strongest_Extension("X", ["Ab", "Cd"])
    assert result == "X.Ab"


def test_single_extension():
    """With a single extension the loop runs once and the branch is False,
    but lines 3-7 and 11-12 still execute.
    """
    result = Strongest_Extension("Solo", ["OnE"])
    assert result == "Solo.OnE"


def test_non_alpha_characters_are_ignored():
    """Non-alphabetic characters contribute nothing to the strength.

    Strengths: "1!2" -> 0, "A" -> 1 (beats 0, branch taken).
    """
    result = Strongest_Extension("N", ["1!2", "A"])
    assert result == "N.A"


def test_negative_strength_can_be_beaten():
    """A negative initial strength can still be beaten by a later extension.

    Strengths: "abc" -> -3, "AB" -> 2 (beats -3, branch taken).
    """
    result = Strongest_Extension("Neg", ["abc", "AB"])
    assert result == "Neg.AB"
