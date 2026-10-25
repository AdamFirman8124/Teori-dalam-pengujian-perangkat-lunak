

# Generated at 2026-10-24 19:17:38.447175
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Basic: substring present
    assert module_0.filter_by_substring(["hello", "world", "hi"], "h") == ["hello", "hi"]

    # No matches -> empty list
    assert module_0.filter_by_substring(["abc", "def"], "z") == []

    # Empty substring matches every string (Python `"" in x` is True)
    assert module_0.filter_by_substring(["a", "b"], "") == ["a", "b"]

    # Empty input list
    assert module_0.filter_by_substring([], "a") == []

    # Substring equal to whole string
    assert module_0.filter_by_substring(["cat", "dog"], "cat") == ["cat"]

    # Case sensitivity: "H" should not match "hello"
    assert module_0.filter_by_substring(["hello", "Hello"], "H") == ["Hello"]

    # Order preserved
    assert module_0.filter_by_substring(["banana", "apple", "bandana"], "ban") == ["banana", "bandana"]

    # Substring longer than any element
    assert module_0.filter_by_substring(["a", "bb"], "aaa") == []

    # Duplicates preserved
    assert module_0.filter_by_substring(["aa", "aa", "b"], "a") == ["aa", "aa"]

    print("All tests passed")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-10-24 19:17:39.766531
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Basic: substring present
    assert module_0.filter_by_substring(["hello", "world", "hi"], "h") == ["hello", "hi"]

    # No matches -> empty list
    assert module_0.filter_by_substring(["abc", "def"], "z") == []

    # Empty substring matches every string (Python `"" in x` is True)
    assert module_0.filter_by_substring(["a", "b"], "") == ["a", "b"]

    # Empty input list
    assert module_0.filter_by_substring([], "a") == []

    # Substring equal to whole string
    assert module_0.filter_by_substring(["cat", "dog"], "cat") == ["cat"]

    # Case sensitivity: "H" should not match "hello"
    assert module_0.filter_by_substring(["hello", "Hello"], "H") == ["Hello"]

    # Order preserved
    assert module_0.filter_by_substring(["banana", "apple", "bandana"], "ban") == ["banana", "bandana"]

    # Substring longer than any element
    assert module_0.filter_by_substring(["a", "bb"], "aaa") == []

    # Duplicates preserved
    assert module_0.filter_by_substring(["aa", "aa", "b"], "a") == ["aa", "aa"]

    print("All tests passed")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-10-24 19:17:41.083523
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Basic: substring present
    assert module_0.filter_by_substring(["hello", "world", "hi"], "h") == ["hello", "hi"]

    # No matches -> empty list
    assert module_0.filter_by_substring(["abc", "def"], "z") == []

    # Empty substring matches every string (Python `"" in x` is True)
    assert module_0.filter_by_substring(["a", "b"], "") == ["a", "b"]

    # Empty input list
    assert module_0.filter_by_substring([], "a") == []

    # Substring equal to whole string
    assert module_0.filter_by_substring(["cat", "dog"], "cat") == ["cat"]

    # Case sensitivity: "H" should not match "hello"
    assert module_0.filter_by_substring(["hello", "Hello"], "H") == ["Hello"]

    # Order preserved
    assert module_0.filter_by_substring(["banana", "apple", "bandana"], "ban") == ["banana", "bandana"]

    # Substring longer than any element
    assert module_0.filter_by_substring(["a", "bb"], "aaa") == []

    # Duplicates preserved
    assert module_0.filter_by_substring(["aa", "aa", "b"], "a") == ["aa", "aa"]

    print("All tests passed")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-10-24 19:17:42.396298
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Basic: substring present
    assert module_0.filter_by_substring(["hello", "world", "hi"], "h") == ["hello", "hi"]

    # No matches -> empty list
    assert module_0.filter_by_substring(["abc", "def"], "z") == []

    # Empty substring matches every string (Python `"" in x` is True)
    assert module_0.filter_by_substring(["a", "b"], "") == ["a", "b"]

    # Empty input list
    assert module_0.filter_by_substring([], "a") == []

    # Substring equal to whole string
    assert module_0.filter_by_substring(["cat", "dog"], "cat") == ["cat"]

    # Case sensitivity: "H" should not match "hello"
    assert module_0.filter_by_substring(["hello", "Hello"], "H") == ["Hello"]

    # Order preserved
    assert module_0.filter_by_substring(["banana", "apple", "bandana"], "ban") == ["banana", "bandana"]

    # Substring longer than any element
    assert module_0.filter_by_substring(["a", "bb"], "aaa") == []

    # Duplicates preserved
    assert module_0.filter_by_substring(["aa", "aa", "b"], "a") == ["aa", "aa"]

    print("All tests passed")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-10-24 19:17:43.730148
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Basic: substring present
    assert module_0.filter_by_substring(["hello", "world", "hi"], "h") == ["hello", "hi"]

    # No matches -> empty list
    assert module_0.filter_by_substring(["abc", "def"], "z") == []

    # Empty substring matches every string (Python `"" in x` is True)
    assert module_0.filter_by_substring(["a", "b"], "") == ["a", "b"]

    # Empty input list
    assert module_0.filter_by_substring([], "a") == []

    # Substring equal to whole string
    assert module_0.filter_by_substring(["cat", "dog"], "cat") == ["cat"]

    # Case sensitivity: "H" should not match "hello"
    assert module_0.filter_by_substring(["hello", "Hello"], "H") == ["Hello"]

    # Order preserved
    assert module_0.filter_by_substring(["banana", "apple", "bandana"], "ban") == ["banana", "bandana"]

    # Substring longer than any element
    assert module_0.filter_by_substring(["a", "bb"], "aaa") == []

    # Duplicates preserved
    assert module_0.filter_by_substring(["aa", "aa", "b"], "a") == ["aa", "aa"]

    print("All tests passed")


if __name__ == "__main__":
    test_filter_by_substring()