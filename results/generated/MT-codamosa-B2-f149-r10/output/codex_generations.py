

# Generated at 2026-11-01 21:43:32.622846
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # Only even-length strings are kept; odd-length ones removed
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

    # Result sorted primarily by length, then alphabetically
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

    # Empty input returns empty list
    assert module_0.sorted_list_sum([]) == []

    # All odd-length strings results in empty list
    assert module_0.sorted_list_sum(["a", "abc", "abcde"]) == []

    # Length ordering overrides original positions
    assert module_0.sorted_list_sum(["dddd", "bb", "cc"]) == ["bb", "cc", "dddd"]

    # Ties on length broken alphabetically (via initial sort + stable sort)
    assert module_0.sorted_list_sum(["dcba", "abcd", "ab"]) == ["ab", "abcd", "dcba"]

    # Mixed lengths with duplicates
    assert module_0.sorted_list_sum(["eee", "ef", "ff", "gh"]) == ["ef", "ff", "gh"]

    # Single element, even length
    assert module_0.sorted_list_sum(["test"]) == ["test"]

    # Single element, odd length gets filtered
    assert module_0.sorted_list_sum(["tests"]) == []

# Generated at 2026-11-01 21:43:42.555413
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # Filters out odd-length strings
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

    # Sorted by length ascending when lengths differ
    assert module_0.sorted_list_sum(["abc", "de", "abcd", "a"]) == ["de", "abcd"]
    assert module_0.sorted_list_sum(["aaaa", "bb", "cc"]) == ["bb", "cc", "aaaa"]

    # Same-length strings remain in alphabetical order (stable sort)
    assert module_0.sorted_list_sum(["dd", "aa", "cc", "bb"]) == ["aa", "bb", "cc", "dd"]
    assert module_0.sorted_list_sum(["school", "AI", "asdf", "b"]) == ["AI", "asdf", "school"]

    # Empty input returns empty list
    assert module_0.sorted_list_sum([]) == []

    # All odd-length strings get filtered out
    assert module_0.sorted_list_sum(["a", "bbb", "ccccc"]) == []

    # Single element cases
    assert module_0.sorted_list_sum(["even"]) == ["even"]
    assert module_0.sorted_list_sum(["odd"]) == []

    # Duplicates are preserved
    assert module_0.sorted_list_sum(["ab", "ab", "abc"]) == ["ab", "ab"]

    print("All tests passed!")


test_sorted_list_sum()

# Generated at 2026-11-01 21:44:06.325376
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # Test with mixed even and odd length strings
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

    # Test with all even length strings, sorted by length then lexicographically
    assert module_0.sorted_list_sum(["ab", "cd", "efgh"]) == ["ab", "cd", "efgh"]
    assert module_0.sorted_list_sum(["abcd", "ab", "abcdef"]) == ["ab", "abcd", "abcdef"]

    # Test with same length strings - should be lexicographically ordered
    assert module_0.sorted_list_sum(["dd", "aa", "cc", "bb"]) == ["aa", "bb", "cc", "dd"]

    # Test with empty list
    assert module_0.sorted_list_sum([]) == []

    # Test with all odd length strings - should return empty list
    assert module_0.sorted_list_sum(["a", "abc", "abcde"]) == []

    # Test with single element
    assert module_0.sorted_list_sum(["even"]) == ["even"]
    assert module_0.sorted_list_sum(["odd"]) == []

    # Test with duplicates
    assert module_0.sorted_list_sum(["aa", "aa", "bbb"]) == ["aa", "aa"]

    # Test that original list sorting happens first (lexicographic tiebreak for equal lengths)
    assert module_0.sorted_list_sum(["bbaa", "abba", "cc"]) == ["cc", "abba", "bbaa"]

    # Test with empty strings (length 0 is even)
    assert module_0.sorted_list_sum(["", "a", "bb"]) == ["", "bb"]

    # Verify original list is not mutated in an unexpected way
    original = ["bb", "a", "cc"]
    result = module_0.sorted_list_sum(original)
    assert result == ["bb", "cc"]
    # Note: original list IS sorted in place by the function
    assert original == ["a", "bb", "cc"]

    print("All tests passed!")


if __name__ == "__main__":
    test_sorted_list_sum()

# Generated at 2026-11-01 21:44:42.279904
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # Basic case: odd-length strings are removed, result sorted by length
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

    # Ties in length preserve alphabetical order (stable sort after pre-sort)
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

    # Empty input list
    assert module_0.sorted_list_sum([]) == []

    # All odd-length strings filtered out
    assert module_0.sorted_list_sum(["a", "abc", "abcde"]) == []

    # All even-length strings kept, ordered by length then alphabetically
    assert module_0.sorted_list_sum(["dd", "bbbb", "cc"]) == ["dd", "cc", "bbbb"]

    # Mixed case with pre-sorting affecting tie order
    assert module_0.sorted_list_sum(["school", "AI", "asdf", "b"]) == ["AI", "asdf", "school"]

    # Duplicates are preserved
    assert module_0.sorted_list_sum(["aa", "aa", "b"]) == ["aa", "aa"]

    # Single element cases
    assert module_0.sorted_list_sum(["hello"]) == []
    assert module_0.sorted_list_sum(["hi"]) == ["hi"]

    # Empty string has length 0 (even), so it is kept
    assert module_0.sorted_list_sum(["", "a", "bb"]) == ["", "bb"]

    # Odd-length mixed with even-length
    assert module_0.sorted_list_sum(["abc", "de", "fgh"]) == ["de"]


if __name__ == "__main__":
    test_sorted_list_sum()
    print("All tests passed!")

# Generated at 2026-11-01 21:45:07.241569
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # Filters out odd-length strings and sorts remaining by length
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert module_0.sorted_list_sum(["abc", "abcd", "ab"]) == ["ab", "abcd"]

    # Only even-length strings remain
    assert module_0.sorted_list_sum(["aa", "bb", "cc"]) == ["aa", "bb", "cc"]

    # All odd-length strings -> empty result
    assert module_0.sorted_list_sum(["a", "abc", "abcde"]) == []

    # Empty input list
    assert module_0.sorted_list_sum([]) == []

    # Single even-length element
    assert module_0.sorted_list_sum(["hello!!"]) == ["hello!!"]

    # Same length -> preserves alphabetical order (initial sort is stable via sorted-by-len)
    assert module_0.sorted_list_sum(["dog", "cat", "bird", "fish"]) == ["bird", "fish"]

    # Ties resolved alphabetically among equal-length strings
    assert module_0.sorted_list_sum(["dcba", "ab", "cd"]) == ["ab", "cd", "dcba"]

    # Mixed case duplicates of same length
    assert module_0.sorted_list_sum(["xyz", "xy", "wxy", "wx"]) == ["wx", "xy", "wxy", "xyz"]

    print("All tests passed!")


if __name__ == "__main__":
    test_sorted_list_sum()