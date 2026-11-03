

# Generated at 2026-11-03 05:55:15.008713
# Unit test for function select_words
def test_select_words():
    # Basic examples
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello world", 4) == ["world"]
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]

    # No matching words
    assert module_0.select_words("a b c d e f", 10) == []

    # Empty string
    assert module_0.select_words("", 4) == []

    # Single character words
    assert module_0.select_words("a b c", 1) == ["b", "c"]

    # All vowels (uppercase vowels should not count as consonants)
    assert module_0.select_words("AEIOU bcdfg", 5) == ["bcdfg"]
    assert module_0.select_words("AEIOU bcdfg", 0) == ["AEIOU"]

    # Word with repeated consonants
    assert module_0.select_words("sss aaa", 3) == ["sss"]

    # n = 0 matches words with only vowels
    assert module_0.select_words("eye sky", 0) == ["eye"]

# Generated at 2026-11-03 05:55:45.569114
# Unit test for function select_words
def test_select_words():
    # Standard cases
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello World", 4) == ["World"]
    assert module_0.select_words("Uncle Sam", 3) == ["Uncle"]

    # Words with zero consonants
    assert module_0.select_words("a b c d", 0) == ["a", "b", "c", "d"]
    assert module_0.select_words("aeiou", 0) == ["aeiou"]

    # Multiple matches preserving order
    assert module_0.select_words("one two three four five", 2) == ["two", "four", "five"]

    # Empty string
    assert module_0.select_words("", 1) == []
    assert module_0.select_words("", 0) == []

    # Case insensitivity of vowel check
    assert module_0.select_words("AEIOU Bc", 0) == ["AEIOU"]
    assert module_0.select_words("AEIOU Bc", 1) == ["Bc"]

    # No matches
    assert module_0.select_words("cat dog", 10) == []

# Generated at 2026-11-03 05:56:17.387261
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

    # n = 0 selects words with only vowels
    assert module_0.select_words("a e i o u aeio", 0) == ["a", "e", "i", "o", "u", "aeio"]

    # Case insensitivity: uppercase consonants still count
    assert module_0.select_words("AEIOU BCDF", 4) == ["BCDF"]
    assert module_0.select_words("Apple ORANGE", 3) == ["Apple"]

    # Single word strings
    assert module_0.select_words("hello", 3) == ["hello"]
    assert module_0.select_words("hello", 2) == []

    # Words with mixed case
    assert module_0.select_words("AbCdEf", 3) == ["AbCdEf"]

    # Multiple matches preserving order
    assert module_0.select_words("cat dog bird fish", 2) == ["cat", "dog", "fish"]

    # No matches
    assert module_0.select_words("one two three", 10) == []

    # Repeated identical words
    assert module_0.select_words("test test test", 3) == ["test", "test", "test"]

    # Extra whitespace between words
    assert module_0.select_words("  Mary   had  a  little   lamb ", 4) == ["little"]

# Generated at 2026-11-03 05:58:15.744363
# Unit test for function select_words
def test_select_words():
    # Standard cases
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello world", 4) == ["world"]
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]

    # Empty string
    assert module_0.select_words("", 0) == []
    assert module_0.select_words("", 4) == []

    # Single-character words
    assert module_0.select_words("a b c d", 1) == ["b", "c", "d"]
    assert module_0.select_words("a e i o u", 0) == ["a", "e", "i", "o", "u"]

    # Case-insensitivity of vowel detection
    assert module_0.select_words("AEIOU aeiou", 0) == ["AEIOU", "aeiou"]
    assert module_0.select_words("BCDF bcdf", 4) == ["BCDF", "bcdf"]

    # All words match
    assert module_0.select_words("cat dog fox", 2) == ["cat", "dog", "fox"]

    # No matches
    assert module_0.select_words("cat dog fox", 5) == []

    # Repeated words
    assert module_0.select_words("hello hello world", 3) == ["hello", "hello"]

    # Words with all consonants vs all vowels
    assert module_0.select_words("rhythm sky eye", 3) == ["sky"]
    assert module_0.select_words("rhythm", 5) == ["rhythm"]

# Generated at 2026-11-03 06:01:05.219177
# Unit test for function select_words
def test_select_words():
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 3) == ["white", "space"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("", 4) == []
    assert module_0.select_words("a b c d e f", 0) == ["a", "e"]
    assert module_0.select_words("hello world", 4) == ["world"]
    assert module_0.select_words("Hello", 3) == ["Hello"]
    assert module_0.select_words("xyz", 3) == ["xyz"]
    assert module_0.select_words("one two three", 100) == []