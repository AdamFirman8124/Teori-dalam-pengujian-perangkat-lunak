

# Generated at 2026-11-03 03:58:55.842687
# Unit test for function find_max
def test_find_max():
    # Word with the most unique characters wins
    assert module_0.find_max(["name", "of", "string"]) == "string"

    # Tie on unique count -> lexicographically smallest wins
    assert module_0.find_max(["name", "enam", "game"]) == "enam"

    # All words have 1 unique char -> lexicographically smallest wins
    assert module_0.find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    # Single-element list
    assert module_0.find_max(["abc"]) == "abc"

    # Same length but different unique character counts
    assert module_0.find_max(["aabb", "abcd"]) == "abcd"

    # Case sensitivity: 'aA' has 2 unique chars, 'aa' has 1
    assert module_0.find_max(["aA", "aa"]) == "aA"

    # Duplicates present
    assert module_0.find_max(["dog", "dog", "cat"]) == "cat"

    # Repeated characters count only once (4 unique vs 3)
    assert module_0.find_max(["mississippi", "xyz"]) == "mississippi"

    # More complex case: "banana" (3 unique), "abcde" (5 unique), "abc" (3 unique)
    assert module_0.find_max(["banana", "abcde", "abc"]) == "abcde"

    # Empty list raises IndexError
    with pytest.raises(IndexError):
        module_0.find_max([])

# Generated at 2026-11-03 04:01:43.370671
# Unit test for function find_max
def test_find_max():
    # nonce:02bf4277
    # Word with the most unique characters wins
    assert module_0.find_max(["name", "of", "string"]) == "string"
    assert module_0.find_max(["apple", "banana", "cherry", "date", "fig"]) == "cherry"

    # Ties broken by lexicographical order (smallest first)
    assert module_0.find_max(["name", "enam", "game"]) == "enam"
    assert module_0.find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    assert module_0.find_max(["abc", "cba"]) == "abc"
    assert module_0.find_max(["b", "a", "c"]) == "a"
    assert module_0.find_max(["xyz", "abc", "def"]) == "abc"

    # Repeated characters don't increase unique count
    assert module_0.find_max(["aabbcc", "abc"]) == "aabbcc"
    assert module_0.find_max(["mississippi", "misp"]) == "misp"

    # Single element / duplicates
    assert module_0.find_max(["hello"]) == "hello"
    assert module_0.find_max(["play", "play", "play"]) == "play"

    # Empty strings
    assert module_0.find_max(["", "a", "aa"]) == "a"
    assert module_0.find_max(["", ""]) == ""

    # Case sensitivity: uppercase sorts before lowercase
    assert module_0.find_max(["AB", "ab"]) == "AB"

    # Non-letter characters count toward uniqueness
    assert module_0.find_max(["a1!", "ab"]) == "a1!"

    # Result must be a member of the input list
    words = ["cat", "act", "tac", "dog"]
    assert module_0.find_max(words) in words
    assert module_0.find_max(words) == "act"

    # Empty input raises IndexError
    try:
        module_0.find_max([])
        assert False, "Expected IndexError for empty input"
    except IndexError:
        pass

    print("test_find_max: all assertions passed")


if __name__ == "__main__":
    test_find_max()

# Generated at 2026-11-03 04:03:54.473962
# Unit test for function find_max
def test_find_max():
    # Basic cases: word with most unique characters wins
    assert module_0.find_max(["name", "of", "string"]) == "string"
    assert module_0.find_max(["name", "enam", "game"]) == "enam"  # tie -> lexicographic
    assert module_0.find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"  # tie -> lexicographic
    assert module_0.find_max(["abc", "cba"]) == "abc"  # tie -> lexicographic
    assert module_0.find_max(["play", "play", "play"]) == "play"

    # Single element
    assert module_0.find_max(["hello"]) == "hello"

    # All duplicates within words
    assert module_0.find_max(["aa", "bb"]) == "aa"  # tie -> lexicographic

    # Mixed lengths and uniqueness
    assert module_0.find_max(["apple", "banana", "cherry"]) == "banana"  # 4 unique vs 3
    assert module_0.find_max(["book", "pencil"]) == "pencil"  # 5 unique vs 3

    # Empty string is a valid word (0 unique chars)
    assert module_0.find_max(["", "a"]) == "a"
    assert module_0.find_max([""]) == ""

    # Case sensitivity: 'A' and 'a' are distinct characters
    assert module_0.find_max(["aA", "aa"]) == "aA"

    # Numbers and special characters count as unique chars
    assert module_0.find_max(["a1!", "abc"]) == "a1!"  # both 3, tie -> "a1!" < "abc"

    # Longer list
    words = ["cat", "dog", "bird", "fish", "elephant", "giraffe"]
    assert module_0.find_max(words) == "elephant"  # 7 unique chars

    print("All tests passed!")

# Generated at 2026-11-03 04:05:57.649386
# Unit test for function find_max
def test_find_max():
    # Word with most unique characters wins
    assert module_0.find_max(["name", "of", "string"]) == "string"
    # Tie on unique count -> lexicographically smallest wins
    assert module_0.find_max(["name", "enam", "game"]) == "enam"
    # All single-unique-char words -> smallest lexicographically
    assert module_0.find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    # Increasing unique character counts
    assert module_0.find_max(["abc", "abcd", "abcde"]) == "abcde"
    # Single element list
    assert module_0.find_max(["hello"]) == "hello"
    # Repeated characters don't increase unique count
    assert module_0.find_max(["aabbcc", "abc", "xyz"]) == "abc"
    # Case sensitivity: 'A' and 'a' are distinct characters
    assert module_0.find_max(["Aa", "ab"]) == "Aa"
    # Empty string has zero unique characters
    assert module_0.find_max(["", "a"]) == "a"
    # Tie between different-length words with same unique count
    assert module_0.find_max(["apple", "pear"]) == "apple"
    # Duplicates in list
    assert module_0.find_max(["dog", "dog", "cat"]) == "cat"

# Generated at 2026-11-03 04:08:00.308073
# Unit test for function find_max
def test_find_max():
    # Word with the most unique characters wins
    assert module_0.find_max(["name", "of", "string"]) == "string"
    # Tie in unique count -> lexicographically smallest wins
    assert module_0.find_max(["name", "enam", "game"]) == "enam"
    # All single unique char, lexicographic tie-break
    assert module_0.find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    # Single element list
    assert module_0.find_max(["apple"]) == "apple"
    # More unique chars beats fewer, regardless of length
    assert module_0.find_max(["abc", "abcdef", "ab"]) == "abcdef"
    # Case-sensitive unique characters: 'A' != 'a', tie broken lexicographically
    assert module_0.find_max(["aA", "Aa"]) == "Aa"
    # Mixed lengths and repeats
    assert module_0.find_max(["hello", "world", "python"]) == "python"
    # Empty string handled correctly
    assert module_0.find_max(["", "a"]) == "a"
    # Tie among equal-length words
    assert module_0.find_max(["cat", "dog", "bat"]) == "bat"
    # Repeated characters reduce unique count
    assert module_0.find_max(["aabbb", "abcd", "aabbccdd"]) == "abcd"
    print("All tests passed!")