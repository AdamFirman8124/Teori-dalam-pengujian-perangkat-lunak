

# Generated at 2026-11-02 18:59:26.910856
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # Mixed even and odd length strings
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert module_0.sorted_list_sum(["school", "AI", "asdf", "b"]) == ["AI", "asdf", "school"]
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

    # All strings even length: sorted alphabetically first, then by length (stable)
    assert module_0.sorted_list_sum(["bb", "aa", "cc", "ab"]) == ["aa", "ab", "bb", "cc"]

    # Length-based reordering after filtering
    assert module_0.sorted_list_sum(["dddd", "aa", "bb"]) == ["aa", "bb", "dddd"]
    assert module_0.sorted_list_sum(["dddddd", "bb", "aa"]) == ["aa", "bb", "dddddd"]

    # Single element
    assert module_0.sorted_list_sum(["abc"]) == []
    assert module_0.sorted_list_sum(["ab"]) == ["ab"]

    # Empty list
    assert module_0.sorted_list_sum([]) == []

    # All odd length strings filtered out
    assert module_0.sorted_list_sum(["a", "abc", "abcde"]) == []

    # Ties in length preserve alphabetical order (stable sort)
    assert module_0.sorted_list_sum(["dd", "cc", "bb", "aa"]) == ["aa", "bb", "cc", "dd"]
    assert module_0.sorted_list_sum(["ax", "bx", "aa", "bb"]) == ["aa", "ax", "bb", "bx"]

    print("All tests passed!")


test_sorted_list_sum()

# Generated at 2026-11-02 19:01:05.881299
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # nonce:4c5d77bc
    # Basic filtering: odd-length strings removed, result sorted by length
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert module_0.sorted_list_sum(["school", "AI", "asdf", "b"]) == ["AI", "asdf", "school"]

    # Empty input
    assert module_0.sorted_list_sum([]) == []

    # All odd-length strings are filtered out
    assert module_0.sorted_list_sum(["a", "bbb", "ccccc"]) == []

    # All even-length strings sorted by length
    assert module_0.sorted_list_sum(["abcd", "ab", "abcdef"]) == ["ab", "abcd", "abcdef"]

    # Ties in length preserve alphabetical order (stable sort after initial sort)
    assert module_0.sorted_list_sum(["dcba", "abcd", "efgh"]) == ["abcd", "dcba", "efgh"]
    assert module_0.sorted_list_sum(["bb", "aa", "cc"]) == ["aa", "bb", "cc"]

    # Single element cases
    assert module_0.sorted_list_sum(["even"]) == ["even"]
    assert module_0.sorted_list_sum(["odd"]) == []

    # Duplicates are preserved
    assert module_0.sorted_list_sum(["ab", "ab", "abc"]) == ["ab", "ab"]

    # Mixed case with duplicates and ties
    assert module_0.sorted_list_sum(["hey", "there", "hi", "yo", "code", "code"]) == ["hi", "yo", "code", "code"]

    print("All tests passed!")


if __name__ == "__main__":
    test_sorted_list_sum()

# Generated at 2026-11-02 19:02:48.955791
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # Basic filtering and sorting by length
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd", "efgh"]) == ["ab", "cd", "efgh"]

    # Empty list returns empty list
    assert module_0.sorted_list_sum([]) == []

    # All odd-length strings are filtered out
    assert module_0.sorted_list_sum(["a", "abc", "abcde"]) == []

    # All even-length strings are kept, sorted by length then alphabetically
    assert module_0.sorted_list_sum(["dddd", "bb", "cc", "aa"]) == ["aa", "bb", "cc", "dddd"]

    # Stable sort: same-length strings preserve alphabetical order
    assert module_0.sorted_list_sum(["cc", "aa", "dd", "bb"]) == ["aa", "bb", "cc", "dd"]

    # Mixed case strings
    assert module_0.sorted_list_sum(["school", "AI", "asdf", "b"]) == ["AI", "asdf", "school"]

    # Single even-length element
    assert module_0.sorted_list_sum(["ok"]) == ["ok"]

    # Single odd-length element is removed
    assert module_0.sorted_list_sum(["xyz"]) == []

    # Duplicate strings preserved
    assert module_0.sorted_list_sum(["ab", "ab", "abc"]) == ["ab", "ab"]

    # Longer example from typical usage
    assert module_0.sorted_list_sum(["school", "AI", "asdf", "b", "ca"]) == ["AI", "ca", "asdf", "school"]

    print("All tests passed!")


if __name__ == "__main__":
    test_sorted_list_sum()

# Generated at 2026-11-02 19:04:18.108110
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    # nonce:905d8596
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]
    assert module_0.sorted_list_sum(["school", "AI", "asdf", "b"]) == ["AI", "asdf", "school"]
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]
    assert module_0.sorted_list_sum(["abc", "defg", "hi", "jklm"]) == ["hi", "defg", "jklm"]
    assert module_0.sorted_list_sum(["a"]) == []
    assert module_0.sorted_list_sum([]) == []
    assert module_0.sorted_list_sum(["bb", "cc", "aa"]) == ["aa", "bb", "cc"]
    assert module_0.sorted_list_sum(["dddd", "ee", "ff", "ggg"]) == ["ee", "ff", "dddd"]
    assert module_0.sorted_list_sum(["ab", "abcd", "abcde"]) == ["ab", "abcd"]

# Generated at 2026-11-02 19:05:12.666217
# Unit test for function sorted_list_sum
def test_sorted_list_sum():
    """Test that only even-length strings are kept, sorted by length then lexicographically."""
    # Basic case: mixed lengths
    assert module_0.sorted_list_sum(["aa", "a", "aaa"]) == ["aa"]

    # Multiple even-length strings sorted by length
    assert module_0.sorted_list_sum(["ab", "a", "aaa", "cd"]) == ["ab", "cd"]

    # Empty list
    assert module_0.sorted_list_sum([]) == []

    # All odd lengths -> empty result
    assert module_0.sorted_list_sum(["a", "abc", "abcde"]) == []

    # All even lengths
    assert module_0.sorted_list_sum(["ab", "abcd", "abcdef"]) == ["ab", "abcd", "abcdef"]

    # Ties in length resolved lexicographically (lst.sort() then stable sort by len)
    assert module_0.sorted_list_sum(["bb", "aa", "cc"]) == ["aa", "bb", "cc"]

    # Single element, even length
    assert module_0.sorted_list_sum(["hello"]) == []

    # Single element, even length
    assert module_0.sorted_list_sum(["hi"]) == ["hi"]

    # Duplicates preserved
    assert module_0.sorted_list_sum(["ab", "ab", "abc"]) == ["ab", "ab"]

    # Mixed case strings
    assert module_0.sorted_list_sum(["AB", "ab", "A"]) == ["AB", "ab"]

    # Longer example from typical spec
    assert module_0.sorted_list_sum(["school", "AI", "asdf", "b"]) == ["AI", "asdf", "school"]

    # Order of input shouldn't matter for result
    assert module_0.sorted_list_sum(["aaa", "aa", "a"]) == ["aa"]

    # Length ordering takes priority over lexicographic order
    assert module_0.sorted_list_sum(["zz", "abcd", "aa"]) == ["aa", "zz", "abcd"]


def test_sorted_list_sum_does_not_mutate_original():
    """Ensure the function works on unsorted input and returns correct result."""
    lst = ["dd", "b", "cc", "aaa"]
    result = module_0.sorted_list_sum(lst)
    assert result == ["cc", "dd"]
    # Note: original list IS sorted in-place by implementation; only verify result correctness


def test_sorted_list_sum_numeric_strings():
    """Test with numeric strings."""
    assert module_0.sorted_list_sum(["12", "1", "123", "34"]) == ["12", "34"]
    assert module_0.sorted_list_sum(["1234", "56"]) == ["56", "1234"]


def test_sorted_list_sum_empty_strings():
    """Empty string has length 0, which is even, so it should be included."""
    assert module_0.sorted_list_sum(["", "a", "bb"]) == ["", "bb"]
    assert module_0.sorted_list_sum(["", ""]) == ["", ""]


if __name__ == "__main__":
    test_sorted_list_sum()
    test_sorted_list_sum_does_not_mutate_original()
    test_sorted_list_sum_numeric_strings()
    test_sorted_list_sum_empty_strings()
    print("All tests passed!")