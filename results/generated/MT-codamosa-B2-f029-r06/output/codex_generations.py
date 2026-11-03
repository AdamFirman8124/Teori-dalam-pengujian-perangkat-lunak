

# Generated at 2026-11-02 16:46:03.474063
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Basic filtering: strings starting with the given prefix
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # Prefix matching full string
    assert module_0.filter_by_prefix(['abc', 'abcd', 'abcde'], 'abc') == ['abc', 'abcd', 'abcde']

    # No matches returns empty list
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'z') == []

    # Empty prefix returns all strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']

    # Empty input list returns empty list
    assert module_0.filter_by_prefix([], 'a') == []

    # Empty input list with empty prefix returns empty list
    assert module_0.filter_by_prefix([], '') == []

    # Case sensitivity check
    assert module_0.filter_by_prefix(['Apple', 'apple'], 'A') == ['Apple']

    # Single element list matching prefix
    assert module_0.filter_by_prefix(['hello'], 'he') == ['hello']

    # Single element list not matching prefix
    assert module_0.filter_by_prefix(['hello'], 'x') == []

# Generated at 2026-11-02 16:47:59.643117
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with a common prefix
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    
    # Test with another prefix
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']
    
    # Test with prefix matching multiple items
    assert module_0.filter_by_prefix(['apple', 'banana', 'apricot', 'cherry'], 'ap') == ['apple', 'apricot']
    
    # Test with no matching strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'z') == []
    
    # Test with empty prefix (should return all strings)
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']
    
    # Test with empty input list
    assert module_0.filter_by_prefix([], 'a') == []
    
    # Test with exact match (string equals prefix)
    assert module_0.filter_by_prefix(['abc', 'abcdef'], 'abc') == ['abc', 'abcdef']
    
    # Test with prefix longer than some strings
    assert module_0.filter_by_prefix(['ab', 'abc'], 'abc') == ['abc']
    
    # Test case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple'], 'A') == ['Apple']
    
    # Test preserving original order
    assert module_0.filter_by_prefix(['a1', 'b1', 'a2', 'b2', 'a3'], 'a') == ['a1', 'a2', 'a3']
    
    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-02 16:50:26.159756
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test basic filtering
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    
    # Test empty list
    assert module_0.filter_by_prefix([], 'a') == []
    
    # Test no matches
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'z') == []
    
    # Test empty prefix returns all strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']
    
    # Test prefix matching entire string
    assert module_0.filter_by_prefix(['abc', 'abcde', 'xyz'], 'abc') == ['abc', 'abcde']
    
    # Test all strings match prefix
    assert module_0.filter_by_prefix(['apple', 'apricot', 'avocado'], 'a') == ['apple', 'apricot', 'avocado']
    
    # Test case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple'], 'A') == ['Apple']
    
    # Test single character prefix
    assert module_0.filter_by_prefix(['cat', 'dog', 'cow'], 'c') == ['cat', 'cow']
    
    # Test prefix longer than strings
    assert module_0.filter_by_prefix(['ab', 'cd'], 'abc') == []
    
    print("All tests passed!")


# Run the test
test_filter_by_prefix()

# Generated at 2026-11-02 16:53:10.204114
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Basic filtering
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # Prefix matching multiple items
    assert module_0.filter_by_prefix(['apple', 'banana', 'apricot', 'cherry'], 'ap') == ['apple', 'apricot']

    # No matches returns empty list
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'z') == []

    # Empty prefix returns all strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']

    # Empty input list returns empty list
    assert module_0.filter_by_prefix([], 'a') == []

    # Full string as prefix (exact match)
    assert module_0.filter_by_prefix(['hello', 'world'], 'hello') == ['hello']

    # Case sensitivity check
    assert module_0.filter_by_prefix(['Apple', 'apple'], 'A') == ['Apple']

    # Prefix longer than some strings
    assert module_0.filter_by_prefix(['ab', 'abc', 'abcd'], 'abc') == ['abc', 'abcd']

    # Duplicates preserved
    assert module_0.filter_by_prefix(['aa', 'aa', 'bb'], 'a') == ['aa', 'aa']

    # Order preserved
    assert module_0.filter_by_prefix(['ccc', 'caa', 'cbb'], 'c') == ['ccc', 'caa', 'cbb']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-02 16:54:19.206656
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with an empty list
    assert module_0.filter_by_prefix([], "a") == []

    # Test with a normal case
    assert module_0.filter_by_prefix(["abc", "bcd", "cde", "array"], "a") == ["abc", "array"]

    # Test with empty prefix (should return all strings)
    assert module_0.filter_by_prefix(["abc", "bcd", "cde"], "") == ["abc", "bcd", "cde"]

    # Test with no matching strings
    assert module_0.filter_by_prefix(["abc", "bcd", "cde"], "z") == []

    # Test with prefix matching the entire string
    assert module_0.filter_by_prefix(["abc"], "abc") == ["abc"]

    # Test with prefix longer than string (no match)
    assert module_0.filter_by_prefix(["ab"], "abc") == []

    # Test with duplicate strings
    assert module_0.filter_by_prefix(["apple", "apple", "banana"], "apple") == ["apple", "apple"]

    # Test with case sensitivity
    assert module_0.filter_by_prefix(["Apple", "apple"], "a") == ["apple"]

    # Test with single character prefix
    assert module_0.filter_by_prefix(["cat", "dog", "cow"], "c") == ["cat", "cow"]

    # Test order preservation
    assert module_0.filter_by_prefix(["xyz1", "xyz2", "xyz3"], "xyz") == ["xyz1", "xyz2", "xyz3"]