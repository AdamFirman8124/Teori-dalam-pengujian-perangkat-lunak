

# Generated at 2026-11-01 21:27:01.689148
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test with multiple matches
    assert module_0.filter_by_substring(['apple', 'banana', 'grape', 'pineapple'], 'apple') == ['apple', 'pineapple']

    # Test with no matches
    assert module_0.filter_by_substring(['cat', 'dog', 'bird'], 'fish') == []

    # Test with empty list
    assert module_0.filter_by_substring([], 'abc') == []

    # Test with empty substring (matches everything)
    assert module_0.filter_by_substring(['a', 'b', 'c'], '') == ['a', 'b', 'c']

    # Test with substring equal to full string
    assert module_0.filter_by_substring(['hello', 'world'], 'hello') == ['hello']

    # Test with substring in middle of string
    assert module_0.filter_by_substring(['xxabcxx', 'abc', 'ab'], 'abc') == ['xxabcxx', 'abc']

    # Test with case sensitivity
    assert module_0.filter_by_substring(['Hello', 'hello'], 'hello') == ['hello']

    # Test with single character substring
    assert module_0.filter_by_substring(['cat', 'dog', 'cow'], 'o') == ['dog', 'cow']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-11-01 21:27:43.388157
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test with normal case - some strings match
    assert module_0.filter_by_substring([], 'a') == []
    
    # Test with multiple matches
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    
    # Test with substring 'b'
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde', 'array'], 'b') == ['abc', 'bcd']
    
    # Test with substring that matches all
    assert module_0.filter_by_substring(['a', 'ab', 'abc'], 'a') == ['a', 'ab', 'abc']
    
    # Test with no matches
    assert module_0.filter_by_substring(['xyz', 'def'], 'q') == []
    
    # Test with empty substring - should return all strings
    assert module_0.filter_by_substring(['abc', 'def'], '') == ['abc', 'def']
    
    # Test with exact match
    assert module_0.filter_by_substring(['hello', 'world'], 'hello') == ['hello']
    
    # Test with substring longer than some strings
    assert module_0.filter_by_substring(['ab', 'abc', 'abcd'], 'abc') == ['abc', 'abcd']
    
    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-11-01 21:28:14.907548
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test with empty list
    assert module_0.filter_by_substring([], 'john') == []

    # Test basic filtering - substring present in some elements
    assert module_0.filter_by_substring(
        ['apple', 'banana', 'grape', 'pineapple'], 'apple'
    ) == ['apple', 'pineapple']

    # Test substring not present in any element
    assert module_0.filter_by_substring(['cat', 'dog', 'bird'], 'fish') == []

    # Test exact match only
    assert module_0.filter_by_substring(['hello', 'world', 'hello'], 'hello') == [
        'hello', 'hello'
    ]

    # Test empty substring (matches everything)
    assert module_0.filter_by_substring(['abc', 'def'], '') == ['abc', 'def']

    # Test case sensitivity
    assert module_0.filter_by_substring(['Apple', 'apple', 'APPLE'], 'apple') == ['apple']

    # Test substring at beginning, middle, and end
    assert module_0.filter_by_substring(['prefix_data', 'mid_dle', 'data_suffix'], 'data') == [
        'prefix_data', 'data_suffix'
    ]

    # Test single character substring
    assert module_0.filter_by_substring(['cat', 'dog', 'cow'], 'o') == ['dog', 'cow']

    # Test with duplicate values
    assert module_0.filter_by_substring(['aa', 'bb', 'aa'], 'aa') == ['aa', 'aa']

    # Test longer substring than some strings
    assert module_0.filter_by_substring(['ab', 'abc', 'abcd'], 'abcd') == ['abcd']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()

# Generated at 2026-11-01 21:28:40.612082
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Empty list returns empty list
    assert module_0.filter_by_substring([], 'a') == []

    # Basic filtering: only strings containing the substring
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde'], 'a') == ['abc']
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde'], 'bc') == ['abc', 'bcd']

    # Multiple matches preserve order and duplicates
    assert module_0.filter_by_substring(['abc', 'bcd', 'abc'], 'abc') == ['abc', 'abc']

    # No matches returns empty list
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde'], 'xyz') == []

    # Empty substring matches everything
    assert module_0.filter_by_substring(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']

    # Substring in the middle of the string
    assert module_0.filter_by_substring(['hello', 'world', 'help'], 'ell') == ['hello', 'help']

    # Matching is case-sensitive
    assert module_0.filter_by_substring(['ABC', 'abc'], 'abc') == ['abc']

    # Whole string equals substring
    assert module_0.filter_by_substring(['a', 'ab', 'ba'], 'a') == ['a', 'ab', 'ba']

# Generated at 2026-11-01 21:29:27.407991
# Unit test for function filter_by_substring
def test_filter_by_substring():
    # Test with a normal case: multiple matches
    assert module_0.filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

    # Test with substring appearing in the middle of strings
    assert module_0.filter_by_substring(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']

    # Test with no matches
    assert module_0.filter_by_substring(['dog', 'cat', 'bird'], 'fish') == []

    # Test with empty input list
    assert module_0.filter_by_substring([], 'a') == []

    # Test with empty substring: every string contains the empty string
    assert module_0.filter_by_substring(['a', 'b', 'c'], '') == ['a', 'b', 'c']

    # Test with substring equal to a full string
    assert module_0.filter_by_substring(['hello', 'world', 'hello world'], 'hello world') == ['hello world']

    # Test case sensitivity
    assert module_0.filter_by_substring(['Apple', 'apple', 'APPLE'], 'apple') == ['apple']

    # Test with single character substring
    assert module_0.filter_by_substring(['cat', 'dog', 'cot'], 'o') == ['dog', 'cot']

    # Test that the result preserves original order
    assert module_0.filter_by_substring(['bca', 'abc', 'cba'], 'a') == ['bca', 'abc', 'cba']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_substring()