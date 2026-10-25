# file: project/f093/__init__.py:1-6
# asked: {"lines": [3, 4, 5, 6], "branches": []}
# gained: {"lines": [3, 4, 5, 6], "branches": []}

import pytest

import f093


def test_encode_lowercase_vowels_shifted_after_swapcase():
    # 'aeiou' -> swapcase 'AEIOU' -> each vowel shifted +2 -> 'CGKQW'
    assert f093.encode("aeiou") == "CGKQW"


def test_encode_uppercase_vowels_shifted_after_swapcase():
    # 'AEIOU' -> swapcase 'aeiou' -> each vowel shifted +2 -> 'cgkqw'
    assert f093.encode("AEIOU") == "cgkqw"


def test_encode_consonants_only_swapcased():
    assert f093.encode("bcdf") == "BCDF"
    assert f093.encode("BCDF") == "bcdf"


def test_encode_empty_string_returns_empty_string():
    assert f093.encode("") == ""


def test_encode_mixed_sentence():
    # 'Hello World' -> 'hELLO wORLD' -> 'hGLLQ wQRLD'
    assert f093.encode("Hello World") == "hGLLQ wQRLD"


def test_encode_leaves_non_letters_untouched():
    message = "a1b2!? \t\n"
    result = f093.encode(message)
    assert result == "C1B2!? \t\n"
    assert len(result) == len(message)


@pytest.mark.parametrize("vowel", list("aeiouAEIOU"))
def test_encode_single_vowel_matches_shift_rule(vowel):
    expected = chr(ord(vowel.swapcase()) + 2)
    result = f093.encode(vowel)
    assert result == expected
    assert len(result) == 1


@pytest.mark.parametrize(
    "message",
    ["", "a", "Z", "Hello, World!", "The quick brown fox jumps over the lazy dog", "12345"],
)
def test_encode_postconditions_length_and_swapcase_of_non_vowels(message):
    result = f093.encode(message)
    # length is always preserved
    assert len(result) == len(message)
    # non-vowel characters are exactly the swapcased originals
    vowels = "aeiouAEIOU"
    swapped = message.swapcase()
    for original, encoded in zip(swapped, result):
        if original not in vowels:
            assert encoded == original
        else:
            assert encoded == chr(ord(original) + 2)
