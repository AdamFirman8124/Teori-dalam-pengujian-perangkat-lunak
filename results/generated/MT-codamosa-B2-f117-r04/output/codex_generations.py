

# Generated at 2026-11-02 18:47:45.035165
# Unit test for function select_words
def test_select_words():
    # Basic cases
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello World", 4) == ["World"]
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]

    # Empty string
    assert module_0.select_words("", 0) == []
    assert module_0.select_words("", 3) == []

    # Words with zero consonants (all vowels)
    assert module_0.select_words("a b c d", 0) == ["a", "b", "c", "d"]
    assert module_0.select_words("AEIOU", 0) == ["AEIOU"]
    assert module_0.select_words("aeiou xyz", 0) == ["aeiou"]

    # Case insensitivity of vowels
    assert module_0.select_words("bcd", 3) == ["bcd"]
    assert module_0.select_words("BCDF", 4) == ["BCDF"]
    assert module_0.select_words("Hello", 3) == ["Hello"]

    # No matches
    assert module_0.select_words("cat dog bird", 10) == []
    assert module_0.select_words("one two three", 0) == []

    # Punctuation is counted as a consonant by implementation
    assert module_0.select_words("Mary, had a little lamb.", 4) == ["Mary,", "little", "lamb."]

    # Multiple words matching
    assert module_0.select_words("bbb ccc ddd", 3) == ["bbb", "ccc", "ddd"]

    print("All tests passed!")


test_select_words()

# Generated at 2026-11-02 18:49:23.134395
# Unit test for function select_words
def test_select_words():
    # Test with typical examples
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == ["simple", "white", "space"]
    assert module_0.select_words("Hello world", 4) == ["world"]
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]

    # Test with n = 0 (words that are all vowels)
    assert module_0.select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]

    # Test with empty string
    assert module_0.select_words("", 3) == []
    assert module_0.select_words("", 0) == []

    # Test with no matching words
    assert module_0.select_words("hello world", 100) == []

    # Test case insensitivity of vowels
    assert module_0.select_words("AEI BCD", 3) == ["BCD"]
    assert module_0.select_words("AEIOU xyz", 3) == ["xyz"]

    # Test uppercase and lowercase mixed
    assert module_0.select_words("AbCdEfG", 4) == ["AbCdEfG"]

    # Test punctuation counts as consonant (not in vowel list)
    assert module_0.select_words("hello!", 5) == ["hello!"]
    assert module_0.select_words("a.b", 2) == ["a.b"]

    # Test numbers count as consonants
    assert module_0.select_words("abc123", 6) == ["abc123"]

    # Test single character words
    assert module_0.select_words("a b c d", 1) == ["b", "c", "d"]

    # Test multiple spaces between words
    assert module_0.select_words("  hello   world  ", 3) == ["hello", "world"]

    # Test result order follows input order
    assert module_0.select_words("lamb Mary little", 3) == ["lamb", "Mary"]

    # Test words with repeated vowels
    assert module_0.select_words("aaa bbb", 3) == ["bbb"]

    # Test n larger than any word length
    assert module_0.select_words("cat dog", 10) == []

    # Test 'y' is treated as consonant
    assert module_0.select_words("why", 3) == ["why"]

    print("All tests passed!")


if __name__ == "__main__":
    test_select_words()

# Generated at 2026-11-02 18:50:24.649769
# Unit test for function select_words
def test_select_words():
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("simple little space", 4) == ["simple", "little"]
    assert module_0.select_words("world", 4) == ["world"]
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]
    assert module_0.select_words("", 4) == []
    assert module_0.select_words("a a a a", 0) == ["a", "a", "a", "a"]

# Generated at 2026-11-02 18:52:31.273443
# Unit test for function select_words
def test_select_words():
    # Basic cases
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("Hello world", 4) == ["world"]
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]
    assert module_0.select_words("a b c d e f", 1) == ["b", "c", "d", "f"]

    # No matching words
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("a b c d", 5) == []

    # Empty string
    assert module_0.select_words("", 0) == []
    assert module_0.select_words("", 4) == []

    # Zero consonants (vowel-only words, vowel check is case-insensitive)
    assert module_0.select_words("a e I O u", 0) == ["a", "e", "I", "O", "u"]
    assert module_0.select_words("AEIOU", 0) == ["AEIOU"]

    # Uppercase consonants are counted
    assert module_0.select_words("BCDF", 4) == ["BCDF"]

    # Non-letter characters (punctuation/digits) count as consonants
    assert module_0.select_words("hello, world!", 4) == ["hello,"]
    assert module_0.select_words("abc123", 5) == ["abc123"]

    # Word containing 'y' (not treated as a vowel)
    assert module_0.select_words("rhythm", 6) == ["rhythm"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]

# Generated at 2026-11-02 18:54:10.910359
# Unit test for function select_words
def test_select_words():
    # Basic examples
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]

    # No matching words
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("hello world", 1) == []

    # Multiple matches preserve order
    assert module_0.select_words("simple white space", 3) == ["white", "space"]
    assert module_0.select_words("bbb aaa ccc", 3) == ["bbb", "ccc"]

    # Empty string returns empty list
    assert module_0.select_words("", 5) == []

    # Words with zero consonants
    assert module_0.select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]

    # Case insensitivity (uses .lower())
    assert module_0.select_words("UNCLE Sam", 3) == ["UNCLE"]
    assert module_0.select_words("HeLLo WoRLd", 3) == ["HeLLo"]

    # Single word input
    assert module_0.select_words("hello", 3) == ["hello"]
    assert module_0.select_words("hello", 5) == []

    # Extra whitespace is handled by split()
    assert module_0.select_words("  Mary   had  a  little   lamb ", 4) == ["little"]

    # n larger than any word's consonant count
    assert module_0.select_words("cat dog", 10) == []

    print("All tests passed!")


if __name__ == "__main__":
    test_select_words()