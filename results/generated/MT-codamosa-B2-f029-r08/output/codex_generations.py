

# Generated at 2026-11-03 06:18:33.496046
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with empty list
    assert module_0.filter_by_prefix([], "a") == []

    # Test with empty prefix (should return all strings)
    assert module_0.filter_by_prefix(["abc", "def", "ghi"], "") == ["abc", "def", "ghi"]

    # Test with prefix matching some strings
    assert module_0.filter_by_prefix(["abc", "bcd", "cde", "array"], "a") == ["abc", "array"]

    # Test with prefix matching no strings
    assert module_0.filter_by_prefix(["abc", "bcd", "cde"], "z") == []

    # Test with prefix matching all strings
    assert module_0.filter_by_prefix(["abc", "abcd", "abcde"], "abc") == ["abc", "abcd", "abcde"]

    # Test case sensitivity
    assert module_0.filter_by_prefix(["Apple", "apple", "APple"], "ap") == ["apple"]

    # Test with single character prefix
    assert module_0.filter_by_prefix(["cat", "dog", "cow"], "c") == ["cat", "cow"]

    # Test with longer prefix than some strings
    assert module_0.filter_by_prefix(["ab", "abc"], "abc") == ["abc"]

    # Test that order is preserved
    result = module_0.filter_by_prefix(["axe", "bat", "ant", "bee"], "a")
    assert result == ["axe", "ant"]

    # Test with duplicate strings
    assert module_0.filter_by_prefix(["foo", "foo", "bar"], "foo") == ["foo", "foo"]

    # Test with prefix equal to full string
    assert module_0.filter_by_prefix(["hello", "world"], "hello") == ["hello"]

    # Test with special characters
    assert module_0.filter_by_prefix(["#tag", "tag", "#comment"], "#") == ["#tag", "#comment"]

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-03 06:19:29.820483
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with an empty list
    assert module_0.filter_by_prefix([], 'a') == []

    # Test with an empty prefix (should return all strings)
    assert module_0.filter_by_prefix(['abc', 'def', 'abd'], '') == ['abc', 'def', 'abd']

    # Test with a prefix that matches some strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # Test with a prefix that matches no strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z') == []

    # Test with a prefix matching all strings
    assert module_0.filter_by_prefix(['abc', 'abd', 'abcde'], 'ab') == ['abc', 'abd', 'abcde']

    # Test with a prefix that is an exact string match
    assert module_0.filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']

    # Test with single-character strings
    assert module_0.filter_by_prefix(['a', 'b', 'c', 'ab'], 'a') == ['a', 'ab']

    # Test with prefix longer than some strings
    assert module_0.filter_by_prefix(['a', 'ab', 'abc'], 'abc') == ['abc']

    # Test with duplicate strings
    assert module_0.filter_by_prefix(['abc', 'abc', 'bcd'], 'abc') == ['abc', 'abc']

    # Test case sensitivity
    assert module_0.filter_by_prefix(['ABC', 'abc'], 'a') == ['abc']

    # Test with strings containing spaces and special characters
    assert module_0.filter_by_prefix(['hello world', 'help', 'hell'], 'hell') == ['hello world', 'hell']

    print("All test_filter_by_prefix tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-03 06:20:39.463109
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with an empty list
    assert module_0.filter_by_prefix([], 'a') == []

    # Test with an empty prefix (should return all strings)
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], '') == ['abc', 'bcd', 'cde', 'array']

    # Test with a common prefix
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # Test with a multi-character prefix
    assert module_0.filter_by_prefix(['abc', 'abcd', 'abcde', 'xyz'], 'abc') == ['abc', 'abcd', 'abcde']

    # Test with a prefix that matches nothing
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z') == []

    # Test case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple', 'APPLY'], 'a') == ['apple']

    # Test prefix equal to a full string
    assert module_0.filter_by_prefix(['hello', 'world'], 'hello') == ['hello']

    # Test single element list
    assert module_0.filter_by_prefix(['test'], 't') == ['test']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-03 06:21:38.742882
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with a common prefix
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    
    # Test with prefix matching all strings
    assert module_0.filter_by_prefix(['apple', 'application', 'appetite'], 'app') == ['apple', 'application', 'appetite']
    
    # Test with prefix matching some strings
    assert module_0.filter_by_prefix(['dog', 'cat', 'dove', 'duck'], 'd') == ['dog', 'dove', 'duck']
    
    # Test with no matching strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'z') == []
    
    # Test with empty prefix (should return all strings)
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']
    
    # Test with empty list
    assert module_0.filter_by_prefix([], 'a') == []
    
    # Test with empty list and empty prefix
    assert module_0.filter_by_prefix([], '') == []
    
    # Test case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple', 'APPLE'], 'a') == ['apple']
    
    # Test where a string equals the prefix exactly
    assert module_0.filter_by_prefix(['abc', 'abcdef'], 'abc') == ['abc', 'abcdef']
    
    # Test with prefix longer than some strings
    assert module_0.filter_by_prefix(['a', 'ab', 'abc'], 'abc') == ['abc']
    
    # Test order preservation
    assert module_0.filter_by_prefix(['ax', 'ay', 'az', 'bx'], 'a') == ['ax', 'ay', 'az']
    
    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-03 06:22:26.253980
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with empty list
    assert module_0.filter_by_prefix([], "a") == []

    # Test with no matches
    assert module_0.filter_by_prefix(["apple", "banana"], "c") == []

    # Test with matches
    assert module_0.filter_by_prefix(["abc", "bcd", "cde", "array"], "a") == ["abc", "array"]

    # Test with empty prefix (matches all strings)
    assert module_0.filter_by_prefix(["abc", "bcd"], "") == ["abc", "bcd"]

    # Test with prefix equal to full string
    assert module_0.filter_by_prefix(["abc", "abcd"], "abc") == ["abc", "abcd"]

    # Test with case sensitivity
    assert module_0.filter_by_prefix(["Apple", "apple"], "a") == ["apple"]

    # Test with duplicate strings
    assert module_0.filter_by_prefix(["abc", "abc", "abd"], "ab") == ["abc", "abc", "abd"]

    # Test preserving original order
    assert module_0.filter_by_prefix(["bca", "abc", "acb"], "a") == ["abc", "acb"]