

# Generated at 2026-11-02 11:11:30.072506
# Unit test for function select_words
def test_select_words():
    # Basic examples
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello World", 4) == ["World"]
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]

    # Empty string
    assert module_0.select_words("", 3) == []

    # No words match
    assert module_0.select_words("cat dog fish", 10) == []

    # All words match
    assert module_0.select_words("cat dog", 2) == ["cat", "dog"]

    # Zero consonants (all-vowel words)
    assert module_0.select_words("aeiou a", 0) == ["aeiou", "a"]

    # Single-character words
    assert module_0.select_words("a b c d", 1) == ["b", "c", "d"]

    # Case insensitivity: uppercase letters still count as consonants
    assert module_0.select_words("AEIOU aeiou", 0) == ["AEIOU", "aeiou"]
    assert module_0.select_words("BCDFG", 5) == ["BCDFG"]

    # Mixed case word
    assert module_0.select_words("HeLLo", 3) == ["HeLLo"]

    # n larger than any word's consonant count
    assert module_0.select_words("hello", 100) == []

    # Word order preserved
    assert module_0.select_words("world hello test", 3) == ["world", "test"]

# Generated at 2026-11-02 11:13:48.107860
# Unit test for function select_words
def test_select_words():
    # Words with exactly n consonants
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]

    # No words match the consonant count
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("simple white space", 3) == ["simple", "white", "space"]

    # Mixed-case input
    assert module_0.select_words("Hello World", 4) == ["World"]

    # Words containing only vowels with n == 0
    assert module_0.select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]

    # Uppercase vowels should be treated as vowels
    assert module_0.select_words("AEIOU aeiou", 0) == ["AEIOU", "aeiou"]

    # 'y' is counted as a consonant
    assert module_0.select_words("y", 1) == ["y"]
    assert module_0.select_words("y", 0) == []

    # Empty input string
    assert module_0.select_words("", 3) == []

    # Consonant count higher than any word's count
    assert module_0.select_words("cat dog", 10) == []

    print("All tests passed!")


if __name__ == "__main__":
    test_select_words()

# Generated at 2026-11-02 11:15:06.237429
# Unit test for function select_words
def test_select_words():
    # Basic examples
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]

    # No word matches the consonant count
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("simple white space", 3) == ["white", "space"]
    assert module_0.select_words("simple white space", 4) == ["simple"]

    # Empty string returns empty list
    assert module_0.select_words("", 5) == []

    # Single-letter words: vowels have 0 consonants
    assert module_0.select_words("a b c", 0) == ["a"]
    assert module_0.select_words("a b c", 1) == ["b", "c"]

    # 'y' is treated as a consonant
    assert module_0.select_words("yes y", 1) == ["y"]
    assert module_0.select_words("yes y", 2) == ["yes"]

    # Case-insensitive vowel checking (uppercase consonants counted)
    assert module_0.select_words("BANANA", 3) == ["BANANA"]
    assert module_0.select_words("Apple", 3) == ["Apple"]

    # No matches returns empty list
    assert module_0.select_words("hello world", 10) == []

    # Order of appearance is preserved
    assert module_0.select_words("cat dog bird", 2) == ["cat", "dog"]

# Generated at 2026-11-02 11:17:53.150459
# Unit test for function select_words
def test_select_words():
    # Basic examples
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello World", 4) == ["World"]
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]

    # Empty string
    assert module_0.select_words("", 3) == []
    assert module_0.select_words("", 0) == []

    # Single word matches / non-matches
    assert module_0.select_words("hello", 3) == ["hello"]
    assert module_0.select_words("hello", 4) == []
    assert module_0.select_words("world", 4) == ["world"]

    # Vowel detection is case-insensitive (uppercase vowels not counted)
    assert module_0.select_words("Apple", 3) == ["Apple"]
    assert module_0.select_words("APPLE", 3) == ["APPLE"]
    assert module_0.select_words("bAnAnA", 3) == ["bAnAnA"]

    # 'y' is not in the vowel list, so it counts as a consonant
    assert module_0.select_words("yummy", 4) == ["yummy"]
    assert module_0.select_words("sky", 3) == ["sky"]

    # n = 0 matches words with no consonants
    assert module_0.select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]

    # No matches when n is larger than any word's consonant count
    assert module_0.select_words("cat dog fish", 10) == []

    # Multiple matches preserve original order
    assert module_0.select_words("test best", 3) == ["test", "best"]
    assert module_0.select_words("string", 5) == ["string"]
    assert module_0.select_words("string", 3) == []

    print("All tests passed!")


if __name__ == "__main__":
    test_select_words()

# Generated at 2026-11-02 11:19:16.851093
# Unit test for function select_words
def test_select_words():
    # Basic functionality
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello world", 4) == ["world"]
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]

    # Empty string input
    assert module_0.select_words("", 4) == []
    assert module_0.select_words("", 0) == []

    # Words with no consonants
    assert module_0.select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]
    assert module_0.select_words("a e i o u", 1) == []

    # Case insensitivity for vowels
    assert module_0.select_words("AEIOU bcd", 3) == ["bcd"]
    assert module_0.select_words("AEIOU", 0) == ["AEIOU"]

    # 'y' is treated as a consonant
    assert module_0.select_words("y", 1) == ["y"]
    assert module_0.select_words("Mary", 3) == ["Mary"]

    # n larger than any word's consonant count
    assert module_0.select_words("cat dog", 10) == []

    # Multiple matching words preserve original order
    assert module_0.select_words("test best rest", 3) == ["test", "best", "rest"]

    # Single word input
    assert module_0.select_words("world", 4) == ["world"]
    assert module_0.select_words("world", 3) == []

    # No matches at all
    assert module_0.select_words("a a a", 2) == []

    print("All tests passed!")


# nonce:2ba817ed