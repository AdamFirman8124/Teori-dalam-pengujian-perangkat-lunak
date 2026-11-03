

# Generated at 2026-11-02 12:40:44.446934
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test basic filtering
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    
    # Test prefix matching multiple strings
    assert module_0.filter_by_prefix(['apple', 'banana', 'apricot', 'cherry'], 'ap') == ['apple', 'apricot']
    
    # Test no matches
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'z') == []
    
    # Test empty prefix returns all strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']
    
    # Test empty input list
    assert module_0.filter_by_prefix([], 'a') == []
    
    # Test exact match (string equals prefix)
    assert module_0.filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']
    
    # Test prefix longer than strings
    assert module_0.filter_by_prefix(['a', 'ab'], 'abc') == []
    
    # Test case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple'], 'A') == ['Apple']
    
    # Test single element list
    assert module_0.filter_by_prefix(['hello'], 'he') == ['hello']
    
    # Test order preservation
    assert module_0.filter_by_prefix(['cat', 'car', 'dog', 'cab'], 'ca') == ['cat', 'car', 'cab']
    
    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-02 12:44:11.147503
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test basic filtering with a common prefix
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # Test filtering with prefix that matches nothing
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z') == []

    # Test with empty prefix (should return all strings)
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], '') == ['abc', 'bcd', 'cde', 'array']

    # Test with empty input list
    assert module_0.filter_by_prefix([], 'a') == []

    # Test with exact match prefix equal to full string
    assert module_0.filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']

    # Test case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple', 'APPLE'], 'A') == ['Apple', 'APPLE']

    # Test prefix longer than some strings
    assert module_0.filter_by_prefix(['ab', 'abc'], 'abc') == ['abc']

    # Test single-element list
    assert module_0.filter_by_prefix(['hello'], 'he') == ['hello']
    assert module_0.filter_by_prefix(['hello'], 'lo') == []

    # Test with multi-character prefix
    assert module_0.filter_by_prefix(['dog', 'deer', 'dot', 'cat'], 'do') == ['dog', 'dot']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-02 12:46:49.116315
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with a common prefix
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    
    # Test with empty string list
    assert module_0.filter_by_prefix([], 'a') == []
    
    # Test with empty prefix (should return all strings)
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']
    
    # Test with prefix that matches nothing
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'z') == []
    
    # Test with prefix matching entire string
    assert module_0.filter_by_prefix(['abc', 'abcdef'], 'abc') == ['abc', 'abcdef']
    
    # Test with prefix longer than some strings
    assert module_0.filter_by_prefix(['ab', 'abc'], 'abc') == ['abc']
    
    # Test case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple'], 'a') == ['apple']
    
    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()