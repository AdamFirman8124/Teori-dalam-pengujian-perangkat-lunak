

# Generated at 2026-11-02 14:35:14.828592
# Unit test for function select_words
def test_select_words():
    # Basic cases
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello world", 4) == ["world"]

    # Case insensitivity: vowels are checked in lowercase
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]
    assert module_0.select_words("APPLE banana Orange", 3) == ["APPLE", "banana", "Orange"]

    # n = 0: words containing only vowels
    assert module_0.select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]
    assert module_0.select_words("AEIOU xyz", 0) == ["AEIOU"]

    # Words with a single consonant
    assert module_0.select_words("a b c d", 1) == ["b", "c", "d"]

    # No matches
    assert module_0.select_words("hello", 10) == []
    assert module_0.select_words("cat dog", 5) == []

    # Empty string
    assert module_0.select_words("", 0) == []
    assert module_0.select_words("", 3) == []

    # All words match
    assert module_0.select_words("hi yo", 1) == ["hi", "yo"]

    # Result preserves original word order and original casing
    assert module_0.select_words("Foo BAR baz", 2) == ["Foo", "BAR"]

# Generated at 2026-11-02 14:37:13.597579
# Unit test for function select_words
def test_select_words():
    # Basic cases
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Hello world", 4) == ["world"]
    assert module_0.select_words("Uncle Sam", 3) == ["Uncle"]

    # Words where 'y' counts as a consonant
    assert module_0.select_words("why try", 3) == ["why", "try"]

    # Edge cases
    assert module_0.select_words("", 0) == []
    assert module_0.select_words("", 3) == []
    assert module_0.select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]
    assert module_0.select_words("a b c d", 1) == ["b", "c", "d"]
    assert module_0.select_words("I am ok", 0) == ["I"]

    # No matches -> empty list
    assert module_0.select_words("xyz", 5) == []
    assert module_0.select_words("cat dog", 10) == []

    # Case insensitivity (vowels checked via .lower())
    assert module_0.select_words("BCD aeiou", 3) == ["BCD"]

    # Order of appearance is preserved
    assert module_0.select_words("bbb aaa ccc", 3) == ["bbb", "ccc"]

    print("All select_words tests passed!")


if __name__ == "__main__":
    test_select_words()

# Generated at 2026-11-02 14:41:26.041156
# Unit test for function select_words
def test_select_words():
    # Basic examples
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello world", 4) == ["world"]

    # Case insensitivity of vowel check
    assert module_0.select_words("APPLE pear Plum", 3) == ["APPLE", "pear", "Plum"]

    # Zero consonants: only words made entirely of vowels
    assert module_0.select_words("a e i o u ae io", 0) == ["a", "e", "i", "o", "u", "ae", "io"]

    # Empty string returns empty list
    assert module_0.select_words("", 3) == []

    # No word matches the required consonant count
    assert module_0.select_words("cat dog bird", 10) == []

    # Single word strings
    assert module_0.select_words("world", 4) == ["world"]
    assert module_0.select_words("hello", 3) == ["hello"]

    # 'y' is treated as a consonant (not in the vowel list)
    assert module_0.select_words("rhythm why", 6) == ["rhythm"]
    assert module_0.select_words("yay", 2) == ["yay"]

    # Words with duplicate letters counted correctly
    assert module_0.select_words("aa bb ccc", 2) == ["bb"]

    # Multiple spaces between words are handled by split()
    assert module_0.select_words("Mary   had   a   little   lamb", 3) == ["Mary", "lamb"]

    # All words match
    assert module_0.select_words("dog cat", 2) == ["dog", "cat"]