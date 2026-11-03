

# Generated at 2026-11-03 05:58:08.796518
# Unit test for function remove_vowels
def test_remove_vowels():
    # Empty string
    assert module_0.remove_vowels("") == "", "Empty string should return empty string"

    # String with only vowels
    assert module_0.remove_vowels("aeiou") == "", "All lowercase vowels should be removed"
    assert module_0.remove_vowels("AEIOU") == "", "All uppercase vowels should be removed"

    # String with no vowels
    assert module_0.remove_vowels("xyz") == "xyz", "No vowels should return unchanged"
    assert module_0.remove_vowels("bcdfg") == "bcdfg", "Consonants should remain"

    # Mixed case vowels
    assert module_0.remove_vowels("aEdIoUx") == "x", "Mixed case vowels should all be removed"

    # Typical sentences
    assert module_0.remove_vowels("abcdef") == "bcdf", "Only vowels removed from word"
    assert module_0.remove_vowels("Hello, World!") == "Hll, Wrld!", "Punctuation preserved"

    # Spaces, digits, special characters preserved
    assert module_0.remove_vowels("a1b2c3") == "1b23", "Digits preserved, vowels removed"
    assert module_0.remove_vowels(" ") == " ", "Spaces preserved"
    assert module_0.remove_vowels("This is a test.") == "Ths s  tst.", "Sentence case handled"

    # Repeated vowels
    assert module_0.remove_vowels("aaa") == "", "Repeated vowels removed"
    assert module_0.remove_vowels("banana") == "bnn", "'banana' -> 'bnn'"

    # Unicode / non-ASCII characters untouched
    assert module_0.remove_vowels("café") == "cf", "Non-ASCII consonant chars preserved"

    print("All test_remove_vowels tests passed!")


if __name__ == "__main__":
    test_remove_vowels()

# Generated at 2026-11-03 05:59:25.377043
# Unit test for function remove_vowels
def test_remove_vowels():
    # Test with empty string
    assert module_0.remove_vowels("") == ""

    # Test with string containing only vowels
    assert module_0.remove_vowels("abcdef\nghijklm") == "bcdf\nghjklm"

    # Test with mixed vowels and consonants
    assert module_0.remove_vowels("abcdef") == "bcdf"
    assert module_0.remove_vowels("aaaaa") == ""
    assert module_0.remove_vowels("aaBAA") == "B"
    assert module_0.remove_vowels("zbcd") == "zbcd"

    # Test with uppercase and lowercase vowels
    assert module_0.remove_vowels("AEIOUaeiou") == ""

    # Test with string containing no vowels
    assert module_0.remove_vowels("xyz") == "xyz"
    assert module_0.remove_vowels("bcdfg") == "bcdfg"

    # Test with vowels at start, middle, and end
    assert module_0.remove_vowels("apple") == "ppl"
    assert module_0.remove_vowels("orange") == "rng"

    # Test with numbers and special characters
    assert module_0.remove_vowels("h3ll0 w0rld!") == "h3ll0 w0rld!"
    assert module_0.remove_vowels("a1e2i3o4u5") == "12345"

# Generated at 2026-11-03 06:00:57.846907
# Unit test for function remove_vowels
def test_remove_vowels():
    # Basic cases with lowercase vowels
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

    # Mixed case
    assert module_0.remove_vowels("AbEcEdEf") == "bcdf"
    assert module_0.remove_vowels("Python Programming") == "Pythn Prgrmmng"

    # Vowels with punctuation, digits, and whitespace
    assert module_0.remove_vowels("Hello, World!") == "Hll, Wrld!"
    assert module_0.remove_vowels("12345") == "12345"
    assert module_0.remove_vowels("a e i o u") == "    "

    # Special characters remain untouched
    assert module_0.remove_vowels("!@#$%^&*()") == "!@#$%^&*()"

    # 'y' is not a vowel
    assert module_0.remove_vowels("why") == "why"
    assert module_0.remove_vowels("rhythm") == "rhythm"

    # Single characters
    assert module_0.remove_vowels("a") == ""
    assert module_0.remove_vowels("b") == "b"

# Generated at 2026-11-03 06:02:18.539255
# Unit test for function remove_vowels
def test_remove_vowels():
    assert module_0.remove_vowels('') == ''
    assert module_0.remove_vowels("abcdef\nghijklm") == 'bcdf\nghjklm'
    assert module_0.remove_vowels('abcdef') == 'bcdf'
    assert module_0.remove_vowels('aaaaa') == ''
    assert module_0.remove_vowels('aaBAA') == 'B'
    assert module_0.remove_vowels('zbcd') == 'zbcd'
    assert module_0.remove_vowels('Hello World') == 'Hll Wrld'
    assert module_0.remove_vowels('AEIOUaeiou') == ''
    assert module_0.remove_vowels('xyz') == 'xyz'
    assert module_0.remove_vowels('1234!@#') == '1234!@#'
    print("All tests passed!")

# Generated at 2026-11-03 06:03:30.014275
# Unit test for function remove_vowels
def test_remove_vowels():
    """Test suite for remove_vowels function."""
    
    # Test basic lowercase vowel removal
    assert module_0.remove_vowels("hello") == "hll", "Failed to remove lowercase vowels"
    assert module_0.remove_vowels("banana") == "bnn", "Failed to remove vowels from 'banana'"
    
    # Test uppercase vowel removal
    assert module_0.remove_vowels("HELLO") == "HLL", "Failed to remove uppercase vowels"
    assert module_0.remove_vowels("Apple") == "ppl", "Failed mixed case removal"
    
    # Test mixed case string
    assert module_0.remove_vowels("AbEcIdOfU") == "bcd", "Failed mixed case vowel removal"
    
    # Test string with no vowels
    assert module_0.remove_vowels("rhythm") == "rhythm", "Should not modify string without vowels"
    assert module_0.remove_vowels("xyz") == "xyz", "Should not modify string without vowels"
    
    # Test string with only vowels
    assert module_0.remove_vowels("aeiou") == "", "Failed to remove all vowels"
    assert module_0.remove_vowels("AEIOU") == "", "Failed to remove all uppercase vowels"
    assert module_0.remove_vowels("aEiOu") == "", "Failed mixed-case all-vowel string"
    
    # Test empty string
    assert module_0.remove_vowels("") == "", "Failed on empty string"
    
    # Test string with numbers and special characters
    assert module_0.remove_vowels("h3ll0 w0rld!") == "h3ll0 w0rld!", "Failed with numbers/special chars"
    assert module_0.remove_vowels("a1e2i3") == "123", "Failed mixed alnum string"
    
    # Test spaces and punctuation are preserved
    assert module_0.remove_vowels("The quick brown fox") == "Th qck brwn fx", "Failed sentence test"
    assert module_0.remove_vowels("Hello, World!") == "Hll, Wrld!", "Failed punctuation preservation"
    
    # Test repeated vowels
    assert module_0.remove_vowels("aaeeiioouu") == "", "Failed repeated vowels"
    
    # Test single characters
    assert module_0.remove_vowels("a") == "", "Failed single vowel"
    assert module_0.remove_vowels("b") == "b", "Failed single consonant"
    
    print("All tests passed!")


# Run the test
if __name__ == "__main__":
    test_remove_vowels()