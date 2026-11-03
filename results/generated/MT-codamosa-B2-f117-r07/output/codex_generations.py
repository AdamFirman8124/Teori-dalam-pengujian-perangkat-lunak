

# Generated at 2026-11-02 18:28:08.452819
# Unit test for function select_words
def test_select_words():
    # Basic test cases
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello World", 4) == ["World"]
    assert module_0.select_words("Uncle Sam", 3) == ["Uncle"]

    # No words match
    assert module_0.select_words("one two three", 10) == []

    # Empty string
    assert module_0.select_words("", 3) == []

    # n = 0 should match words with no consonants (vowel-only words)
    assert module_0.select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]

    # Case insensitivity check
    assert module_0.select_words("MARY HAD A LITTLE LAMB", 3) == ["MARY", "LAMB"]

    # 'y' is treated as a consonant
    assert module_0.select_words("y shy try", 1) == ["y", "shy", "try"]

    # Punctuation counts as consonants in this implementation
    assert module_0.select_words("hello!", 6) == ["hello!"]

    # Single word string
    assert module_0.select_words("world", 5) == ["world"]

    # Multiple matches preserving order
    assert module_0.select_words("cat dog bird fish", 3) == ["cat", "dog", "bird", "fish"]

    # Whole sentence with mixed lengths
    assert module_0.select_words("the quick brown fox jumps", 3) == ["the", "fox", "jumps"]

# Generated at 2026-11-02 18:30:45.440594
# Unit test for function select_words
def test_select_words():
    # Words with exactly n consonants are selected
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello world", 4) == ["world"]

    # No matches
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]
    assert module_0.select_words("a b c", 1) == ["b", "c"]

    # Empty string
    assert module_0.select_words("", 4) == []

    # Zero consonants (all vowels)
    assert module_0.select_words("aa aa", 0) == ["aa", "aa"]

    # Mixed case handling (vowels checked lowercased)
    assert module_0.select_words("Apple BEE", 3) == ["Apple", "BEE"]

    # Single word input
    assert module_0.select_words("world", 4) == ["world"]

    print("All tests passed!")


if __name__ == "__main__":
    test_select_words()

# Generated at 2026-11-02 18:33:35.600510
# Unit test for function select_words
def test_select_words():
    # Basic test cases
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello world", 4) == ["world"]
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]

    # Edge cases
    assert module_0.select_words("", 4) == []
    assert module_0.select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]
    assert module_0.select_words("hello", 10) == []
    assert module_0.select_words("bcdfg", 5) == ["bcdfg"]

    # Case insensitivity: uppercase vowels should not count as consonants
    assert module_0.select_words("AEIOU bcd", 3) == ["bcd"]
    assert module_0.select_words("MARY", 3) == ["MARY"]

    # Order preservation and partial matching
    assert module_0.select_words("cat dog bird fish", 2) == ["cat", "dog"]
    assert module_0.select_words("one two three four five", 2) == ["two", "four"]

    print("All tests passed!")


test_select_words()

# Generated at 2026-11-02 18:35:42.510792
# Unit test for function select_words
def test_select_words():
    # Basic cases from known behavior
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello World", 4) == ["World"]
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]

    # Case-insensitivity of vowel check
    assert module_0.select_words("UPPER lower", 3) == ["UPPER", "lower"]

    # Empty input string returns empty list
    assert module_0.select_words("", 4) == []

    # Words with zero consonants (all vowels)
    assert module_0.select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]

    # 'y' is treated as a consonant
    assert module_0.select_words("rhythm", 6) == ["rhythm"]

    # No words match the consonant count
    assert module_0.select_words("cat dog", 5) == []

    # Single word input that matches
    assert module_0.select_words("world", 4) == ["world"]

    # All words match the consonant count
    assert module_0.select_words("hi to", 1) == ["hi", "to"]