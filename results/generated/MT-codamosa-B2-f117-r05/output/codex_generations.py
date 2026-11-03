

# Generated at 2026-11-01 23:52:37.665970
# Unit test for function select_words
def test_select_words():
    # Example cases
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello world", 4) == ["world"]

    # Empty string returns empty list
    assert module_0.select_words("", 3) == []

    # No word matches the consonant count
    assert module_0.select_words("cat dog fish", 10) == []

    # n = 0 selects words made only of vowels
    assert module_0.select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]

    # Vowel check is case-insensitive
    assert module_0.select_words("AEI bcd", 0) == ["AEI"]
    assert module_0.select_words("AEI bcd", 3) == ["bcd"]

    # 'y' is treated as a consonant
    assert module_0.select_words("yay", 2) == ["yay"]

    # Multiple words can match
    assert module_0.select_words("test best rest", 3) == ["test", "best", "rest"]

    # Original word order and casing are preserved
    assert module_0.select_words("bbb aaa ccc", 3) == ["bbb", "ccc"]

    # Single-word sentence
    assert module_0.select_words("hello", 3) == ["hello"]

    # Non-letter characters count as consonants
    assert module_0.select_words("a1b", 2) == ["a1b"]

    print("All select_words tests passed!")


if __name__ == "__main__":
    test_select_words()

# Generated at 2026-11-01 23:54:38.449333
# Unit test for function select_words
def test_select_words():
    # Basic cases
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("simple white space", 3) == ["white", "space"]
    assert module_0.select_words("Hello World", 4) == ["World"]
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]

    # Edge cases
    assert module_0.select_words("", 3) == []          # empty string
    assert module_0.select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]  # no consonants

    # Case insensitivity
    assert module_0.select_words("APPLE banana ORANGE kiwi", 3) == ["kiwi"]
    assert module_0.select_words("APPLE", 3) == ["APPLE"]

    # Single word / single letter
    assert module_0.select_words("b", 1) == ["b"]
    assert module_0.select_words("x", 0) == []

    # All words match
    assert module_0.select_words("cat dog", 2) == ["cat", "dog"]

    # No matches
    assert module_0.select_words("aa bb cc", 5) == []

    print("All tests passed!")


if __name__ == "__main__":
    test_select_words()

# Generated at 2026-11-01 23:56:15.528914
# Unit test for function select_words
def test_select_words():
    # Test basic cases
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == ["simple", "white"]
    assert module_0.select_words("simple white space", 3) == []
    
    # Test no matches
    assert module_0.select_words("a b c d", 0) == ["a", "b", "c", "d"]
    assert module_0.select_words("hello world", 10) == []
    
    # Test empty string
    assert module_0.select_words("", 0) == []
    assert module_0.select_words("", 3) == []
    
    # Test single word
    assert module_0.select_words("hello", 3) == ["hello"]
    assert module_0.select_words("hello", 4) == []
    
    # Test case insensitivity (mixed case words)
    assert module_0.select_words("Mary Had A Little Lamb", 4) == ["Little"]
    assert module_0.select_words("MARY HAD A LITTLE LAMB", 3) == ["MARY", "LAMB"]
    
    # Test words with punctuation attached (treated as consonants)
    assert module_0.select_words("hello, world!", 3) == ["hello,", "world!"]
    
    # Test multiple spaces
    assert module_0.select_words("hello   world", 3) == ["hello", "world"]
    
    # Test all vowels (0 consonants)
    assert module_0.select_words("aeiou", 0) == ["aeiou"]
    assert module_0.select_words("aeiou", 1) == []
    
    # Test counting 'y' as consonant (not in vowel list)
    assert module_0.select_words("yellow sky", 4) == ["yellow", "sky"]
    
    # Test exact consonant counts
    assert module_0.select_words("cat dog bird", 2) == ["cat", "dog"]
    assert module_0.select_words("rhythm", 6) == ["rhythm"]
    
    print("All tests passed!")


# Run tests
test_select_words()

# Generated at 2026-11-01 23:57:36.331221
# Unit test for function select_words
def test_select_words():
    # Basic examples
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 2) == ["had"]

    # No matches
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("simple white space", 5) == []

    # Multiple matches preserve order
    assert module_0.select_words("simple white space", 3) == ["white", "space"]
    assert module_0.select_words("simple white space", 4) == ["simple"]

    # Empty string
    assert module_0.select_words("", 0) == []
    assert module_0.select_words("", 1) == []

    # Words with zero consonants
    assert module_0.select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]

    # Case insensitivity: uppercase vowels are not counted as consonants
    assert module_0.select_words("Apple APPLE", 3) == ["Apple", "APPLE"]

    # 'y' is treated as a consonant
    assert module_0.select_words("why sky try", 3) == ["why", "sky", "try"]

    # Mixed-case consonants are counted
    assert module_0.select_words("Hello World", 3) == ["Hello"]
    assert module_0.select_words("Hello World", 4) == ["World"]

    # Non-letter characters count as consonants
    assert module_0.select_words("hi!", 2) == ["hi!"]

    print("All tests passed!")

# Generated at 2026-11-01 23:58:00.758223
# Unit test for function select_words
def test_select_words():
    # Test with a typical sentence, n=4
    assert module_0.select_words("Mary had a little lamb", 4) == ["little", "lamb"]
    
    # Test with n=3
    assert module_0.select_words("simple little space", 3) == ["simple", "space", "little"]
    
    # Test with n=5 (no words match)
    assert module_0.select_words("simple little space", 5) == []
    
    # Test with empty string
    assert module_0.select_words("", 4) == []
    
    # Test with single word matching
    assert module_0.select_words("hello", 3) == ["hello"]
    
    # Test with single word not matching
    assert module_0.select_words("world", 2) == []
    
    # Test with uppercase letters (case insensitive consonant check)
    assert module_0.select_words("Apple", 3) == ["Apple"]
    assert module_0.select_words("APPLE BANANA", 3) == ["APPLE"]
    
    # Test with all vowels
    assert module_0.select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]
    
    # Test with punctuation attached to words
    assert module_0.select_words("Mary, had a little lamb!", 4) == ["Mary,", "little", "lamb!"]
    
    # Test with n=0 (words with no consonants)
    assert module_0.select_words("aa bb cc", 0) == ["aa"]
    
    # Test with multiple spaces between words
    assert module_0.select_words("hello   world", 3) == ["hello", "world"]
    
    # Test with numbers/digits in words (digits count as consonants)
    assert module_0.select_words("a1b2", 4) == ["a1b2"]
    
    print("All tests passed!")


test_select_words()