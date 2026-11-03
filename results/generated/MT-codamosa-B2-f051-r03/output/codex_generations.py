

# Generated at 2026-11-03 01:37:11.965183
# Unit test for function remove_vowels
def test_remove_vowels():
    # Test with empty string
    assert module_0.remove_vowels("") == ""

    # Test with string containing only vowels (lowercase)
    assert module_0.remove_vowels("aaaaa") == ""
    assert module_0.remove_vowels("aeiou") == ""

    # Test with string containing only vowels (uppercase)
    assert module_0.remove_vowels("AEIOU") == ""

    # Test with mixed case vowels and consonants
    assert module_0.remove_vowels("abcdef") == "bcdf"
    assert module_0.remove_vowels("abcdefg") == "bcdfg"
    assert module_0.remove_vowels("HELLO") == "HLL"
    assert module_0.remove_vowels("Hello World") == "Hll Wrld"

    # Test with string containing no vowels
    assert module_0.remove_vowels("zbcd") == "zbcd"
    assert module_0.remove_vowels("xyz") == "xyz"

    # Test with mixed vowels and consonants
    assert module_0.remove_vowels("aaBAA") == "B"
    assert module_0.remove_vowels("Yellow") == "Yllw"

    # Test with string containing digits and punctuation
    assert module_0.remove_vowels("a1b2c3") == "1b2c3"
    assert module_0.remove_vowels("hello!") == "hll!"
    assert module_0.remove_vowels("Testing, 1-2-3!") == "Tstng, 1-2-3!"

    # Test with string containing 'y' (not treated as a vowel)
    assert module_0.remove_vowels("why") == "why"
    assert module_0.remove_vowels("rhythm") == "rhythm"

    print("All tests passed!")


test_remove_vowels()

# Generated at 2026-11-03 01:38:20.259523
# Unit test for function remove_vowels
def test_remove_vowels():
    # Basic cases
    assert module_0.remove_vowels("") == ""
    assert module_0.remove_vowels("abcdef") == "bcdf"
    assert module_0.remove_vowels("aaaaa") == ""
    assert module_0.remove_vowels("aaBAA") == "B"
    assert module_0.remove_vowels("zbcd") == "zbcd"

    # Mixed case vowels
    assert module_0.remove_vowels("AEIOUaeiou") == ""
    assert module_0.remove_vowels("Hello World") == "Hll Wrld"

    # Strings with no vowels
    assert module_0.remove_vowels("xyz") == "xyz"
    assert module_0.remove_vowels("12345!@#") == "12345!@#"

    # Strings with only vowels
    assert module_0.remove_vowels("aeiou") == ""
    assert module_0.remove_vowels("AEIOU") == ""

    # Mixed content
    assert module_0.remove_vowels("Python Programming") == "Pythn Prgrmmng"
    assert module_0.remove_vowels("The quick brown fox") == "Th qck brwn fx"

    # Special characters and spaces preserved
    assert module_0.remove_vowels("a b c") == " b c"
    assert module_0.remove_vowels("!@#a$%") == "!@#$%"

    # Unicode characters (non-vowel letters preserved)
    assert module_0.remove_vowels("café") == "cfé"

    # Single characters
    assert module_0.remove_vowels("a") == ""
    assert module_0.remove_vowels("b") == "b"

    print("All tests passed!")


test_remove_vowels()

# Generated at 2026-11-03 01:39:26.813424
# Unit test for function remove_vowels
def test_remove_vowels():
    # Empty string
    assert module_0.remove_vowels('') == ''
    # Mixed case with newline
    assert module_0.remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'
    # Simple lowercase
    assert module_0.remove_vowels('abcdef') == 'bcdf'
    # All vowels
    assert module_0.remove_vowels('aaaaa') == ''
    # Mixed case vowels
    assert module_0.remove_vowels('aaBAA') == 'B'
    # No vowels
    assert module_0.remove_vowels('zbcd') == 'zbcd'
    # Uppercase vowel removal
    assert module_0.remove_vowels('HELLO World') == 'HLL Wrld'
    # Punctuation preserved
    assert module_0.remove_vowels('Python!') == 'Pythn!'
    # All vowels both cases
    assert module_0.remove_vowels('AEIOUaeiou') == ''
    # Consonants only, mixed case
    assert module_0.remove_vowels('xyzXYZ') == 'xyzXYZ'
    # Digits and spaces preserved
    assert module_0.remove_vowels('a1b2c3 e4i5') == '1b2c3 45'

# Generated at 2026-11-03 01:41:13.943424
# Unit test for function remove_vowels
def test_remove_vowels():
    # Basic cases
    assert module_0.remove_vowels("") == ""
    assert module_0.remove_vowels("abcdef") == "bcdf"
    assert module_0.remove_vowels("aaaaa") == ""
    assert module_0.remove_vowels("aaBAA") == "B"
    assert module_0.remove_vowels("zbcd") == "zbcd"

    # Mixed case vowels
    assert module_0.remove_vowels("Hello World") == "Hll Wrld"
    assert module_0.remove_vowels("AEIOUaeiou") == ""

    # Strings with no vowels
    assert module_0.remove_vowels("xyz") == "xyz"
    assert module_0.remove_vowels("rhythm") == "rhythm"

    # Strings with spaces and punctuation
    assert module_0.remove_vowels("The quick brown fox jumps!") == "Th qck brwn fx jmps!"

    # Single characters
    assert module_0.remove_vowels("a") == ""
    assert module_0.remove_vowels("b") == "b"
    assert module_0.remove_vowels("A") == ""

    # Numbers and special characters are preserved
    assert module_0.remove_vowels("a1e2i3o4u5") == "12345"
    assert module_0.remove_vowels("!@#$%") == "!@#$%"

    # Long mixed string
    assert module_0.remove_vowels("Python Programming") == "Pythn Prgrmmng"

    print("All tests passed!")


if __name__ == "__main__":
    test_remove_vowels()

# Generated at 2026-11-03 01:43:20.497087
# Unit test for function remove_vowels
def test_remove_vowels():
    assert module_0.remove_vowels("") == ""
    assert module_0.remove_vowels("abcdef") == "bcdf"
    assert module_0.remove_vowels("aaaaa") == ""
    assert module_0.remove_vowels("aaBAA") == "B"
    assert module_0.remove_vowels("zbcd") == "zbcd"
    assert module_0.remove_vowels("abcdef\ncd") == "bcdf\ncd"
    assert module_0.remove_vowels("HELLO") == "HLL"
    assert module_0.remove_vowels("Python is fun!") == "Pythn s fn!"
    assert module_0.remove_vowels("AEIOUaeiou") == ""
    assert module_0.remove_vowels("12345!@#") == "12345!@#"
    assert module_0.remove_vowels("rhythm") == "rhythm"
    print("All tests passed!")