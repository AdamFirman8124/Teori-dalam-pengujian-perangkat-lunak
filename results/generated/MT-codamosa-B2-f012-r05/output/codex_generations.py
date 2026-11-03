

# Generated at 2026-11-03 03:27:40.890431
# Unit test for function longest
def test_longest():
    # Test with empty list
    assert module_0.longest([]) is None

    # Test with a single string
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Test with multiple strings of different lengths
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["ccc", "bb", "a"]) == "ccc"
    assert module_0.longest(["bb", "ccc", "a"]) == "ccc"

    # Test with multiple strings of the same max length (should return the first)
    assert module_0.longest(["a", "bb", "cc"]) == "bb"
    assert module_0.longest(["xx", "yy", "zz"]) == "xx"

    # Test with strings containing empty strings
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["", ""]) == ""

    # Test with longer realistic strings
    assert module_0.longest(["apple", "banana", "cherry"]) == "banana"
    assert module_0.longest(["one", "two", "three", "four", "five"]) == "three"

    print("All tests passed!")


if __name__ == "__main__":
    test_longest()

# Generated at 2026-11-03 03:29:42.538749
# Unit test for function longest
def test_longest():
    # Empty list returns None
    assert module_0.longest([]) is None

    # Single element list returns that element
    assert module_0.longest(["hello"]) == "hello"
    assert module_0.longest([""]) == ""

    # Multiple elements, unique max length
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["ccc", "bb", "a"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"

    # Ties: first occurrence of max length wins
    assert module_0.longest(["a", "bb", "cc"]) == "bb"
    assert module_0.longest(["xx", "yy", "z"]) == "xx"
    assert module_0.longest(["abc", "def", "gh"]) == "abc"

    # All elements same length: first one returned
    assert module_0.longest(["a", "b", "c"]) == "a"
    assert module_0.longest(["ab", "cd", "ef"]) == "ab"

    # Contains empty strings among others
    assert module_0.longest(["", "a", ""]) == "a"
    assert module_0.longest(["", ""]) == ""

    # Longer strings later in the list
    assert module_0.longest(["a", "abc", "ab", "abcd"]) == "abcd"

    # Whitespace and special characters
    assert module_0.longest(["a b", "ab", "!!!"]) == "!!!"
    assert module_0.longest(["line1", "longer line"]) == "longer line"

    # Unicode strings
    assert module_0.longest(["héllo", "hi", "wörld!"]) == "wörld!"

    # Very long string vs short ones
    assert module_0.longest(["x", "x" * 1000, "xx"]) == "x" * 1000

    print("All tests passed!")


if __name__ == "__main__":
    test_longest()

# Generated at 2026-11-03 03:31:19.612271
# Unit test for function longest
def test_longest():
    # Empty list returns None
    assert module_0.longest([]) is None

    # Single element list returns that element
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["abc"]) == "abc"

    # Multiple elements: returns the first longest
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["cat", "dog", "elephant", "bird"]) == "elephant"

    # Ties: returns the first occurrence of the max length
    assert module_0.longest(["aa", "bb", "c"]) == "aa"
    assert module_0.longest(["x", "yy", "zz", "w"]) == "yy"
    assert module_0.longest(["a", "b", "c"]) == "a"

    # All strings same length: returns first
    assert module_0.longest(["ab", "cd", "ef"]) == "ab"

    # Strings with spaces count toward length
    assert module_0.longest(["a b", "ab"]) == "a b"

    # Empty string among non-empty strings
    assert module_0.longest(["", "a", ""]) == "a"

    # List of empty strings returns empty string
    assert module_0.longest(["", ""]) == ""

# Generated at 2026-11-03 03:33:11.945907
# Unit test for function longest
def test_longest():
    # Test empty list returns None
    assert module_0.longest([]) is None

    # Test single element list
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest(["hello"]) == "hello"

    # Test list with unique longest string
    assert module_0.longest(["a", "bb", "ccc"]) == "ccc"
    assert module_0.longest(["abc", "ab", "a"]) == "abc"

    # Test longest string appears first
    assert module_0.longest(["cccc", "a", "bb"]) == "cccc"

    # Test tie returns first occurrence of max length
    assert module_0.longest(["ab", "cd", "e"]) == "ab"
    assert module_0.longest(["a", "bb", "cc"]) == "bb"

    # Test all strings same length returns first
    assert module_0.longest(["a", "b", "c"]) == "a"
    assert module_0.longest(["xx", "yy", "zz"]) == "xx"

    # Test with empty string in list
    assert module_0.longest(["", "a"]) == "a"
    assert module_0.longest(["", ""]) == ""
    assert module_0.longest([""]) == ""

    # Test with strings containing spaces and special characters
    assert module_0.longest(["hello world", "hi", "hey"]) == "hello world"
    assert module_0.longest(["!!!", "??", "."]) == "!!!"

    # Test with longer lists
    assert module_0.longest(["one", "two", "three", "four", "five"]) == "three"
    assert module_0.longest(["a" * 100, "b" * 50]) == "a" * 100

    # Test duplicates
    assert module_0.longest(["abc", "abc", "ab"]) == "abc"
    assert module_0.longest(["ab", "ab", "ab"]) == "ab"

    # Test unicode strings
    assert module_0.longest(["héllo", "hi"]) == "héllo"
    assert module_0.longest(["日本語", "en"]) == "日本語"

    # Test None input behavior for non-list falsy input
    assert module_0.longest(()) is None

# Generated at 2026-11-03 03:35:26.398622
# Unit test for function longest
def test_longest():
    # Empty list should return None
    assert module_0.longest([]) is None

    # Single element list
    assert module_0.longest(["a"]) == "a"
    assert module_0.longest([""]) == ""

    # Longest string in the middle
    assert module_0.longest(["a", "bb", "c"]) == "bb"

    # Longest string at the end
    assert module_0.longest(["a", "b", "ccc"]) == "ccc"

    # Longest string at the beginning
    assert module_0.longest(["hello", "hi", "hey"]) == "hello"

    # Tie in length: first occurrence should be returned
    assert module_0.longest(["ab", "cd", "e"]) == "ab"
    assert module_0.longest(["x", "yy", "zz"]) == "yy"

    # All strings same length: first one returned
    assert module_0.longest(["a", "b", "c"]) == "a"

    # Strings with spaces and special characters
    assert module_0.longest(["one two", "three", "!!"]) == "one two"

    # Long list
    assert module_0.longest(["a" * 10, "b" * 5, "c" * 15, "d" * 2]) == "c" * 15

    print("All test_longest tests passed!")


if __name__ == "__main__":
    test_longest()