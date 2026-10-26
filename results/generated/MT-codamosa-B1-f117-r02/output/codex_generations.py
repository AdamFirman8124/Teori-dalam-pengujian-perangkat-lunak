

# Generated at 2026-10-25 09:37:34.536707
# Unit test for function select_words

# Generated at 2026-10-25 09:37:36.950699
# Unit test for function select_words

# Generated at 2026-10-25 09:37:39.364808
# Unit test for function select_words

# Generated at 2026-10-25 09:37:47.299678
# Unit test for function select_words
def test_select_words():
    # Basic examples
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello world", 4) == ["world"]

    # Empty string
    assert module_0.select_words("", 4) == []

    # Case insensitivity (uppercase vowels must not count as consonants)
    assert module_0.select_words("APPLE", 3) == ["APPLE"]
    assert module_0.select_words("AEIOU", 0) == ["AEIOU"]

    # Word that is all vowels
    assert module_0.select_words("a e i o u", 1) == []

    # No match returns empty list
    assert module_0.select_words("cat dog", 10) == []

    # Duplicate qualifying words are all returned
    assert module_0.select_words("cat cat dog", 2) == ["cat", "cat"]

    print("All tests passed!")

# Generated at 2026-10-25 09:37:48.771530
# Unit test for function select_words
def test_select_words():
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello world", 4) == ["world"]
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]
    assert module_0.select_words("AEIOU aeiou", 0) == ["AEIOU", "aeiou"]
    assert module_0.select_words("", 0) == []
    print("all passed")

test_select_words()

# Generated at 2026-10-25 09:37:49.997760
# Unit test for function select_words
def test_select_words():
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello world", 4) == ["world"]
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]
    assert module_0.select_words("AEIOU aeiou", 0) == ["AEIOU", "aeiou"]
    assert module_0.select_words("", 0) == []
    print("all passed")

test_select_words()

# Generated at 2026-10-25 09:37:51.461902
# Unit test for function select_words
def test_select_words():
    assert module_0.select_words("Mary had a little lamb", 4) == ["little"]
    assert module_0.select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert module_0.select_words("simple white space", 2) == []
    assert module_0.select_words("Hello world", 4) == ["world"]
    assert module_0.select_words("Uncle sam", 3) == ["Uncle"]
    assert module_0.select_words("AEIOU aeiou", 0) == ["AEIOU", "aeiou"]
    assert module_0.select_words("", 0) == []
    print("all passed")

test_select_words()