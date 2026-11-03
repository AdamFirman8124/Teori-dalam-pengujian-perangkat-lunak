

# Generated at 2026-11-03 02:45:15.913282
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test with empty list
    assert module_0.filter_by_substring([], 'a') == []

    # Test basic filtering
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'b') == ['abc', 'bcd']
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'cd') == ['bcd', 'cde']

    # Test with empty substring (matches everything)
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']

    # Test with substring not present in any string
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde'], 'xyz') == []

    # Test with exact match
    assert module_0.filter_by_substring(['abc'], 'abc') == ['abc']

    # Test case sensitivity
    assert module_0.filter_by_substring(['ABC', 'abc', 'Abc'], 'a') == ['abc']

    # Test with duplicate strings
    assert module_0.filter_by_substring(['aaa', 'aaa', 'bbb'], 'a') == ['aaa', 'aaa']

    # Test substring appearing multiple times in one string
    assert module_0.filter_by_substring(['banana', 'bandana'], 'an') == ['banana', 'bandana']

    # Test substring at start and end of strings
    assert module_0.filter_by_substring(['prefix_middle', 'middle_suffix'], 'prefix') == ['prefix_middle', 'middle_suffix']

    # Test single character strings
    assert module_0.filter_by_substring(['a', 'b', 'c'], 'b') == ['b']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-11-03 02:47:33.845643
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test with basic substring filtering
    assert module_0.filter_by_substring([], 'a') == []
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'b') == ['abc', 'bcd']

    # Test with empty substring (matches everything)
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']

    # Test with substring not present in any string
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde'], 'z') == []

    # Test with substring equal to the whole string
    assert module_0.filter_by_substring(['hello', 'world'], 'hello') == ['hello']

    # Test with case sensitivity
    assert module_0.filter_by_substring(['Apple', 'apple', 'APPLE'], 'apple') == ['apple']

    # Test with substring appearing multiple times in a string
    assert module_0.filter_by_substring(['aaa', 'aba', 'abc'], 'a') == ['aaa', 'aba', 'abc']

    # Test with single-character strings
    assert module_0.filter_by_substring(['a', 'b', 'a'], 'a') == ['a', 'a']

    # Test with special characters
    assert module_0.filter_by_substring(['a-b', 'ab', 'a b'], '-') == ['a-b']

    # Test preserving order of input
    assert module_0.filter_by_substring(['xyz', 'abc', 'xqz', 'axb'], 'x') == ['xyz', 'xqz', 'axb']

    # Test with longer substrings
    assert module_0.filter_by_substring(['programming', 'program', 'gram'], 'gram') == ['programming', 'program', 'gram']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-11-03 02:50:03.056114
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test basic filtering
    assert module_0.filter_by_substring([], 'a') == []
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'ab') == ['abc']
    
    # Test substring not found in any string
    assert module_0.filter_by_substring(['abc', 'def', 'ghi'], 'xyz') == []
    
    # Test all strings contain the substring
    assert module_0.filter_by_substring(['xxx', 'xxx', 'xxx'], 'x') == ['xxx', 'xxx', 'xxx']
    
    # Test empty substring matches everything
    assert module_0.filter_by_substring(['abc', 'def'], '') == ['abc', 'def']
    
    # Test case sensitivity
    assert module_0.filter_by_substring(['Apple', 'apple', 'APPLE'], 'apple') == ['apple']
    
    # Test substring at beginning, middle, and end
    assert module_0.filter_by_substring(['prefix_middle_suffix'], 'middle') == ['prefix_middle_suffix']
    assert module_0.filter_by_substring(['hello', 'world'], 'hello') == ['hello']
    assert module_0.filter_by_substring(['world', 'hello'], 'hello') == ['hello']
    
    # Test with duplicate strings
    assert module_0.filter_by_substring(['aa', 'bb', 'aa'], 'a') == ['aa', 'aa']
    
    # Test single character substring
    assert module_0.filter_by_substring(['cat', 'dog', 'bird'], 'o') == ['dog', 'bird']
    
    # Test substring longer than strings
    assert module_0.filter_by_substring(['a', 'b'], 'abc') == []
    
    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-11-03 02:51:26.814729
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test with empty list
    assert module_0.filter_by_substring([], 'a') == []

    # Test with basic substring filtering
    assert module_0.filter_by_substring(['abc', 'bacd', 'array'], 'a') == ['abc', 'bacd', 'array']

    # Test with substring that matches only some elements
    assert module_0.filter_by_substring(['apple', 'banana', 'cherry'], 'an') == ['banana']

    # Test with substring not present in any element
    assert module_0.filter_by_substring(['hello', 'world'], 'xyz') == []

    # Test with empty substring (matches all)
    assert module_0.filter_by_substring(['one', 'two', 'three'], '') == ['one', 'two', 'three']

    # Test with exact match
    assert module_0.filter_by_substring(['cat', 'catalog', 'dog'], 'cat') == ['cat', 'catalog']

    # Test with case sensitivity
    assert module_0.filter_by_substring(['Apple', 'apple'], 'Apple') == ['Apple']

    # Test with single element list
    assert module_0.filter_by_substring(['single'], 'ing') == ['single']

    # Test with duplicate elements
    assert module_0.filter_by_substring(['aa', 'ab', 'aa'], 'a') == ['aa', 'ab', 'aa']

    # Test with substring containing special characters
    assert module_0.filter_by_substring(['a-b', 'ab', 'c-d'], '-') == ['a-b', 'c-d']

    # Test with longer substring
    assert module_0.filter_by_substring(['xxx', 'asd', 'xxy', 'john doe', 'johnSmith'], 'john') == ['john doe', 'johnSmith']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-11-03 02:52:17.052154
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Basic filtering
    assert module_0.filter_by_substring([], 'a') == []
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'b') == ['abc', 'bcd']

    # Substring not present
    assert module_0.filter_by_substring(['abc', 'def'], 'xyz') == []

    # Substring matches all elements
    assert module_0.filter_by_substring(['aaa', 'aab', 'aac'], 'a') == ['aaa', 'aab', 'aac']

    # Empty substring matches everything
    assert module_0.filter_by_substring(['abc', 'def'], '') == ['abc', 'def']

    # Case sensitivity
    assert module_0.filter_by_substring(['ABC', 'abc', 'Abc'], 'abc') == ['abc']

    # Substring appears at start, middle, and end
    assert module_0.filter_by_substring(['prefix_sub', 'mid_sub_mid', 'sub_suffix'], 'sub') == [
        'prefix_sub', 'mid_sub_mid', 'sub_suffix'
    ]

    # Single-element list
    assert module_0.filter_by_substring(['hello'], 'ell') == ['hello']
    assert module_0.filter_by_substring(['hello'], 'world') == []

    # Duplicate elements preserved
    assert module_0.filter_by_substring(['ab', 'ab', 'cd'], 'ab') == ['ab', 'ab']

    # Order preserved
    result = module_0.filter_by_substring(['xxa', 'yya', 'zza'], 'a')
    assert result == ['xxa', 'yya', 'zza']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()