

# Generated at 2026-11-02 19:28:48.876590
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Basic case: multiple matches
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    
    # Substring appears in the middle
    assert module_0.filter_by_substring(['hello', 'world', 'shell'], 'ell') == ['hello', 'shell']
    
    # No matches
    assert module_0.filter_by_substring(['abc', 'def'], 'xyz') == []
    
    # Empty input list
    assert module_0.filter_by_substring([], 'a') == []
    
    # Empty substring matches everything
    assert module_0.filter_by_substring(['abc', 'def'], '') == ['abc', 'def']
    
    # Case sensitivity check
    assert module_0.filter_by_substring(['ABC', 'abc'], 'a') == ['abc']
    
    # Substring equals full string
    assert module_0.filter_by_substring(['test'], 'test') == ['test']
    
    # Multiple occurrences within a string count once
    assert module_0.filter_by_substring(['aaab', 'baaa', 'abab'], 'aa') == ['aaab', 'baaa']
    
    # Order preservation
    result = module_0.filter_by_substring(['xyz', 'abc', 'xyc', 'ab'], 'xy')
    assert result == ['xyz', 'xyc']
    
    # Duplicate strings are all kept
    assert module_0.filter_by_substring(['dog', 'dog', 'cat'], 'dog') == ['dog', 'dog']

# Generated at 2026-11-02 19:30:15.541746
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test with basic filtering
    assert module_0.filter_by_substring([], 'a') == []
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    
    # Test with substring 'b'
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'b') == ['abc', 'bacd']
    
    # Test with substring that matches nothing
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z') == []
    
    # Test with empty substring (should match all strings)
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde'], '') == ['abc', 'bacd', 'cde']
    
    # Test with substring equal to full string
    assert module_0.filter_by_substring(['hello', 'world'], 'hello') == ['hello']
    
    # Test with case sensitivity
    assert module_0.filter_by_substring(['Apple', 'apple', 'APPLE'], 'apple') == ['apple']
    
    # Test with substring appearing multiple times in a string
    assert module_0.filter_by_substring(['aaab', 'abab', 'abba'], 'ab') == ['aaab', 'abab', 'abba']
    
    # Test with single element list
    assert module_0.filter_by_substring(['xyz'], 'x') == ['xyz']
    assert module_0.filter_by_substring(['xyz'], 'y') == ['xyz']
    assert module_0.filter_by_substring(['xyz'], 'z') == ['xyz']
    assert module_0.filter_by_substring(['xyz'], 'w') == []
    
    # Test with special characters
    assert module_0.filter_by_substring(['a-b', 'a b', 'ab'], '-') == ['a-b']
    assert module_0.filter_by_substring(['one@two', 'one two', 'onetwo'], '@') == ['one@two']
    
    # Test with whitespace substring
    assert module_0.filter_by_substring(['hello world', 'helloworld', 'world hello'], ' ') == ['hello world', 'world hello']
    
    # Test preserving order of input
    assert module_0.filter_by_substring(['ba', 'ab', 'cab', 'abc'], 'ab') == ['ab', 'cab', 'abc']
    
    # Test with longer substring
    assert module_0.filter_by_substring(['testing', 'resting', 'nesting', 'test'], 'test') == ['testing', 'test']
    
    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-11-02 19:32:25.375548
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test basic filtering
    assert module_0.filter_by_substring([], 'a') == []
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde'], 'a') == ['abc', 'bacd']
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde'], 'ab') == ['abc']
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde'], 'cd') == ['bacd', 'cde']

    # Test no matches
    assert module_0.filter_by_substring(['abc', 'def'], 'xyz') == []

    # Test all matches
    assert module_0.filter_by_substring(['aaa', 'aaa', 'aaa'], 'a') == ['aaa', 'aaa', 'aaa']

    # Test empty substring matches everything
    assert module_0.filter_by_substring(['abc', 'def'], '') == ['abc', 'def']

    # Test case sensitivity
    assert module_0.filter_by_substring(['ABC', 'abc'], 'a') == ['abc']
    assert module_0.filter_by_substring(['ABC', 'abc'], 'A') == ['ABC']

    # Test substring at start/end
    assert module_0.filter_by_substring(['hello', 'world'], 'he') == ['hello']
    assert module_0.filter_by_substring(['hello', 'world'], 'lo') == ['hello']

    # Test with duplicates
    assert module_0.filter_by_substring(['xx', 'yy', 'xx'], 'x') == ['xx', 'xx']

    # Test substring longer than strings
    assert module_0.filter_by_substring(['ab', 'cd'], 'abc') == []


if __name__ == "__main__":
    test_filter_by_substring()
    print("All tests passed!")

# Generated at 2026-11-02 19:34:01.418524
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test with empty list
    assert module_0.filter_by_substring([], 'a') == []

    # Test with no matches
    assert module_0.filter_by_substring(['abc', 'def'], 'xyz') == []

    # Test with all matches
    assert module_0.filter_by_substring(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']

    # Test with some matches
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # Test with empty substring (matches everything)
    assert module_0.filter_by_substring(['abc', 'def'], '') == ['abc', 'def']

    # Test with substring equal to whole string
    assert module_0.filter_by_substring(['hello', 'world'], 'hello') == ['hello']

    # Test with substring appearing in middle
    assert module_0.filter_by_substring(['xxabcxx', 'xbc'], 'abc') == ['xxabcxx']

    # Test with duplicate strings
    assert module_0.filter_by_substring(['aa', 'aa', 'bb'], 'aa') == ['aa', 'aa']

    # Test with special characters
    assert module_0.filter_by_substring(['a@b', 'ab'], '@') == ['a@b']

    # Test case sensitivity
    assert module_0.filter_by_substring(['ABC', 'abc'], 'abc') == ['abc']

    # Test with single-character strings
    assert module_0.filter_by_substring(['a', 'b', 'a'], 'a') == ['a', 'a']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-11-02 19:36:09.342258
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Basic case: filter strings containing the substring
    assert module_0.filter_by_substring([], 'a') == []
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'b') == ['abc', 'bcd']
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'cd') == ['bcd', 'cde']
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'z') == []

    # Substring matching entire string
    assert module_0.filter_by_substring(['hello', 'world'], 'hello') == ['hello']

    # Empty substring matches everything
    assert module_0.filter_by_substring(['abc', 'def'], '') == ['abc', 'def']

    # Case sensitivity check
    assert module_0.filter_by_substring(['ABC', 'abc'], 'abc') == ['abc']

    # Multiple occurrences of substring still match once
    assert module_0.filter_by_substring(['aaa', 'aba', 'aaa'], 'a') == ['aaa', 'aba', 'aaa']

    # Single element list
    assert module_0.filter_by_substring(['test'], 'test') == ['test']
    assert module_0.filter_by_substring(['test'], 'testing') == []

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()