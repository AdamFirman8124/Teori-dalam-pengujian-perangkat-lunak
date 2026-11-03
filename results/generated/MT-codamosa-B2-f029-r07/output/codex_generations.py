

# Generated at 2026-11-03 02:30:55.079067
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Basic filtering
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # No matches
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'z') == []

    # Empty input list
    assert module_0.filter_by_prefix([], 'a') == []

    # Empty prefix returns all strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']

    # Prefix matches full string and longer strings
    assert module_0.filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']

    # Preserves original order
    assert module_0.filter_by_prefix(['a1', 'b1', 'a2', 'b2'], 'a') == ['a1', 'a2']

    # Case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple', 'banana'], 'A') == ['Apple']
    assert module_0.filter_by_prefix(['Apple', 'apple', 'banana'], 'apple') == ['apple']

    # Prefix longer than any string
    assert module_0.filter_by_prefix(['abc'], 'abcd') == []

    # Prefix equal to a string itself
    assert module_0.filter_by_prefix(['hello', 'help', 'world'], 'hello') == ['hello']

    # Duplicate strings
    assert module_0.filter_by_prefix(['aa', 'aa', 'bb'], 'aa') == ['aa', 'aa']

    # Single character strings
    assert module_0.filter_by_prefix(['a', 'b', 'c'], 'a') == ['a']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-03 02:32:25.962455
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Basic filtering
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'c') == ['cde']

    # No matches
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'd') == []

    # Empty input list
    assert module_0.filter_by_prefix([], 'a') == []

    # Empty prefix matches everything
    assert module_0.filter_by_prefix(['abc', 'bcd'], '') == ['abc', 'bcd']

    # Prefix longer than the strings
    assert module_0.filter_by_prefix(['ab', 'a'], 'abc') == []

    # Exact match
    assert module_0.filter_by_prefix(['abc', 'abcd'], 'abc') == ['abc', 'abcd']

    # Preserves order and duplicates
    assert module_0.filter_by_prefix(['ax', 'bx', 'ay', 'ax'], 'a') == ['ax', 'ay', 'ax']

# Generated at 2026-11-03 02:33:53.817495
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Basic filtering
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']

    # Empty prefix matches everything
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], '') == ['abc', 'bcd', 'cde', 'array']

    # Prefix matches all strings
    assert module_0.filter_by_prefix(['ab', 'abc', 'abcd'], 'ab') == ['ab', 'abc', 'abcd']

    # No matches
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'z') == []

    # Empty input list
    assert module_0.filter_by_prefix([], 'a') == []

    # Exact match prefixes
    assert module_0.filter_by_prefix(['abc', 'ab', 'abcd'], 'abc') == ['abc', 'abcd']

    # Case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple'], 'A') == ['Apple']
    assert module_0.filter_by_prefix(['Apple', 'apple'], 'a') == ['apple']

    # Single element list
    assert module_0.filter_by_prefix(['hello'], 'he') == ['hello']
    assert module_0.filter_by_prefix(['hello'], 'hi') == []

    # Multi-character prefix
    assert module_0.filter_by_prefix(['prefix', 'pre', 'prepare', 'other'], 'pre') == ['prefix', 'pre', 'prepare']

    # Strings with special characters
    assert module_0.filter_by_prefix(['#hash', '@mention', '#hashtag'], '#') == ['#hash', '#hashtag']

    # Duplicate strings
    assert module_0.filter_by_prefix(['abc', 'abc', 'abd'], 'ab') == ['abc', 'abc', 'abd']

# Generated at 2026-11-03 02:34:53.894328
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with empty list
    assert module_0.filter_by_prefix([], 'a') == []

    # Test with no matches
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'x') == []

    # Test with some matches
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'c') == ['cde']

    # Test with prefix matching multiple characters
    assert module_0.filter_by_prefix(['abc', 'abcd', 'abcde', 'bcd'], 'abc') == ['abc', 'abcd', 'abcde']

    # Test with prefix equal to a full string
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'abc') == ['abc']

    # Test with empty prefix (should match all strings)
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']

    # Test with duplicates
    assert module_0.filter_by_prefix(['abc', 'abc', 'xyz'], 'ab') == ['abc', 'abc']

    print("All tests passed!")

# Generated at 2026-11-03 02:35:59.426570
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with multiple matching strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # Test with no matching strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z') == []

    # Test with empty string list
    assert module_0.filter_by_prefix([], 'a') == []

    # Test with empty prefix (should return all strings)
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']

    # Test with prefix matching all strings
    assert module_0.filter_by_prefix(['apple', 'apricot'], 'ap') == ['apple', 'apricot']

    # Test with prefix longer than some strings
    assert module_0.filter_by_prefix(['ab', 'abc', 'abcd'], 'abc') == ['abc', 'abcd']

    # Test with exact match strings
    assert module_0.filter_by_prefix(['hello', 'world'], 'hello') == ['hello']

    # Test with prefix that is an entire string
    assert module_0.filter_by_prefix(['cat', 'catalog', 'dog'], 'cat') == ['cat', 'catalog']

    # Test case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple'], 'A') == ['Apple']

    # Test with duplicate strings
    assert module_0.filter_by_prefix(['abc', 'abc', 'xyz'], 'abc') == ['abc', 'abc']

    # Test with single character prefix
    assert module_0.filter_by_prefix(['one', 'two', 'three'], 't') == ['two', 'three']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()