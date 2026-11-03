

# Generated at 2026-11-03 03:25:26.839927
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # Test with mixed even and odd length strings
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

    # Test with all even length strings, sorted by length
    assert module_0.sorted_list_sum(["ab", "abcd", "cd"]) == ["ab", "cd", "abcd"]

    # Test with same-length strings (should stay alphabetically sorted)
    assert module_0.sorted_list_sum(["cc", "bb", "aa"]) == ["aa", "bb", "cc"]

    # Test with all odd length strings (should return empty list)
    assert module_0.sorted_list_sum(["a", "abc", "abcde"]) == []

    # Test with empty list
    assert module_0.sorted_list_sum([]) == []

    # Test with single even-length element
    assert module_0.sorted_list_sum(["hello world"]) == ["hello world"]

    # Test with single odd-length element
    assert module_0.sorted_list_sum(["abc"]) == []

    # Test with mixed lengths and alphabetical tie-breaking
    assert module_0.sorted_list_sum(["dcba", "dc", "abcd", "ab"]) == ["ab", "dc", "abcd", "dcba"]

    # Test with duplicate strings
    assert module_0.sorted_list_sum(["aa", "aa", "aaa"]) == ["aa", "aa"]

    # Test with numbers as strings of even length
    assert module_0.sorted_list_sum(["1234", "12", "12"]) == ["12", "12", "1234"]

    print("All tests passed!")


test_sorted_list_sum()

# Generated at 2026-11-03 03:27:19.377765
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # Test with mixed even and odd length strings
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

    # Test with all odd length strings (should return empty list)
    assert module_0.sorted_list_sum(["a", "abc", "abcde"]) == []

    # Test with all even length strings
    assert module_0.sorted_list_sum(["ab", "abcd", "abcdef"]) == ["ab", "abcd", "abcdef"]

    # Test with strings of the same length (should stay alphabetically sorted)
    assert module_0.sorted_list_sum(["bb", "aa", "cc"]) == ["aa", "bb", "cc"]

    # Test with unsorted input of varying even lengths
    assert module_0.sorted_list_sum(["dddd", "aa", "cc", "b"]) == ["aa", "cc", "dddd"]

    # Test with empty list
    assert module_0.sorted_list_sum([]) == []

    # Test with single element
    assert module_0.sorted_list_sum(["ab"]) == ["ab"]
    assert module_0.sorted_list_sum(["abc"]) == []

    # Test with duplicates
    assert module_0.sorted_list_sum(["ab", "ab", "abc"]) == ["ab", "ab"]

    # Test with mixed lengths and tie-breaking by alphabetical order
    assert module_0.sorted_list_sum(["bba", "bb", "aa", "dddd", "a"]) == ["aa", "bb", "dddd"]

    # Test that length takes priority over alphabetical order in final sort
    assert module_0.sorted_list_sum(["zz", "aaaa", "bb"]) == ["zz", "bb", "aaaa"]

    print("All tests passed!")


test_sorted_list_sum()

# Generated at 2026-11-03 03:29:06.490283
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # Basic case: odd-length strings are removed, even-length sorted by length
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

    # Two even-length strings of same length, sorted alphabetically
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

    # Multiple lengths: shorter even-length strings come first
    assert module_0.sorted_list_sum(["abcd", "ab", "abcde", "abcdef"]) == ["ab", "abcd", "abcdef"]

    # Same length strings are sorted alphabetically (stable sort after initial sort)
    assert module_0.sorted_list_sum(["dd", "bb", "aa", "cc"]) == ["aa", "bb", "cc", "dd"]

    # All odd-length strings result in empty list
    assert module_0.sorted_list_sum(["a", "abc", "abcde"]) == []

    # Empty input list
    assert module_0.sorted_list_sum([]) == []

    # Mixed lengths, verify filtering and ordering together
    assert module_0.sorted_list_sum(["hello", "world", "hi", "hey", "yo"]) == ["hi", "yo"]

    # Single even-length string
    assert module_0.sorted_list_sum(["even"]) == ["even"]

    # Single odd-length string is filtered out
    assert module_0.sorted_list_sum(["odd"]) == []

    # Duplicates are preserved
    assert module_0.sorted_list_sum(["ab", "ab", "a"]) == ["ab", "ab"]

    # Input list should not be permanently reordered in unexpected ways (sorted first)
    original = ["zz", "aa", "bb"]
    result = module_0.sorted_list_sum(original)
    assert result == ["aa", "bb", "zz"]

    print("All tests passed!")


if __name__ == "__main__":
    test_sorted_list_sum()

# Generated at 2026-11-03 03:30:59.985840
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # Basic case: odd-length strings are filtered out
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

    # Even-length strings sorted by length
    assert module_0.sorted_list_sum(["school", "AI", "asdf", "b"]) == ["AI", "asdf", "school"]

    # Empty input list
    assert module_0.sorted_list_sum([]) == []

    # All odd-length strings -> empty result
    assert module_0.sorted_list_sum(["a", "abc", "abcde"]) == []

    # Ties in length keep alphabetical (stable) order
    assert module_0.sorted_list_sum(["bb", "aa", "cc"]) == ["aa", "bb", "cc"]

    # Duplicates are preserved
    assert module_0.sorted_list_sum(["ab", "abc", "ab"]) == ["ab", "ab"]

    # Single even-length string
    assert module_0.sorted_list_sum(["abcd"]) == ["abcd"]

    # Mixed lengths ordered ascending
    assert module_0.sorted_list_sum(["dddd", "bb", "cccc", "a"]) == ["bb", "dddd", "cccc"]

    print("All tests passed!")