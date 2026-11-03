

# Generated at 2026-11-02 00:40:44.298297
# Unit test for function find_max
def test_find_max():
    # nonce:6f4ccda6
    # Word with the most unique characters wins
    assert module_0.find_max(["name", "of", "string"]) == "string"
    # Tie on unique count -> lexicographically smallest wins
    assert module_0.find_max(["name", "enam", "game"]) == "enam"
    # All words have one unique char -> lexicographically smallest
    assert module_0.find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    # Anagrams tie on unique count -> lexicographic tiebreak
    assert module_0.find_max(["abc", "cba", "bac"]) == "abc"
    # Mixed unique counts
    assert module_0.find_max(["apple", "banana", "cherry"]) == "cherry"
    # Single element list
    assert module_0.find_max(["single"]) == "single"
    # Equal unique counts -> lexicographic tiebreak
    assert module_0.find_max(["ab", "cd", "ef"]) == "ab"
    # Longer word with more unique chars wins
    assert module_0.find_max(["hello", "world", "python"]) == "python"
    # Empty string has zero unique characters
    assert module_0.find_max(["", "a"]) == "a"
    # set() is case-sensitive: 'A' and 'a' are distinct
    assert module_0.find_max(["Aa", "ab"]) == "Aa"


if __name__ == "__main__":
    test_find_max()
    print("All tests passed!")

# Generated at 2026-11-02 00:42:00.797344
# Unit test for function find_max
def test_find_max():
    # Word with the most unique characters wins
    assert module_0.find_max(["name", "of", "string"]) == "string"
    assert module_0.find_max(["name", "enam", "game"]) == "enam"
    assert module_0.find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    # Tie on unique character count -> lexicographically smallest wins
    assert module_0.find_max(["apple", "pear", "grape"]) == "apple"
    assert module_0.find_max(["bca", "cab", "abc"]) == "abc"
    assert module_0.find_max(["xy", "yx", "ab"]) == "ab"

    # Repeated characters don't add uniqueness
    assert module_0.find_max(["banana", "bandana"]) == "bandana"
    assert module_0.find_max(["aaa", "aab", "abb"]) == "aab"

    # Single-element list
    assert module_0.find_max(["hello"]) == "hello"
    assert module_0.find_max(["z"]) == "z"

    # Case sensitivity: 'A' and 'a' are distinct characters
    assert module_0.find_max(["aA", "aa"]) == "aA"

    # Longer word with more unique chars beats shorter ones
    assert module_0.find_max(["cat", "elephant", "dog"]) == "elephant"

    # All identical words
    assert module_0.find_max(["same", "same", "same"]) == "same"


if __name__ == "__main__":
    test_find_max()
    print("All tests passed!")

# Generated at 2026-11-02 00:43:03.158559
# Unit test for function find_max
def test_find_max():
    # Word with the most unique characters wins
    assert module_0.find_max(["name", "of", "string"]) == "string"

    # Tie on unique count -> lexicographically smallest word wins
    assert module_0.find_max(["name", "enam", "game"]) == "enam"

    # Single-element list
    assert module_0.find_max(["aaaaaaa"]) == "aaaaaaa"

    # Repeated characters count only once
    assert module_0.find_max(["abc", "aaaa", "aaa"]) == "abc"

    # Case-sensitive uniqueness: 'A' != 'a'
    assert module_0.find_max(["aA", "aa"]) == "aA"

    # Empty string has zero unique characters
    assert module_0.find_max(["", "a"]) == "a"

    # All tied on unique count -> alphabetical order decides
    assert module_0.find_max(["bb", "aa", "cc"]) == "aa"

    # Mixed lengths and repeats
    assert module_0.find_max(["apple", "banana", "cherry"]) == "cherry"

    # Duplicate words in the list, tie broken alphabetically
    assert module_0.find_max(["abc", "abc", "abd"]) == "abc"

    # Longer word but fewer unique characters loses
    assert module_0.find_max(["aabbcc", "xyz"]) == "xyz"

    # Empty list should raise IndexError
    try:
        module_0.find_max([])
        assert False, "Expected IndexError for empty list"
    except IndexError:
        pass

# Generated at 2026-11-02 00:44:40.188209
# Unit test for function find_max
def test_find_max():
    # Word with the most unique characters wins
    assert module_0.find_max(["name", "of", "string"]) == "string"

    # Tie on unique character count -> lexicographically smallest word
    assert module_0.find_max(["name", "enam", "game"]) == "enam"
    assert module_0.find_max(["aaaaaaa", "bb", "cc"]) == "bb"
    assert module_0.find_max(["ab", "cd", "ef"]) == "ab"

    # All identical words
    assert module_0.find_max(["abc", "abc"]) == "abc"

    # Mixed lengths and unique counts
    assert module_0.find_max(["apple", "banana", "cherry"]) == "cherry"

    # Single-element list
    assert module_0.find_max(["hello"]) == "hello"

    # Repeated letters still count unique chars only
    assert module_0.find_max(["aabb", "ab"]) == "aabb"

    # Case sensitivity: 'A' and 'a' are distinct characters
    assert module_0.find_max(["aA", "aa"]) == "aA"

    # Empty strings have zero unique characters
    assert module_0.find_max(["", "a"]) == "a"

# Generated at 2026-11-02 00:46:02.798255
# Unit test for function find_max
def test_find_max():
    # Word with the most unique characters wins
    assert module_0.find_max(["name", "of", "string"]) == "string"

    # Tie on unique character count -> lexicographically smallest word
    assert module_0.find_max(["name", "enam", "game"]) == "enam"

    # All tied -> smallest lexicographic word returned
    assert module_0.find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    # Single element list
    assert module_0.find_max(["hello"]) == "hello"

    # Repeated characters don't increase unique count
    assert module_0.find_max(["abcabc", "abcd"]) == "abcd"

    # Case sensitivity: 'a' and 'A' are distinct characters
    assert module_0.find_max(["aA", "ab"]) == "aA"

    # Input order doesn't affect result
    assert module_0.find_max(["xy", "z", "wxyz"]) == "wxyz"

    # Tie among several single-char words -> lexicographically smallest
    assert module_0.find_max(["b", "a", "c"]) == "a"