

# Generated at 2026-11-02 14:21:46.009627
# Unit test for function find_max
def test_find_max():
    # Basic case: word with most unique characters wins
    assert module_0.find_max(["name", "of", "string"]) == "string"

    # Tie in unique character count -> lexicographically smallest wins
    assert module_0.find_max(["name", "enam", "game"]) == "enam"

    # All words have 1 unique char; lexicographic tie-break
    assert module_0.find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    # Single-element list
    assert module_0.find_max(["apple"]) == "apple"

    # Duplicate letters reduce unique character count
    assert module_0.find_max(["abc", "aaabb"]) == "abc"

    # Empty string vs non-empty string
    assert module_0.find_max(["", "a"]) == "a"

    # Simple tie broken lexicographically
    assert module_0.find_max(["ab", "ba"]) == "ab"

    # Larger mixed example
    assert module_0.find_max(["hello", "world", "python", "code"]) == "python"

# Generated at 2026-11-02 14:23:23.565533
# Unit test for function find_max
def test_find_max():
    # Basic case: word with most unique characters
    assert module_0.find_max(["name", "of", "string"]) == "string"

    # Tie in unique character count -> lexicographically smallest wins
    assert module_0.find_max(["name", "enam", "game"]) == "enam"

    # All unique counts equal, lexicographic order
    assert module_0.find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    # Single word
    assert module_0.find_max(["hello"]) == "hello"

    # Word with repeated characters has fewer unique chars
    assert module_0.find_max(["abc", "aabbcc", "ab"]) == "abc"

    # Empty string has zero unique characters
    assert module_0.find_max(["", "a", "b"]) == ""

    # Empty string loses when others exist with more unique chars
    assert module_0.find_max(["", "abc"]) == "abc"

    # Tie between same word content but different cases
    assert module_0.find_max(["ABC", "abc"]) == "ABC"

    # Case sensitivity: 'a' and 'A' count as distinct characters
    assert module_0.find_max(["aA", "aa"]) == "aA"

    # Numbers and symbols count as characters
    assert module_0.find_max(["123", "abc"]) == "123"

    # Long word with all same characters
    assert module_0.find_max(["zzzzzzzzz", "abcd"]) == "abcd"

    # Multiple ties resolved lexicographically
    assert module_0.find_max(["bd", "ac", "bb"]) == "ac"

    print("All test_find_max tests passed!")


if __name__ == "__main__":
    test_find_max()

# Generated at 2026-11-02 14:26:22.145428
# Unit test for function find_max
def test_find_max():
    # Basic case: word with most unique characters
    assert module_0.find_max(["name", "of", "string"]) == "string"
    # Tie on unique count -> lexicographically smallest wins
    assert module_0.find_max(["name", "enam", "game"]) == "enam"
    # All single unique char, tie broken alphabetically
    assert module_0.find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"
    # Same length, same unique count
    assert module_0.find_max(["abc", "cba"]) == "abc"
    # Mixed lengths and repeats
    assert module_0.find_max(["play", "this", "game", "of", "footbott"]) == "footbott"
    # Word with more unique chars beats longer word with repeats
    assert module_0.find_max(["we", "are", "gonna", "rock"]) == "rock"
    # Longer word with many unique characters
    assert module_0.find_max(["we", "are", "a", "mad", "nation"]) == "nation"
    # Repeated letters reduce unique count
    assert module_0.find_max(["this", "is", "a", "prrrroooject"]) == "prrrroooject"
    # Single-element list
    assert module_0.find_max(["hello"]) == "hello"
    # Unique count dominates over lexicographic order
    assert module_0.find_max(["b", "tttt", "cccaaa"]) == "cccaaa"

# Generated at 2026-11-02 14:30:15.629934
# Unit test for function find_max
def test_find_max():
    # Word with the most unique characters wins
    assert module_0.find_max(["name", "of", "string"]) == "string"

    # Tie in unique count -> lexicographically smallest wins
    assert module_0.find_max(["name", "enam", "game"]) == "enam"

    # All words have same unique count -> lexicographically smallest
    assert module_0.find_max(["aaaaaaa", "bb", "cc"]) == "aaaaaaa"

    # Single-element list
    assert module_0.find_max(["hello"]) == "hello"

    # Duplicate characters count only once
    assert module_0.find_max(["abcabc", "abcd"]) == "abcd"

    # Tie with repeated characters
    assert module_0.find_max(["abab", "cd"]) == "abab"

    # Case sensitivity: 'A' and 'a' are distinct characters
    assert module_0.find_max(["aA", "ab"]) == "aA"

    # Digits/punctuation count as characters
    assert module_0.find_max(["12", "ab"]) == "12"
    assert module_0.find_max(["a1!", "abcd"]) == "abcd"

    # True tie -> lexicographic order decides
    assert module_0.find_max(["dog", "cat"]) == "cat"

    # Later word can win by unique count
    assert module_0.find_max(["a", "bc", "def"]) == "def"

    # Result must always be one of the input words
    words = ["apple", "grape", "kiwi"]
    assert module_0.find_max(words) in words

    print("All tests passed!")


if __name__ == "__main__":
    test_find_max()