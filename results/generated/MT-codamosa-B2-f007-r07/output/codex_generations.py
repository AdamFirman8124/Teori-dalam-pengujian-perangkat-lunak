

# Generated at 2026-11-02 09:14:59.668291
# Unit test for function filter_by_substring
def test_filter_by_substring():# Test basic filtering
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    
    # Test with substring 'a' returning multiple matches
    assert module_0.filter_by_substring(['apple', 'banana', 'cherry'], 'an') == ['banana']
    
    # Test with empty list
    assert module_0.filter_by_substring([], 'a') == []
    
    # Test with empty substring - should return all strings
    assert module_0.filter_by_substring(['abc', 'def', 'ghi'], '') == ['abc', 'def', 'ghi']
    
    # Test with substring not present in any string
    assert module_0.filter_by_substring(['hello', 'world'], 'xyz') == []
    
    # Test case sensitivity - uppercase vs lowercase
    assert module_0.filter_by_substring(['Hello', 'hello', 'HELLO'], 'hello') == ['hello']
    
    # Test substring equal to entire string
    assert module_0.filter_by_substring(['exact', 'other'], 'exact') == ['exact']
    
    # Test substring at beginning, middle, and end
    assert module_0.filter_by_substring(['prefix_suffix', 'middle_part', 'end_part'], 'part') == ['prefix_suffix', 'middle_part', 'end_part']
    
    # Test with single character substring
    assert module_0.filter_by_substring(['cat', 'dog', 'bird'], 'o') == ['dog']
    
    # Test with substring longer than some strings
    assert module_0.filter_by_substring(['ab', 'abc', 'abcdef'], 'abcd') == ['abcdef']
    
    # Test with special characters as substring
    assert module_0.filter_by_substring(['foo@bar', 'foo-bar', 'foobar'], '@') == ['foo@bar']
    
    # Test with substring containing spaces
    assert module_0.filter_by_substring(['hello world', 'helloworld', 'world hello'], 'hello world') == ['hello world']
    
    # Test order preservation
    result = module_0.filter_by_substring(['xyz_abc', 'abc_xyz', 'abc_abc'], 'abc')
    assert result == ['xyz_abc', 'abc_xyz', 'abc_abc']
    
    # Test with duplicates in input
    assert module_0.filter_by_substring(['dup', 'dup', 'nodup'], 'dup') == ['dup', 'dup', 'nodup']
    
    # Test with unicode characters
    assert module_0.filter_by_substring(['héllo', 'wörld'], 'ö') == ['wörld']
    
    # Test numeric strings
    assert module_0.filter_by_substring(['123', '456', '7890'], '45') == ['456']
    
    print("All tests passed!")

test_filter_by_substring()

# Generated at 2026-11-02 09:15:35.657374
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test with basic filtering
    assert module_0.filter_by_substring([], 'a') == []
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'b') == ['abc', 'bcd']
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'cd') == ['bcd', 'cde']

    # Test with no matches
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde'], 'xyz') == []

    # Test with empty substring (matches everything)
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']

    # Test with substring equal to full string
    assert module_0.filter_by_substring(['hello', 'world'], 'hello') == ['hello']

    # Test with substring appearing multiple times
    assert module_0.filter_by_substring(['aaa', 'aba', 'aaa'], 'aa') == ['aaa', 'aaa']

    # Test with case sensitivity
    assert module_0.filter_by_substring(['Apple', 'apple', 'APPLE'], 'apple') == ['apple']

    # Test with special characters
    assert module_0.filter_by_substring(['a.b', 'axb', 'a-b'], '.') == ['a.b']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-11-02 09:15:55.574739
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test basic substring filtering
    assert module_0.filter_by_substring([], 'a') == []
    
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'ab') == ['abc']
    
    assert module_0.filter_by_substring(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']
    
    # Test substring not found in any string
    assert module_0.filter_by_substring(['abc', 'def'], 'xyz') == []
    
    # Test empty substring matches everything
    assert module_0.filter_by_substring(['abc', 'def'], '') == ['abc', 'def']
    
    # Test case sensitivity
    assert module_0.filter_by_substring(['ABC', 'abc'], 'abc') == ['abc']
    
    # Test substring at start, middle, and end
    assert module_0.filter_by_substring(['hello', 'world hello', 'helloworld'], 'hello') == ['hello', 'world hello', 'helloworld']
    
    # Test single character substring
    assert module_0.filter_by_substring(['cat', 'dog', 'bird'], 'o') == ['dog']
    
    # Test substring longer than strings
    assert module_0.filter_by_substring(['ab', 'cd'], 'abcdef') == []
    
    # Test with special characters
    assert module_0.filter_by_substring(['a-b', 'a b', 'ab'], '-') == ['a-b']
    
    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-11-02 09:16:05.812035
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test with empty list
    assert module_0.filter_by_substring([], 'a') == []

    # Test with substring present in all elements
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde'], 'a') == ['abc', 'bacd']

    # Test with substring present in some elements
    assert module_0.filter_by_substring(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']

    # Test with substring not present in any element
    assert module_0.filter_by_substring(['hello', 'world'], 'zzz') == []

    # Test with empty substring (matches everything)
    assert module_0.filter_by_substring(['a', 'b', 'c'], '') == ['a', 'b', 'c']

    # Test with substring equal to entire string
    assert module_0.filter_by_substring(['test', 'other'], 'test') == ['test']

    # Test with case sensitivity
    assert module_0.filter_by_substring(['Apple', 'apple', 'APPLE'], 'apple') == ['apple']

    # Test with multi-character substring
    assert module_0.filter_by_substring(['football', 'baseball', 'basketball'], 'ball') == ['football', 'baseball', 'basketball']

    # Test with duplicate elements
    assert module_0.filter_by_substring(['abc', 'abc', 'xyz'], 'abc') == ['abc', 'abc']

    # Test with special characters in substring
    assert module_0.filter_by_substring(['a-b', 'ab', 'a b'], '-') == ['a-b']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-11-02 09:16:14.724470
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test with multiple matches
    assert module_0.filter_by_substring(['apple', 'banana', 'grape'], 'an') == ['banana']
    
    # Test with multiple matching elements
    assert module_0.filter_by_substring(['apple', 'banana', 'apricot'], 'ap') == ['apple', 'apricot']
    
    # Test with no matches
    assert module_0.filter_by_substring(['apple', 'banana', 'grape'], 'zzz') == []
    
    # Test with empty input list
    assert module_0.filter_by_substring([], 'abc') == []
    
    # Test with empty substring (everything matches)
    assert module_0.filter_by_substring(['apple', 'banana'], '') == ['apple', 'banana']
    
    # Test with substring equal to full string
    assert module_0.filter_by_substring(['apple', 'banana'], 'apple') == ['apple']
    
    # Test case sensitivity
    assert module_0.filter_by_substring(['Apple', 'apple'], 'apple') == ['apple']
    
    # Test with substring longer than any string
    assert module_0.filter_by_substring(['a', 'b'], 'abc') == []
    
    # Test order preservation
    result = module_0.filter_by_substring(['xxaxx', 'xxbxx', 'xxaxx'], 'a')
    assert result == ['xxaxx', 'xxaxx']
    
    # Test with all elements matching
    assert module_0.filter_by_substring(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']
    
    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()