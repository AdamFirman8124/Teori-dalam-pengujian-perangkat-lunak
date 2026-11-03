

# Generated at 2026-11-02 22:58:52.018820
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test with normal filtering
    assert module_0.filter_by_substring([], 'a') == []
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'ab') == ['abc']
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'cd') == ['bacd', 'cde']

    # Test with no matches
    assert module_0.filter_by_substring(['abc', 'def'], 'xyz') == []

    # Test with empty substring (matches everything)
    assert module_0.filter_by_substring(['abc', 'def'], '') == ['abc', 'def']

    # Test with substring equal to full string
    assert module_0.filter_by_substring(['hello'], 'hello') == ['hello']

    # Test with duplicate strings
    assert module_0.filter_by_substring(['aa', 'aa', 'bb'], 'aa') == ['aa', 'aa']

    # Test with case sensitivity
    assert module_0.filter_by_substring(['Apple', 'apple'], 'apple') == ['apple']

    # Test order preservation
    assert module_0.filter_by_substring(['xxa', 'bxa', 'xa'], 'xa') == ['xxa', 'bxa', 'xa']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-11-02 23:02:06.894835
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test with empty list
    assert module_0.filter_by_substring([], 'a') == []

    # Test with no matches
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde'], 'xyz') == []

    # Test with all matches
    assert module_0.filter_by_substring(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']

    # Test with some matches
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # Test with substring equal to the full string
    assert module_0.filter_by_substring(['hello', 'world'], 'hello') == ['hello']

    # Test with empty substring (matches everything)
    assert module_0.filter_by_substring(['one', 'two', 'three'], '') == ['one', 'two', 'three']

    # Test order preservation
    assert module_0.filter_by_substring(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxy', 'xxxAAA', 'xxx']

    # Test with single character strings
    assert module_0.filter_by_substring(['a', 'b', 'a'], 'a') == ['a', 'a']

    # Test with case sensitivity
    assert module_0.filter_by_substring(['Apple', 'apple', 'APPLE'], 'apple') == ['apple']

    # Test with substring appearing multiple times in a string
    assert module_0.filter_by_substring(['aaab', 'abab', 'bbaa'], 'aa') == ['aaab', 'bbaa']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()