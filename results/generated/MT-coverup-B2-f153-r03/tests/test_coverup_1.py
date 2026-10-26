# file: project/f153/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}

from f153 import Strongest_Extension


def test_single_extension_no_update():
    assert Strongest_Extension("C", ["Ab"]) == "C.Ab"


def test_updates_to_stronger_later():
    # "aa" -> -2, "AA" -> 2, so second wins and covers val > my_val True
    assert Strongest_Extension("my_class", ["aa", "AA"]) == "my_class.AA"


def test_keeps_first_when_later_weaker():
    # "AA" -> 2 stays strongest; later "aa" -> -2 covers val > my_val False
    assert Strongest_Extension("K", ["AA", "aa"]) == "K.AA"


def test_non_alpha_and_mixed_characters():
    # "A1!" -> 1, "a1!" -> -1, "123" -> 0, covers isalpha False branches
    assert Strongest_Extension("Cls", ["A1!", "a1!", "123", "!!!"]) == "Cls.A1!"
    # "ab" -> -2, "A1b2" -> 0, covers update with non-alpha chars present
    assert Strongest_Extension("Cls", ["ab", "A1b2"]) == "Cls.A1b2"
    # tie keeps first: both -> 0
    assert Strongest_Extension("Cls", ["A1b2", "aB1"]) == "Cls.A1b2"
