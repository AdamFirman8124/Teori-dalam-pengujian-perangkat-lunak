# file: project/f153/__init__.py:1-12
# asked: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}
# gained: {"lines": [3, 4, 5, 6, 7, 8, 9, 11, 12], "branches": [[5, 6], [5, 11], [7, 5], [7, 8]]}

from f153 import Strongest_Extension


def test_first_extension_is_strongest():
    result = Strongest_Extension(
        "Slices",
        ["SErviNGSliCes", "Cheese", "StuFfed"],
    )
    assert result == "Slices.SErviNGSliCes"


def test_later_extension_replaces_initial_strongest():
    result = Strongest_Extension("my_class", ["A", "ABC", "Be"])
    assert result == "my_class.ABC"


def test_single_extension():
    result = Strongest_Extension("Cls", ["only"])
    assert result == "Cls.only"


def test_tie_keeps_first_extension():
    result = Strongest_Extension("Cls", ["AB", "CD"])
    assert result == "Cls.AB"


def test_non_alpha_characters_are_ignored():
    result = Strongest_Extension("Cls", ["a1B2!", "ZZz"])
    assert result == "Cls.ZZz"
