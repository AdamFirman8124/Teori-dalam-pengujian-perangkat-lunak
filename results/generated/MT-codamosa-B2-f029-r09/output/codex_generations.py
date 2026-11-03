

# Generated at 2026-11-02 12:51:38.158312
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Basic filtering
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'c') == ['cde']

    # Prefix that matches nothing
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z') == []

    # Empty prefix matches everything
    assert module_0.filter_by_prefix(['abc', 'bcd'], '') == ['abc', 'bcd']
    assert module_0.filter_by_prefix([], '') == []

    # Empty input list
    assert module_0.filter_by_prefix([], 'a') == []

    # Prefix matches exactly one full string
    assert module_0.filter_by_prefix(['abc', 'abcd'], 'abc') == ['abc', 'abcd']

    # Case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple'], 'A') == ['Apple']

    print("All tests passed!")

# Generated at 2026-11-02 12:52:46.966139
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
# nonce:4ae6bff3
    # Test with multiple matches
    assert module_0.filter_by_prefix(['abc', 'abd', 'bcd', 'abcde'], 'abc') == ['abc', 'abcde']

    # Test with no matches
    assert module_0.filter_by_prefix(['abc', 'abd', 'bcd'], 'z') == []

    # Test with empty string list
    assert module_0.filter_by_prefix([], 'a') == []

    # Test with empty prefix (should return all strings)
    assert module_0.filter_by_prefix(['abc', 'abd', 'bcd'], '') == ['abc', 'abd', 'bcd']

    # Test with exact match
    assert module_0.filter_by_prefix(['abc', 'abd'], 'abc') == ['abc']

    # Test with single element list
    assert module_0.filter_by_prefix(['hello'], 'he') == ['hello']

    # Test with prefix longer than strings
    assert module_0.filter_by_prefix(['a', 'b'], 'abc') == []

    # Test order preservation
    assert module_0.filter_by_prefix(['axy', 'bxy', 'ayz'], 'a') == ['axy', 'ayz']

    # Test with duplicate strings
    assert module_0.filter_by_prefix(['abc', 'abc', 'xyz'], 'abc') == ['abc', 'abc']

    print("All test cases passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-02 12:53:57.710536
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test with multiple matching strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # Test with no matching strings
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'd') == []

    # Test with empty list
    assert module_0.filter_by_prefix([], 'a') == []

    # Test with empty prefix (should return all strings)
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], '') == ['abc', 'bcd', 'cde', 'array']

    # Test with prefix matching entire string
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'abc') == ['abc']

    # Test with prefix longer than some strings
    assert module_0.filter_by_prefix(['ab', 'abc', 'abcd'], 'abc') == ['abc', 'abcd']

    # Test case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple', 'APple'], 'ap') == ['apple']

    # Test with duplicate strings
    assert module_0.filter_by_prefix(['abc', 'abc', 'bcd'], 'abc') == ['abc', 'abc']

    # Test with single-character prefixes
    assert module_0.filter_by_prefix(['cat', 'car', 'dog'], 'c') == ['cat', 'car']

    print("All test cases passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-02 12:55:01.822826
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Test basic filtering
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'b') == ['bcd']
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'c') == ['cde']

    # Test prefix matching multiple characters
    assert module_0.filter_by_prefix(['apple', 'apply', 'banana', 'app'], 'app') == ['apple', 'apply', 'app']

    # Test no matches
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], 'z') == []

    # Test empty list
    assert module_0.filter_by_prefix([], 'a') == []

    # Test empty prefix returns all strings
    assert module_0.filter_by_prefix(['abc', 'bcd'], '') == ['abc', 'bcd']

    # Test exact match
    assert module_0.filter_by_prefix(['hello', 'world'], 'hello') == ['hello']

    # Test prefix longer than strings
    assert module_0.filter_by_prefix(['a', 'ab'], 'abc') == []

    # Test case sensitivity
    assert module_0.filter_by_prefix(['Apple', 'apple'], 'A') == ['Apple']

    # Test duplicates
    assert module_0.filter_by_prefix(['abc', 'abc', 'abd'], 'abc') == ['abc', 'abc']

    print("All tests passed!")


if __name__ == "__main__":
    test_filter_by_prefix()

# Generated at 2026-11-02 12:55:58.440333
# Unit test for function filter_by_prefix
def test_filter_by_prefix():
    # Basic case: filter strings by a common prefix
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']

    # Prefix that matches nothing
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z') == []

    # Empty list input
    assert module_0.filter_by_prefix([], 'a') == []

    # Empty prefix matches everything (every string starts with '')
    assert module_0.filter_by_prefix(['abc', 'bcd', 'cde'], '') == ['abc', 'bcd', 'cde']

    # Prefix matching all strings (full-string prefix)
    assert module_0.filter_by_prefix(['ab', 'abc', 'abcd'], 'ab') == ['ab', 'abc', 'abcd']

    # Prefix matching only some strings, preserving original order
    assert module_0.filter_by_prefix(['hello', 'world', 'help', 'hero'], 'he') == ['hello', 'help', 'hero']

    # Case sensitivity check
    assert module_0.filter_by_prefix(['Apple', 'apple'], 'a') == ['apple']

    # Prefix equal to an entire string only matches that string
    assert module_0.filter_by_prefix(['cat', 'catalog', 'dog'], 'cat') == ['cat', 'catalog']

    # Duplicates are preserved
    assert module_0.filter_by_prefix(['x', 'x', 'y'], 'x') == ['x', 'x']

    # Single-element list
    assert module_0.filter_by_prefix(['only'], 'only') == ['only']
    assert module_0.filter_by_prefix(['only'], 'no') == []


if __name__ == "__main__":
    test_filter_by_prefix()
    print("All tests passed!")