# file: project/f051/__init__.py:1-3
# asked: {"lines": [3], "branches": []}
# gained: {"lines": [3], "branches": []}

from f051 import remove_vowels


def test_remove_vowels_lowercase():
    assert remove_vowels("hello") == "hll"


def test_remove_vowels_uppercase():
    assert remove_vowels("HELLO") == "HLL"


def test_remove_vowels_mixed_case():
    assert remove_vowels("AeIoU") == ""


def test_remove_vowels_no_vowels():
    assert remove_vowels("xyz XYZ") == "xyz XYZ"


def test_remove_vowels_all_vowels():
    assert remove_vowels("aeiouAEIOU") == ""


def test_remove_vowels_empty_string():
    assert remove_vowels("") == ""


def test_remove_vowels_sentence():
    assert remove_vowels("Python Programming") == "Pythn Prgrmmng"


def test_remove_vowels_consonants_and_punctuation():
    assert remove_vowels("Hello, World!") == "Hll, Wrld!"
