

# Generated at 2026-11-02 11:27:06.659291
# Unit test for function remove_vowels
def test_remove_vowels():
    # Basic cases
    assert module_0.remove_vowels("") == ""
    assert module_0.remove_vowels("abcdef") == "bcdf"
    assert module_0.remove_vowels("aaaaa") == ""
    assert module_0.remove_vowels("aaBAA") == "B"
    assert module_0.remove_vowels("zbcd") == "zbcd"

    # Uppercase vowels should also be removed
    assert module_0.remove_vowels("AEIOU") == ""
    assert module_0.remove_vowels("aeiou") == ""
    assert module_0.remove_vowels("HELLO") == "HLL"
    assert module_0.remove_vowels("hello") == "hll"

    # Mixed content
    assert module_0.remove_vowels("Hello, World!") == "Hll, Wrld!"
    assert module_0.remove_vowels("Python 3.9 is gr8!") == "Pythn 3.9 s gr8!"
    assert module_0.remove_vowels("12345!@#$%") == "12345!@#$%"

    # Vowels at edges
    assert module_0.remove_vowels("apple") == "ppl"
    assert module_0.remove_vowels("orange") == "rng"
    assert module_0.remove_vowels("umbrella") == "mbrll"

    # 'y' is not a vowel
    assert module_0.remove_vowels("rhythm") == "rhythm"
    assert module_0.remove_vowels("why") == "why"

    # Spaces preserved
    assert module_0.remove_vowels("a b c d e") == "  b c d "

    print("All tests passed!")


if __name__ == "__main__":
    test_remove_vowels()

# Generated at 2026-11-02 11:29:47.996496
# Unit test for function remove_vowels
def test_remove_vowels():
# nonce:4dc427ca
    # Empty string returns empty string
    assert module_0.remove_vowels('') == ''

    # Lowercase vowels removed
    assert module_0.remove_vowels('abcdef') == 'bcdf'

    # Uppercase vowels removed (case-insensitive)
    assert module_0.remove_vowels('AEIOU') == ''
    assert module_0.remove_vowels('aaBAA') == 'B'
    assert module_0.remove_vowels('acBAA') == 'cB'

    # No vowels present, string unchanged
    assert module_0.remove_vowels('zbcd') == 'zbcd'
    assert module_0.remove_vowels('12345!@#') == '12345!@#'

    # Only vowels, result is empty
    assert module_0.remove_vowels('aaaaa') == ''
    assert module_0.remove_vowels('eeeee') == ''

    # Newlines and whitespace are preserved
    assert module_0.remove_vowels('abcdef\nghijklm') == 'bcdf\nghjklm'

    # Punctuation and spaces preserved
    assert module_0.remove_vowels('Hello, World!') == 'Hll, Wrld!'

    # Mixed content
    assert module_0.remove_vowels('PyThOn 3.9') == 'PyThn 3.9'

    print("All tests passed!")

# Generated at 2026-11-02 11:32:31.229858
# Unit test for function remove_vowels
def test_remove_vowels():
    # nonce:e42824ba
    # Empty string
    assert module_0.remove_vowels("") == ""
    # Basic lowercase vowels
    assert module_0.remove_vowels("abcdef") == "bcdf"
    # Only vowels
    assert module_0.remove_vowels("aaaaa") == ""
    # Mixed case vowels
    assert module_0.remove_vowels("aaBAA") == "B"
    # No vowels at all
    assert module_0.remove_vowels("zbcd") == "zbcd"
    # Uppercase vowels removed too
    assert module_0.remove_vowels("HELLO World") == "HLL Wrld"
    # Digits and punctuation preserved
    assert module_0.remove_vowels("Python 3.8!") == "Pythn 3.8!"
    # All vowels, both cases
    assert module_0.remove_vowels("AEIOUaeiou") == ""
    # Sentence example
    assert module_0.remove_vowels("The quick brown fox") == "Th qck brwn fx"