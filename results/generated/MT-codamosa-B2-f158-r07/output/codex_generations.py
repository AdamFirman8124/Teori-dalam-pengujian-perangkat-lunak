

# Generated at 2026-10-24 01:22:44.561474
# Unit test for function find_max
def test_find_max():
    # "cherry" has the most distinct characters: c, h, e, r, y
    assert module_0.find_max(["apple", "banana", "cherry", "aaaa"]) == "cherry"

    # When words have the same number of distinct characters,
    # the lexicographically smallest word is returned.
    assert module_0.find_max(["ba", "ab", "cc"]) == "ab"

    # Repeated characters count only once.
    assert module_0.find_max(["aaaa", "abcd", "aabb"]) == "abcd"

# Generated at 2026-10-24 01:23:00.238866
# Unit test for function find_max
def test_find_max():
    # Selects the word with the most distinct characters
    assert module_0.find_max(["apple", "banana", "cherry"]) == "cherry"

    # Uses lexicographical order when distinct-character counts tie
    assert module_0.find_max(["ba", "ab"]) == "ab"

    # Handles a single word
    assert module_0.find_max(["hello"]) == "hello"

    # Repeated characters are counted only once
    assert module_0.find_max(["aaaa", "abc"]) == "abc"

# Generated at 2026-10-24 01:23:16.098060
# Unit test for function find_max
def test_find_max():
    words = ["apple", "banana", "cherry", "date"]
    
    # "cherry" has the most unique characters
    assert module_0.find_max(words) == "cherry"


def test_find_max_uses_lexicographic_order_for_ties():
    words = ["ba", "cd", "ab"]
    
    # All words have two unique characters, so "ab" comes first alphabetically
    assert module_0.find_max(words) == "ab"

# Generated at 2026-10-24 01:23:31.767807
# Unit test for function find_max
def test_find_max():
    assert module_0.find_max(["apple", "banana", "cherry"]) == "cherry"
    assert module_0.find_max(["hello", "world"]) == "world"
    assert module_0.find_max(["aaa", "bbb", "cc"]) == "aaa"
    assert module_0.find_max(["ba", "ab"]) == "ab"  # alphabetical tie-breaker

# Generated at 2026-10-24 01:23:46.923772
# Unit test for function find_max
def test_find_max():
    # Word with the greatest number of distinct characters
    assert module_0.find_max(["apple", "banana", "cherry"]) == "cherry"

    # If distinct-character counts tie, choose lexicographically first word
    assert module_0.find_max(["dog", "cat", "pig"]) == "cat"

    # Repeated characters should only be counted once
    assert module_0.find_max(["aaaa", "abca", "abcde"]) == "abcde"

    # Tie in distinct-character count
    assert module_0.find_max(["abcd", "wxyz", "abc"]) == "abcd"


if __name__ == "__main__":
    test_find_max()
    print("All tests passed.")